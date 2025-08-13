#!/usr/bin/env python3
import argparse
import base64
import datetime as dt
import email.utils
import hashlib
import logging
import os
import ssl
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

# -------------------------------
# Helpers
# -------------------------------

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def httpdate(ts=None):
    """RFC 7231 IMF-fixdate."""
    if ts is None:
        d = dt.datetime.utcnow()
    elif isinstance(ts, (int, float)):
        d = dt.datetime.utcfromtimestamp(ts)
    else:
        d = dt.datetime.utcfromtimestamp(float(ts))
    return f"{WEEKDAYS[d.weekday()]}, {d.day:02d} {MONTHS[d.month-1]} {d.year} {d.hour:02d}:{d.minute:02d}:{d.second:02d} GMT"

def escape_slashes(url: str) -> str:
    # JSON string already quoted later; here we only escape forward slashes to match the sample literally
    return url.replace("/", r"\/")

# -------------------------------
# ZIP responder (serves /firmwares/*)
# -------------------------------

class ZipResponder:
    """Loads the selected ZIP and serves it with correct headers, Range, HEAD, validators."""
    def __init__(self, file_path, date_hdr=None, last_mod=None):
        import time
        self.file_path = file_path
        with open(file_path, "rb") as f:
            self.data = f.read()
        self.size = len(self.data)
        md5_digest = hashlib.md5(self.data).digest()
        self.content_md5_b64 = base64.b64encode(md5_digest).decode("ascii")
        self.etag_hex_upper = hashlib.md5(self.data).hexdigest().upper()
        # dates
        self.date_hdr = date_hdr or httpdate()
        if last_mod:
            self.last_mod = last_mod
        else:
            try:
                self.last_mod = httpdate(os.path.getmtime(file_path))
            except Exception:
                self.last_mod = self.date_hdr

    def _send_status_only(self, handler, code, extra=None):
        handler.send_response(code)
        # OSS/CDN-ish headers that appear regardless
        handler.send_header("Server", "Tengine")
        handler.send_header("Connection", "keep-alive")
        handler.send_header("Accept-Ranges", "bytes")
        # Pinned/rolling Date
        handler.send_header("Date", handler.server.pin_date or httpdate())
        if extra:
            for k, v in extra:
                handler.send_header(k, v)
        handler.end_headers()

    def handle(self, handler):
        """Serve 200/206/304/416 as appropriate. Returns True if handled."""
        etag = f"\"{self.etag_hex_upper}\""

        # Conditional GET: If-None-Match / If-Modified-Since
        inm = handler.headers.get("If-None-Match")
        if inm and (etag in inm or "*" in inm):
            self._send_status_only(handler, 304, [("ETag", etag)])
            return True

        ims = handler.headers.get("If-Modified-Since")
        if ims:
            try:
                ims_dt = email.utils.parsedate_to_datetime(ims)
                lm_dt = email.utils.parsedate_to_datetime(self.last_mod)
                if ims_dt and lm_dt and ims_dt >= lm_dt:
                    self._send_status_only(handler, 304, [("ETag", etag)])
                    return True
            except Exception:
                pass

        # Range handling (single range; omit Content-MD5 on 206)
        rng = handler.headers.get("Range")
        if_range = handler.headers.get("If-Range")
        use_range = False
        start, end = 0, self.size - 1

        if rng and rng.startswith("bytes="):
            # Honor If-Range only when validator matches (ETag or Last-Modified)
            if if_range:
                ok = False
                try:
                    if if_range.startswith("W/") or if_range.startswith("\""):
                        ok = (if_range.strip() == etag)
                    else:
                        if_dt = email.utils.parsedate_to_datetime(if_range)
                        lm_dt = email.utils.parsedate_to_datetime(self.last_mod)
                        ok = (if_dt and lm_dt and if_dt >= lm_dt)
                except Exception:
                    ok = False
                if not ok:
                    rng = None  # fall back to full entity

        if rng and rng.startswith("bytes="):
            spec = rng.split("=", 1)[1].strip()
            if "," in spec:
                # multiple ranges unsupported -> send full entity
                pass
            else:
                s, _, e = spec.partition("-")
                try:
                    if s == "" and e:  # suffix form: "-500"
                        length = int(e)
                        if length <= 0:
                            raise ValueError
                        start = max(0, self.size - length)
                        end = self.size - 1
                    else:
                        start = int(s) if s else 0
                        end = int(e) if e else (self.size - 1)
                    if start < 0 or end < start or start >= self.size:
                        self._send_status_only(handler, 416, [("Content-Range", f"bytes */{self.size}")])
                        return True
                    use_range = True
                except Exception:
                    self._send_status_only(handler, 416, [("Content-Range", f"bytes */{self.size}")])
                    return True

        # Common headers
        common = [
            ("Server", "Tengine"),
            ("Content-Type", "application/zip"),
            ("Accept-Ranges", "bytes"),
            ("ETag", etag),
            ("Last-Modified", self.last_mod),
            ("Connection", "keep-alive"),
            ("Date", handler.server.pin_date or httpdate()),
            # Decorative / pass-through-ish headers to resemble OSS/CDN
            ("x-oss-request-id", "SIMULATED"),
            ("x-oss-cdn-auth", "success"),
            ("x-oss-object-type", "Normal"),
            ("x-oss-storage-class", "Standard"),
            ("x-oss-server-time", "33"),
            ("Via", "ens-cache9.l2us3[0,0,200-0,H]"),
            ("X-Cache", "HIT TCP_MEM_HIT dirn:-2:-2"),
            ("Timing-Allow-Origin", "*"),
        ]

        if use_range:
            chunk = self.data[start:end+1]
            handler.send_response(206, "Partial Content")
            for k, v in common:
                handler.send_header(k, v)
            handler.send_header("Content-Range", f"bytes {start}-{end}/{self.size}")
            handler.send_header("Content-Length", str(len(chunk)))
            handler.end_headers()
            if handler.command != "HEAD":
                handler.wfile.write(chunk)
        else:
            handler.send_response(200, "OK")
            for k, v in common:
                handler.send_header(k, v)
            handler.send_header("Content-Length", str(self.size))
            handler.send_header("Content-MD5", self.content_md5_b64)  # for full entity only
            handler.end_headers()
            if handler.command != "HEAD":
                handler.wfile.write(self.data)

        logging.info("Served ZIP%s (%d bytes total)",
                     f" [{start}-{end}]" if use_range else "", self.size)
        return True

