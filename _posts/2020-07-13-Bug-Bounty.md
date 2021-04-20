---
layout: single
title: 100 Days of Bug Hunting
date: 2020-7-13
classes: wide
header:
  teaser: /assets/images/BB.png
tags:
  - Bug Bounty
  - Penetration Testing
---  

On April 1st 2019, I decided to try my hand at bug bounty hunting. What started initially as a short experiment quickly evolved into a daily obsession and a full-time hobby. In this post I will talk briefly about my experiences and impressions.  

## Preface    

From my time in the InfoSec Prep discord, as well as on Twitter, I gleaned the community’s views on bug bounty hunting are very polarized. Half consider it to be a scam - slave labor - where big name companies outsource their security and underpay researchers. Then, there are the other half who point to influential members of the community such as Stok and NahamSec who make a living off such work. There are even researchers like Dawgyg who [publicly expresses their displeasure for not making $1mil in 1 year off of their bug bounty work](https://twitter.com/thedawgyg/status/1210293014586777600)! Thus, I decided to just dive in headfirst and see where my views aligned after a set period of time.  

## Goals

Initially I sat down to hash out my goals for this endeavor. I did not simply want to aimlessly throw payloads at websites for a month without any end goal. After a bit of thought I determined the following (in order of increasing difficulty):
-	Find at least one valid, paid bug (not a duplicate)
-	Purchase a Burp Pro license with the profits
	-	The Burp Pro trial is 30 days, so this seemed like a good goal to add
-	See how high of a rank I could achieve in 1 month
-	Determine if this venture is viable long term for a beginner like myself  

To preface any further discussion, the fact that I am writing this after three months as opposed to just one, should give some indication that the answer to the final bullet point is “yes”.   

## 30 Days… and Beyond  
Starting out, I decided to hunt on BugCrowd. I cannot exactly tell you why I chose them; however, I can tell you that I am happy I did. HackerOne (H1) antidotally seems to be the bigger name in bug bounty hunting, but I am not sure why. Personally, I fell in love with BugCrowd (BC) and found myself hunting with them daily. Perhaps the main advantage BC has to H1 is that duplicates on BC still receive points. This helps beginners like me feel more accomplished and gain rank despite not being the first to find a bug. Moreover, after some shaky and `Not Applicable` submissions on BC, I had a huge stroke of beginner’s luck. Within my first week I found a Priority 2 (P2) stored XSS on one of the largest travel sites in the world. Not long after that (and after many more duplicates) I began to receive private invites.  

In my opinion, private invites are a core of component of bug bounty hunting success. Thousands of researchers aimlessly stab at public programs and they are extremely picked over. Thus, getting into a more selective program is almost a pre-requisite to ranking up and succeeding. In another stroke of beginner’s luck one of my first private programs ended up becoming both my most lucrative and favorite company to hunt for. I became enthralled with bug hunting. Each day I hunted from approximately 6AM to Noon.  

Remember my goals outlined above? My first paid bug actually knocked out goal #1 and #2 simultaneously. It felt very good to have used the Burp Pro trial to earn enough to buy a full Burp Pro license for myself. Additionally, in my first 30 days I had climbed globally from ~96,000 in rank to top 2500. However, while the money and the rank were cool accomplishments, I found the knowledge gained through these endeavors to be priceless. I am extremely gifted to have patient and understanding mentors from the InfoSec Prep discord (mainly [Tib3rius](https://twitter.com/TibSec)) that advise me almost daily. This alone was enough to keep me coming back. Thus, I continued bug hunting for another month … and another, until finally I decided this blog post was long overdue.  

At the end of 100 days my notable stats are as follows:
-	Top 330 on BugCrowd (top 0.35% globally)
-	Background checked on BugCrowd ("Next Gen Pen Test" eligible)
-	Four critical submission (SQLi)
-	Applied and accepted to Synack Red Team
-	Enough rewards to buy 100 years of Burp Pro licenses  

Ironically enough in this time I have never submitted a paid bug to HackerOne. This is on my to-do list and I feel as though I need to become more established there; however, with two other sites to hack for I find my time is limited.  


## Conclusion    

As a college student, bug bounty hunting has been an amazing opportunity. It has allowed me to target actual websites to hone my web application testing skill while simultaneously practice writing short reports. The knowledge gained has been free and beyond that of any certification I have taken thus far. I fully intend to continue learning and submitting bugs as I can while finishing my degree. Perhaps at that point in time I will choose to pursue this as a full-time career. It’s tough to know for certain but success is easily obtainable for those who put in the hours each day. There is no “big secret” to bug hunting that you will learn from YouTube videos or blog posts, simply dedicate the time and you will see the results. Go start hunting today!  

## Profiles  
[BugCrowd](https://bugcrowd.com/cinzinga)  

[HackerOne](https://hackerone.com/cinzinga)  

Synack.- private.  



![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.github.io%2FBug-Bounty%2F)




