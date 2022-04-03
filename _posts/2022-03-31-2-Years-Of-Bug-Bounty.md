---
layout: single
title: Two Years of Bug Bounty Hunting
date: 2022-03-31
classes: wide
header:
  teaser: /assets/images/BB.png
tags:
  - Bug Bounty
  - Penetration Testing
--- 

Two years ago this month, I created my first bug bounty account on Bugcrowd. I decided to try my hand at bug bounty hunting for a number of months. As outlined in my earlier article, "100 Days of Bug Hunting" I initially decided to try bug bounty as an experiment to determine its legitimacy. That blog post can be found [here](https://cinzinga.com/Bug-Bounty/). Over these last two years I have consistently bug hunted most days. Throughout this time, my approach and methodology have varied greatly. In this blog post I will outline some insights and statics that I hope you will find interesting.

## About Me

First, a bit about my background. When I started bug bounty hunting in early 2020, I was sophomore (second year) in college. However, I was not entirely new to the field of information security and penetration testing. My interest for the topic really kicked off mid-2019 when I began studying for cyber security certifications such as [CompTIA’s Security+](https://www.comptia.org/certifications/security). 

After earning this certification, I discovered the niche world of practical, hands-on certifications. This introduced me to [eLearnSecurity’s eJPT](https://elearnsecurity.com/product/ejpt-certification/), an entry level pentesting certification, which I earned in mid-2019 as well. Shortly after that, I learned about [Offensive Security’s OSCP](https://www.offensive-security.com/pwk-oscp/) certification. In late 2019 I earned this certification as well. Finally, in early 2020, I passed [eLearnSecurity’s eWPT](https://elearnsecurity.com/product/ewpt-certification/), an entry level web certification.

In early 2020, March 3rd to be exact, I listened to the Darknet Diaries Podcast with dawgyg. This story truly got me interested in bug bounty hunting. At this point, I was tired of taking certifications and wanted to test my tradecraft against real, hardened companies to see if I could hack them. Thus, March 30th of 2020, I registered on Bugcrowd and Hackerone to begin my bug bounty hunting career.

## Bug Bounty Pre-Requisites

My advice for those still in their early days of bug bounty is as follows:

First, some pre-requisites for your hacking journey are an understanding of networking fundamentals. This includes common port numbers, basic subnetting, and different protocols. This information is a cornerstone of any hacker’s education. I highly recommend Professor Messer’s YouTube channel on CompTIA’s Network+. 

Next, one should strive to have a decent understanding of the Linux command line and Bash. I personally do not hack with Linux, I use MacOS so many of the command line elements are identical. This will be important for your recon workflow (pipe, redirect, tee, etc.) and the quick installation of tools via the command line.

Next, I would recommend some familiarity with a programming language. You do not have to be proficient, but a general understanding of common operators, methods, etc. is helpful. In addition to this, a basic understanding of HTML/JavaScript will help with web application hacking.

Finally, have some sort of experience hacking web applications. Like I mentioned, I took eLearnSecurity’s eWPT certification. However, this is totally optional, [PortSwigger’s Web Academy](https://portswigger.net/web-security) is an even more comprehensive, and FREE resource to learn web security. Moreover, things like [HackerOne’s Hacktivity](hackerone.com/hacktivity) and other blog posts are invaluable resources to learn from.

At this point, throw yourself headfirst into bug bounty hunting. Sit down with your web browser and Burp Suite and start hacking. There is no substitute for hands-on-keyboard experience. There are no secret tricks or one-liners or scanning templates that will find you bugs. Success is a function of your time and your effort. Maximize both to maximize success.

## My Hacking Style

Looking back over the last two years, I have seen great evolution in how I approach bug bounty hunting. I my blog post about my first 100 days of bug bounty hunting, I mentioned that I requested a 30-day Burp Suite Pro trial and hacked every day for those 30 days until I earned enough for a year’s license. In those early days I would hack 6-8 hours each day. 

As my understanding of common web vulnerabilities increased, I found I needed to hack for less hours each day. Additionally, the number of private invites I received from my early success allowed for me to hack on more exclusive programs, thus requiring less effort to find bugs.

Early on, I would spend large amounts of time hacking on one single program until I understood every page. I understood where every input was reflected on all other pages. This resulted in dozens of XSS vulnerabilities. While some were duplicates, this deep understanding helped me to stand out in this program and eventually score a handful of critical findings. To this day, I still get invited to exclusive programs by this company for my participation early on.

For those starting out, I recommend this approach. Find a program you like and stick to it. It doesn’t matter if you keep churning out duplicates as long as you continue to learn and hone your methodology against this target. One thing I feel many entry-level hunters do is quickly hop to new programs and run standard scanners against it. While this approach can be lucrative for the fastest folks, it will often lead to disappointment and burnout for those who aren’t the fastest.

These days, my strategy for picking targets is generally as follows. I mainly hunt on On-Demand Bugcrowd programs. These are the programs where they tell you a set start date and time in the future so you can be ready at that time to immediate start hacking. These generally have a $10,000 - $15,000 budget and vulnerabilities are paid out on a sliding scale. I find these style programs generally have a limited scope and favor manual hacking techniques rather than automation. Additionally, on Synack I am very active hunting on the US-only targets. While I understand not everyone has access to these targets, Synack generally has a good number of fresh targets each week for everyone. Again, Synack heavily emphasizes manual hacking techniques rather than automation and widespread scanning.

In addition to these bug bounty programs, I focus as lot on Bugcrowd’s pentest programs (also known as CPTs and NGPTs). For those who do not know, CPTs are generally 1 - 4-week programs where you are the only tester. However, you are required to submit all vulnerabilities of P1-P5 severity in addition to providing extensive documentation as to what was tested as well as write an executive summary. Generally, I have found these programs to pay between $1500 - $5500 depending on the length of the assessment. However, you are not paid-per-vuln like you would be with a bug bounty program.

Similarly, NGPTs are programs where certified hackers are onboarded to look at an exclusive scope. Sometimes this scope has been in a public bug bounty before, other times it has not. The only notable difference is that with NGPTs you are paid-per-vuln in addition to a flat rate.

Finally, I recently joined the [Cobalt Core](https://www.cobalt.io/) just a few months ago. Cobalt places testers on 2-week projects with 1-2 other testers. You are expected to put in ~35 hours of time and in exchange you will receive $1500 per engagement.

These days as I transition into a fulltime job, I am looking for some sustainable long-term options. I find myself gravitating toward CPTs and other “pentest” programs as these are less competitive than traditional bug bounty but provide a steady source of income. Of course, this is personal preference as I live in the United States, a fulltime job is often more lucrative and steadier that bug bounty hunting. This may not be the case for all counties.

## Some Bug Bounty Phases to Avoid

Next up I wanted to talk about some common bug bounty phases you should avoid early on in your career. 

First up avoid spamming low impact reports such as SPF/DKIM/DMARC or clickjacking. While these reports are sometimes accepted, they generally create a lot of noise and add little value to the client.

Somewhat related to this is vulnerability scanners like nuclei. On public programs it is very doubtful that the public templates will yield any non-duplicate bugs. If you can write your own custom templates for zero or n-days, then nuclei can be very lucrative for farming across all bug bounty programs. 

Finally, avoid spamming messages on any platform. This includes platforms like Twitter where some users tend to beg for the payloads and writeups of others. Similarly, triagers review hundreds of reports each day, repeatedly asking them for updates will not cast a favorable light on you. Be respectful, this is a small community and reputation goes a long way.

## Personal Statistics

Alright, at this point I will get off my soapbox and do a bit more technical breakdown of my findings. Moving forward I hope to write more technical blogs explaining some of my findings, similar to [this](https://cinzinga.com/XXE-Case-Studies/) article.

#### Bugcrowd

![](/assets/images/2years/1.png)

![](/assets/images/2years/2.png)

![](/assets/images/2/years3.png)



#### Synack

Statistics on Synack are bit harder to collect.

![](/assets/images/2years/4.png)