# -------------------------------
# HTTP Handler (routes + JSON)
# -------------------------------

class Handler(BaseHTTPRequestHandler):
    server_version = "nginx/1.20.1"   # for the /checkUpdate response
    sys_version = ""                  # suppress Python version

    def log_message(self, fmt, *args):
        logging.info("%s - %s", self.address_string(), fmt % args)

    def _send_checkupdate_json(self):
        # Compute MD5 (hex, lowercase) of the provided ZIP file’s bytes
        md5_hex = self.server.zip_md5_hex_lower

        # Build the app_url exactly like your sample (escaped slashes)
        # Path structure is configurable via --firmware-path-prefix (default mirrors your example).
        app_url_plain = f"https://qingfseu.cleargrass.com{self.server.fw_path_prefix}{md5_hex}_4_5_6_0156.zip"
        app_url = escape_slashes(app_url_plain)

        payload = (
            '{"data":{"upgrade_sign":1,"version":"4.5.6_0156","file_md5":"%s",'
            '"app_url":"%s","desc":"\\u4fee\\u590d\\u4e86\\u4e00\\u4e9b bug\\u3002\\r\\n\\r\\nFixed some bugs.",'
            '"type":0},"code":0}'
        ) % (md5_hex, app_url)

        body = payload.encode("utf-8")
        # Match the headers you asked for (with dynamic Date and Content-Length)
        self.send_response(HTTPStatus.OK)
        self.send_header("Server", "nginx/1.20.1")
        self.send_header("Date", self.server.pin_date or httpdate())
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Connection", "keep-alive")
        self.send_header("Vary", "Accept-Encoding")
        self.send_header("X-Powered-By", "PHP/7.4.33")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)
        logging.info("Served checkUpdate JSON (md5=%s)", md5_hex)

    def do_ANY(self):
        host = (self.headers.get("Host") or "").lower()
        path = self.path or "/"

        # Route A: JSON update info
        if host == "qing.cleargrass.com" and path.startswith("/firmware/checkUpdate"):
            self._send_checkupdate_json()
            return

        # Route B: Serve ZIP
        if host == "qingfseu.cleargrass.com" and path.startswith("/firmwares/"):
            handled = self.server.zip_responder.handle(self)
            if handled:
                return

        # Otherwise: 404
        self.send_error(404, "Not Found")

    # Map HTTP methods
    def do_GET(self): self.do_ANY()
    def do_HEAD(self): self.do_ANY()
    def do_POST(self): self.do_ANY()
    def do_OPTIONS(self): self.do_ANY()

