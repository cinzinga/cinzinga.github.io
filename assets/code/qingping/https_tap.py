#!/usr/bin/env python3
import argparse
import datetime as dt
import logging
import ssl
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlsplit, urlunsplit
import http.client

HOP_BY_HOP = {
    "connection", "proxy-connection", "keep-alive",
    "transfer-encoding", "te", "trailer", "upgrade"
}

def now_iso():
    return dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"

def _read_inbound_body(handler):
    te = (handler.headers.get("Transfer-Encoding") or "").lower()
    if "chunked" in te:
        body = bytearray()
        while True:
            size_line = handler.rfile.readline()
            if not size_line:
                break
            size = int(size_line.split(b";", 1)[0], 16)
            if size == 0:
                _ = handler.rfile.readline()  # consume final CRLF (trailers ignored)
                break
            chunk = handler.rfile.read(size)
            body.extend(chunk)
            _ = handler.rfile.read(2)  # CRLF after chunk
        return bytes(body)
    else:
        length = int(handler.headers.get("Content-Length") or 0)
        if length > 0:
            return handler.rfile.read(length)
        return b""

def _absolute_target(handler):
    """
    Returns (scheme, host, port, path_query) for the outbound request.
    Supports absolute-form and origin-form (with Host header).
    """
    if handler.path.startswith("http://") or handler.path.startswith("https://"):
        u = urlsplit(handler.path)
        scheme = u.scheme.lower()
        host = u.hostname
        port = u.port or (443 if scheme == "https" else 80)
        path = urlunsplit(("", "", u.path or "/", u.query, ""))  # no fragment
        return scheme, host, port, path

    hosthdr = handler.headers.get("Host")
    if not hosthdr:
        raise ValueError("Missing Host header for origin-form request")
    if ":" in hosthdr and not hosthdr.endswith("]"):
        host, port_s = hosthdr.rsplit(":", 1)
        try:
            port = int(port_s)
        except ValueError:
            port = 80
    else:
        host, port = hosthdr, 80
    scheme = "http"  # origin-form implies HTTP
    path = handler.path or "/"
    return scheme, host, port, path

def _filter_outbound_headers(handler, target_host):
    headers = {}
    for k, v in handler.headers.items():
        lk = k.lower()
        if lk in HOP_BY_HOP:
            continue
        if lk == "host":
            headers["Host"] = target_host
        else:
            headers[k] = v
    return headers

def _filter_inbound_response_headers(resp_headers):
    headers = []
    for k, v in resp_headers.items():
        lk = k.lower()
        if lk in HOP_BY_HOP:
            continue
        if lk == "content-length":
            continue  # we’ll set it after buffering
        headers.append((k, v))
    return headers

class ProxyHandler(BaseHTTPRequestHandler):
    server_version = "HTTPS-Tap/ProxyUpstream/1.0"

    def log_message(self, fmt, *args):
        logging.info("%s - %s", self.address_string(), fmt % args)

    def _handle_any(self):
        ts = now_iso()
        method = self.command
        try:
            scheme, host, port, path = _absolute_target(self)
        except Exception as e:
            self.send_error(400, f"Bad Request: {e}")
            return

        body = _read_inbound_body(self)

        # Build Host header value (include port if non-default)
        if (scheme == "http" and port != 80) or (scheme == "https" and port != 443):
            host_header = f"{host}:{port}"
        else:
            host_header = host

        out_headers = _filter_outbound_headers(self, host_header)

        # Always use upstream proxy (defaults to 127.0.0.1:8080)
        proxy_host = self.server.upstream_host
        proxy_port = self.server.upstream_port

        try:
            if scheme == "http":
                # HTTP via proxy: send absolute-form URL on request line
                conn = http.client.HTTPConnection(proxy_host, proxy_port, timeout=30)
                absolute_url = f"http://{host_header}{path}"
                conn.request(method, absolute_url, body=body if body else None, headers=out_headers)
            else:
                # HTTPS via proxy: CONNECT tunnel then TLS to target
                conn = http.client.HTTPSConnection(proxy_host, proxy_port, timeout=30)
                conn.set_tunnel(host, port, headers={})  # can add Proxy-Authorization here if needed
                conn.request(method, path, body=body if body else None, headers=out_headers)

            resp = conn.getresponse()
            resp_body = resp.read()
        except Exception as e:
            logging.exception("Upstream request error via %s:%d to %s://%s:%d%s: %s",
                              proxy_host, proxy_port, scheme, host, port, path, e)
            self.send_error(502, f"Bad Gateway: {e}")
            try:
                conn.close()
            except Exception:
                pass
            return

        # Relay response back
        self.send_response(resp.status, resp.reason)
        for k, v in _filter_inbound_response_headers(resp.headers):
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(resp_body)))
        self.send_header("Connection", "close")
        self.end_headers()
        if method != "HEAD" and resp_body:
            self.wfile.write(resp_body)

        try:
            conn.close()
        except Exception:
            pass

        logging.info("[%s] %s %s://%s:%d%s via %s:%d -> %d %s (%d bytes)",
                     ts, method, scheme, host, port, path, proxy_host, proxy_port,
                     resp.status, resp.reason, len(resp_body))

    # Methods
    def do_GET(self): self._handle_any()
    def do_POST(self): self._handle_any()
    def do_PUT(self): self._handle_any()
    def do_DELETE(self): self._handle_any()
    def do_PATCH(self): self._handle_any()
    def do_OPTIONS(self): self._handle_any()
    def do_HEAD(self): self._handle_any()

class ThreadingTLSServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    def __init__(self, server_address, RequestHandlerClass, ssl_context=None, upstream_host="127.0.0.1", upstream_port=8080):
        super().__init__(server_address, RequestHandlerClass)
        self.ctx = ssl_context
        self.upstream_host = upstream_host
        self.upstream_port = upstream_port

    def get_request(self):
        if not self.ctx:
            return super().get_request()
        sock, addr = self.socket.accept()
        try:
            ssock = self.ctx.wrap_socket(sock, server_side=True, do_handshake_on_connect=True)
            return ssock, addr
        except ssl.SSLError as e:
            logging.warning("TLS handshake failed from %s: %s", addr, e)
        except Exception as e:
            logging.exception("Unexpected TLS handshake error from %s: %s", addr, e)
        try:
            sock.close()
        except Exception:
            pass
        return self.get_request()

def sni_logger(sock, server_name, ctx):
    logging.info("Client SNI: %s", server_name)

def build_ssl_context(cert, key):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(certfile=cert, keyfile=key)
    ctx.set_servername_callback(sni_logger)
    ctx.set_alpn_protocols(["http/1.1"])
    return ctx

def main():
    ap = argparse.ArgumentParser(description="Minimal HTTP forward proxy with fixed upstream proxy")
    ap.add_argument("--addr", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=8081)
    ap.add_argument("--cert", help="TLS cert for HTTPS listener (optional)")
    ap.add_argument("--key", help="TLS key for HTTPS listener (optional)")
    ap.add_argument("--upstream-proxy", default="127.0.0.1:8080",
                    help="Upstream HTTP proxy to use for ALL outbound requests (host:port)")
    ap.add_argument("--log", default="-")
    args = ap.parse_args()

    handlers = [logging.StreamHandler(sys.stdout)] if args.log == "-" else [logging.FileHandler(args.log)]
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", handlers=handlers)

    proxy_host, proxy_port = args.upstream_proxy.rsplit(":", 1)
    proxy_port = int(proxy_port)

    ssl_ctx = None
    if args.cert and args.key:
        ssl_ctx = build_ssl_context(args.cert, args.key)
        logging.info("Starting HTTPS listener on https://%s:%d (upstream %s:%d)",
                     args.addr, args.port, proxy_host, proxy_port)
    else:
        logging.info("Starting HTTP listener on http://%s:%d (upstream %s:%d)",
                     args.addr, args.port, proxy_host, proxy_port)

    srv = ThreadingTLSServer((args.addr, args.port), ProxyHandler, ssl_ctx,
                             upstream_host=proxy_host, upstream_port=proxy_port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down...")
    finally:
        srv.server_close()

if __name__ == "__main__":
    main()
