---
layout: single
title: Linux Privilege Escalation Course Review
date: 2020-01-05
classes: wide
header:
  teaser: /assets/images/root.png
tags:
  - OSCP
  - Penetration Testing
---


This post is a brief review of Tib3rius’ [Linux Privilege Escalation](https://www.udemy.com/course/linux-privilege-escalation/?referralCode=0B0B7AA1E52B4B7F4C06) course, available on Udemy.  

## Background   

I learned about this course from the [InfoSec-Prep Discord](https://discord.gg/TyZpfAs), which is a phenomenal resource for those planning to take the OSCP. Tib3rius is an administrator in this Discord server and is active almost every day, answering questions and providing advice about penetration testing. He is also the author of [AutoRecon](https://github.com/Tib3rius/AutoRecon), an incredibly helpful network reconnaissance tool that I found crucial to have during both PWK and the OSCP.   

## About the Course   

The course is broken up into three main sections: a brief introduction, common privilege escalation techniques, and a conclusion. All together there are 14 videos lasting about 1.5 hours. The course also comes with a vulnerable virtual machine for the student to set up and practice alongside the videos. Additionally, the course allows the student to download the slides as well as the HD videos to view offline if desired.  

The course states that the only prerequisite is a basic familiarity with Linux, which is understandable as this is a course on Linux privilege escalation. Moreover, the intended audience is those currently taking, or planning on taking, PWK/OSCP. Finally, this course states that all students will learn multiple methods of privilege escalation, as well as the *why* behind each method.  

## My Thoughts  

Personally, I found the course extremely informative and very pleasant to watch. The teacher alternates between explaining slides shown on screen and demonstrating the concepts just explained against a Debian VM.  

In the introduction videos, Tib3rius spends time to ensure all students are familiar with file permissions, directory permissions, and special permissions on Linux systems. Moreover, he explains different ways to spawn root shells, and recommends post-exploit enumeration scripts to use.  

Following this brief introduction, the teacher explains common Linux privilege escalation techniques that one may find useful during the PWK course. In addition to explaining the techniques, Tib3rius does a great job of explaining what the vulnerable component is that allows for each exploit to work.  

While I took this course after having completed the OSCP, I still found myself taking thorough notes and screenshots on each lecture. Despite being only 90 minutes of videos, each minute is packed with a ton of information. Furthermore, if you choose to follow along and attack the virtual VM like I did, the course lasts a lot longer than just 1.5 hours. With regards to the level of the content, I found some of the techniques to be beyond anything I personally encountered in PWK/OSCP but still extremely valuable information for a student penetration tester. 

## Conclusion  

The course ends by providing some ideas for privilege escalation strategy or methodology. After speaking with the teacher of this course, I learned he plans to create a class on Windows privilege escalation as well. Having completed PWK/OSCP, I know the PDF and videos tend to be a bit lacking in the privilege escalation section. Thus, I believe that watching Tib3rius’ course on the topic is sure to fill in any knowledge gaps a student might have during PWK.  


![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.github.io%2Ftib-course-review%2F)