# -------------------------------
# TLS server wrapper
# -------------------------------

class ThreadingTLSServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    allow_reuse_address = True
    def __init__(self, server_address, RequestHandlerClass, ssl_context=None):
        super().__init__(server_address, RequestHandlerClass)
        self.ctx = ssl_context
        # filled by main():
        self.zip_responder = None
        self.zip_md5_hex_lower = None
        self.fw_path_prefix = "/firmwares/202501/_update_param__"  # default like your example
        self.pin_date = None  # if you want a fixed Date header; else None for "now"

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

def build_ssl_context(cert, key):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(certfile=cert, keyfile=key)
    # We want HTTP/1.1
    try:
        ctx.set_alpn_protocols(["http/1.1"])
    except Exception:
        pass
    return ctx

# -------------------------------
# Main
# -------------------------------

def main():
    ap = argparse.ArgumentParser(description="Serve update JSON and a ZIP payload over HTTPS.")
    ap.add_argument("--addr", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=443)
    ap.add_argument("--cert", required=True, help="TLS certificate (PEM)")
    ap.add_argument("--key", required=True, help="TLS private key (PEM)")
    ap.add_argument("--zip-file", required=True, help="Path to the ZIP to serve")
    ap.add_argument("--firmware-path-prefix",
                    default="/firmwares/202501/_update_param__",
                    help="Prefix after host in app_url (must end with '__'). "
                         "Default: /firmwares/202501/_update_param__")
    ap.add_argument("--pin-date", default=None,
                    help="Optional fixed Date header value (RFC 7231). If omitted, uses current time.")
    ap.add_argument("--log", default="-")
    args = ap.parse_args()

    # Logging
    handlers = [logging.StreamHandler(sys.stdout)] if args.log == "-" else [logging.FileHandler(args.log)]
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", handlers=handlers)

    # Load ZIP + digests
    with open(args.zip_file, "rb") as f:
        zip_bytes = f.read()
    zip_md5_hex_lower = hashlib.md5(zip_bytes).hexdigest()

    # TLS context
    ssl_ctx = build_ssl_context(args.cert, args.key)

    # Server
    srv = ThreadingTLSServer((args.addr, args.port), Handler, ssl_ctx)
    srv.zip_responder = ZipResponder(args.zip_file)
    srv.zip_md5_hex_lower = zip_md5_hex_lower
    srv.fw_path_prefix = args.firmware_path_prefix if args.firmware_path_prefix.endswith("__") else (args.firmware_path_prefix + "__")
    srv.pin_date = args.pin_date

    logging.info("Listening on https://%s:%d", args.addr, args.port)
    logging.info("Responding to Host=qing.cleargrass.com path=/firmware/checkUpdate* with ZIP md5=%s", zip_md5_hex_lower)
    logging.info("Serving ZIP on Host=qingfseu.cleargrass.com path=/firmwares/* from %s (size=%d)",
                 args.zip_file, srv.zip_responder.size)

    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down...")
    finally:
        srv.server_close()

if __name__ == "__main__":
    main()

