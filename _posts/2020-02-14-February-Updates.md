---
layout: single
title: February Updates
date: 2020-02-14
classes: wide
header:
  teaser: /assets/images/Exploit-Dev/CVE.png
tags:
  - Exploit-Dev
  - Penetration Testing
  - Certification
---

I figure it is about time for another blog post, as it has been just over one month since my last one. However, I am feeling a little lazy so in this entry I will simply list accomplishments and noteworthy things that have occurred in the last 30 days or so. Honestly each of these on their own warrants a blog post, perhaps in the future I will come back and expand on each of them more.   

## Publications  
- [CVE-2020-6637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-6637)
	* This CVE’s status is still ‘reserved’ because I am allowing the vendor 90 days from discovery before publication
- [CVE-2020-7208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7208)
	* This vulnerability was a joint discovery with [m0rph-1](https://github.com/m0rph-1)
- [CVE-2020-7209](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7209)
	* This vulnerability was a joint discovery with [m0rph-1](https://github.com/m0rph-1)

## Certifications  
- [Penetration Testing Course](https://www.virtualhackinglabs.com/?courses=penetration-testing)

- [Penetration Testing Course Advanced+](https://www.virtualhackinglabs.com/?courses=penetration-testing)

I personally found Virtual Hacking Labs to be very fun and a good change of pace. I enjoyed the flat network topology, so I did not have to worry about dependencies or tunneling. The boxes were generally on the easier side, taking me just 14 days to root 41 machines. Only complaints were that too many privilege escalation routes depended on kernel exploits. Additionally, I found the number of Windows machines to be lacking. Definitely a fun cyber range though.  

## Projects  

- Cowrie Honeypot   
Recently I have set up a honeypot using the Cowrie software. All captured malware samples can be viewed [here](https://github.com/cinzinga/HoneypotStuff/tree/master/Samples). This is purely for personal entertainment as I like to see how many times it gets attacked each day, what commands the bots run, and what malware samples I can catch and identify. 

- GitHub_Autopwn  
I can hardly call this a project of my own; however, it is the child of a discussion m0rph-1 and I had one evening. Both him and I enjoy hunting for CVEs, we thought that a great tool to aid in identification of vulnerable could would be a static code analyzer that can be directed at a GitHub repository. This way it would save us the time of cloning a repo and then running a code analyzer. He is an amazing coder and wrote it in about 24 hours. It helped in earning use CVE-2020-7208 and 7208. The code can be viewed [here](https://github.com/m0rph-1/github_autopwn)


## Other   

- Promotion to Discord Moderator
If you have read some of my other posts, you will notice I mention the [InfoSec-Prep Discord](https://discord.gg/CDfvPb) often. This server contains over 5000 cyber security students or professions, including just shy of 600 OSCP certified members. It is a phenomenal place to learn and share ideas.   




![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.github.io%2FFebruary-Updates%2F)