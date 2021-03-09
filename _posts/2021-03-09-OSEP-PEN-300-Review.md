---
layout: single
title: OSEP & PEN-300 Course Review
date: 2021-03-09
classes: wide
header:
  teaser: /assets/images/offsec.png
tags:
  - OSEP
  - Certification
  - Penetration Testing
--- 

I am proud to have completed Offensive Security's Evasion Techniques and Breaching Defenses (PEN-300) course. After successfully passing the 48-hour exam, I earned my Offensive Security Experienced Penetration Tester (OSEP) certification. This is currently the most advanced certification in Offensive Security's penetration testing track.

## Background

Prior to starting PEN-300, I had very little active directory exploitation experience. Through school, I had set up an AD lab which offered great insight into the structure of a domain. Additionally, I had previously passed Pentester Academy’s Certified Red Team Professional (CRTP). Since I took the version of Pentesting With Kali (PWK) that did not include AD attacks (PWKv1), I found CRTP to be the perfect preparation to help bridge the gap between PWKv1 and PEN-300. 

As a fun aside, one of the course authors confirmed I was actually the first student to register for PEN-300!

![](/assets/images/osep/1.png)  

## The Materials

Upon registering for PEN-300, student can expect to receive a ~700-page PDF as well as 19 hours of videos. The syllabus for this course is publicly available on Offensive Security’s site [here](https://www.offensive-security.com/documentation/PEN300-Syllabus.pdf). 

Looking through the syllabus, a lot of the topics were very new to me and I worried I would struggle with only 90 days of lab time in addition to being a full-time student. However, I found this course to be structured in a “crawl, walk, run” format, which I greatly enjoyed! Each topic would generally be taught in the following format: history of the technique, theory of the technique, and finally exploitation using the technique. Moreover, the course instructed students on manually coding tools similar to `PsExec.exe` and `PowerUpSQL.ps1` from scratch in C# to better understand the underlying mechanisms of the attack. While I had minor experience in C/C++ (“Hello World” level), I had never coded in C#. By the end of the course, I was comfortable extrapolating upon the code taught in the course to write my own SQL exploitation tool and undetectable C# shellcode runners.

Once the course moved into some of the more esoteric chapters (Advanced AV Evasion, Kiosk Breakouts, etc.) I found it highly advantageous to watch the videos in addition to following along in the PDF. Generally, the videos are just a narrator reading through the PDF verbatim; however, they have the added benefit of getting to see another person go through the motions. So, if you are a visual learner like me, sometimes it is easier to watch someone use WinDbg rather than reading text instructions on how to use it.

Overall, I found the course materials to be a tremendous reference. While most of the material is nothing new and can be found in many referenced blog posts, I found extreme value in having them all aggregated and distilled down into one PDF reference. Moreover, each chapter had a personal (non-shared) lab to practice the attacks and techniques in. I highly recommend taking the time to create the custom C# code and work through the exercises for each chapter. In addition to this, take the time to try out the “Extra Mile” activities, although be mindful that many of the coding ones can be done on your own time and VM to avoid using up your lab time.

## The Labs

In this section I will talk about the six “challenge” labs at the end of the course. These labs are also private so each student does not have to deal with interruptions other students may create in a shared active directory network.

The first three labs are designed to drill specific skills throughout the course. They are very focused and involve 1-2 major techniques so students can practice chaining attacks in a more open environment. With these first three labs, the paths are generally pretty clear, and the emphasis is on improving one’s tradecraft. 

Labs four through six are where the student is encouraged to struggle, learn, and overcome more challenging and realistic scenarios. Each scenario challenges students to master new initial foothold and lateral movement techniques while reinforcing the common fundamentals of pivoting and post-exploitation enumeration. Unlike other AD labs I have done, there are no CTF-y games of “find the file” to pivot; the majority attack and techniques are covered in the course and improve one’s own knowledge. Make sure you take good notes and understand the “why” each time you get stuck and need to reach out for help or a nudge (join the [InfoSec Prep discord](https://discord.gg/ABmvaUUEyR) if you want to chat with other students). The labs are a reasonable and wholistic review of all the techniques taught throughout the course; however, they are not all encompassing.

## General Questions

Before I (briefly) talk about the exam and my experience, I will answer some questions asked by friends in the InfoSec Prep discord server.

Q. Overall enjoyment of the course?  
A. I loved the course! I found it way more enjoyable than OSCP (perhaps that is because I am more into information security now than I was then?) Regardless, I consider OSCP to be a gateway certification that opens the floodgates to greater learning. This certification was definitely the best that I have taken since my OSCP.

Q. Any Win32 APIs taught in the course?  
A. Yes! This course was the first time I had ever heard of the Win32 APIs (I am a Mac user) and it was a nice introduction. The course material certainly gave me enough experience to go forth on my own and interact with these APIs with C# code.

Q. Favorite and least favorite topics?  
A. The material such as coding malicious macros and kiosk escapes was definitely the most fun for me, but at the same time probably impractical on many penetration tests. However, I still thoroughly enjoyed it. There were definitely some moments in the AV evasion chapters that it got slow to work through, but in the end the knowledge was invaluable!

Q. What makes PEN-300 a “300” level course compared to PEN-200(PWK)?  
A. PWK (PEN-200) is an introductory course to penetration testing. In addition to teaching the basics of many tools (nmap, sqlmap, hashcat, etc.) it teaches students how to think like a penetration tester. By that I mean it teaches students to enumerate, research, enumerate more, and finally exploit. PEN-300 is more advanced than that, it assumes all those initial foothold and privileges escalation skills are a pre-requisite. Beyond the course, it encourages students to exercise creativity based off previous research to go forth and pioneer new techniques and vulnerability research. The tools taught in PEN-300 are not timeless, but the techniques are.

Q. How much time and effort was spent on each module?  
A. The entire course took me approximately 2 months to get through. I was fortunate to have a lot of time over the holidays (December/ January) to work through the material and take detailed notes. While the first 15-16 modules are not strictly AD attacks, I would advise against skipping them to get to the AD stuff faster. A lot of the tradecraft taught in those chapter is important to understanding the course material. Almost everything builds upon the previous chapter and skipping around willy-nilly is not conducive to a positive learning experience. 

Q. Did you have to learn much on your own, outside of the course?  
A. Almost nothing! As previously stated, I only did CRTP prior to beginning OSEP. Once I completed all the material in the labs in about 60 of my 90 days, I actually did start HTB’s Offshore labs; however, I did not enjoy this experience. Much of the AD attacks (once you waded through a lot of the beginning CTF stuff) were easily solved with BloodHound and offered no learning experience or explanation. I solely relied on my own notes from the PDF, videos, and labs to crack the exam.

Q. Was Meterpreter your go-to payload throughout the course or did you utilize other tools / C2s? 
A. Yes! I actually came to love Meterpreter throughout this course. I exclusively used Meterpreter shellcode in my PowerShell and C# shellcode runners. In a future blog post I will outline some of the niche features I discovered in Meterpreter throughout this course!  

Q. How did this course fit within the education process of a novice pentester?  
A. While I cannot fully answer this question (as I am not a professional pentester), I believe that this course is quality education for any aspiring pentester. It is often said that OSCP will get your foot in the door for pentesting, but I believe this course will get you to the top of the list for pentesting applications. Again, I am still currently a student so I cannot answer this question with full confidence, but this certification certainly will not hurt your career!  

Q. 60 versus 90 days?  
A. While I completed all of the course work in approximately 60 days, this track is not for everyone. I am currently a college student and I was blessed to have a few weeks off in December/ January that enabled me to swiftly complete the material and labs.  

Q. Tell us about your exam experience already!!  
A. Okay! Go to the next section.  

## The Exam  

Since this exam is still very new, I am hesitant to talk much about it. However, I will share some brief thoughts as well as statistics from my own attempt. I found the exam to be very fair. That being said I *highly* recommend having gone through the PDF and exercises (if not the extra mile exercises) before taking it. Just because an attack is or is not in the labs does not mean it will or will not be in the exam. However, if you understand each attack in the course and understand each attack in the labs, I have full confidence you can pass the exam. I found the exam to be tough but fair. Moreover, the exam offers multiple ways to pass, a luxury that is not afforded in any of the challenge labs.  

Below are some statistics from my own exam attempt:
-	Started at 10AM
-	Passing points (100pts) in 9 hours
-	Achieved desired objective (secret.txt) in 10.5 hours
-	Submitted report (~65) pages, the next day
-	Received confirmation of pass via email approximate 36 hours after submitting report  

![](/assets/images/osep/2.png)  

## Conclusion

Well, I hope you have enjoyed reading about my PEN-300 course and exam experience. If you have any further questions I can be reached via Twitter/ LinkedIn via my links on the left side of this page, otherwise you can find me in the [InfoSec Prep discord](https://discord.gg/ABmvaUUEyR) under the username `Homebrewer`. Thanks for reading!

![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.com%2FOSEP-PEN-300-Review%2F)
