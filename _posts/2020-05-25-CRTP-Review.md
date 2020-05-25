---
layout: single
title: CRTP Exam Review
date: 2020-5-25
classes: wide
header:
  teaser: /assets/images/CRTP/logo.png
tags:
  - Certification
  - Penetration Testing
---

This last week I took and passed the Certified Red Team Professional exam. [Certified Red Team Professional (CRTP)](https://www.pentesteracademy.com/activedirectorylab) is the introductory level Active Directory Certification offered by Pentester Academy. The course is taught by Nikhil Mittal, who is the author of [Nishang](https://github.com/samratashok/nishang) and frequently speaks at various conventions.

## Labs   

The course is very well made and quite comprehensive. The provided materials are 30+ videos, a PDF of the slides, and a PDF with exercise solutions. The videos can easily be watched at 1.5x speed to work through the material at a rapid pace. There are 3-5 learning objectives after each course topic that allow the student to gain hands on experience in the simulated active directory lab.  

One key thing to note is that the labs are educational labs, not challenge labs like in PWK. This means that the course walks you through the steps to get Domain Admin and Enterprise Admin, the student does not get to go out and practice on their own. Thus, once the student knows the path to DA it is static and does not change.  

The course covers many great topics. These topics include manual AD enumeration and the use BloodHound, privilege escalation and persistence, and detection and defense.  

I personally booked 30 days of CRTP lab time and I felt like this was sufficient time to work through the course materials and practice most learning objectives twice. 

![](/assets/images/CRTP/1.png)  

## Exam  

In my opinion the exam truly made this course worth it. The exam contains 5 machines that the user must pivot between in order to obtain command execution on each of them. This must be accomplished in 24 hours with another 48 hours to write a professional findings report. The exam instructions provide the student with a large hint in case you find yourself stuck. They state that no brute forcing with a dictionary is required. So, if you find yourself trying certain domain privilege escalation attacks that required cracking, know that you are in a rabbit hole.  

Most of the pivots require additional research and careful examination of findings. The first pivot was the most difficult and took me about 6 hours to achieve. After that the second pivot was medium difficulty, taking about 2 hours. At this point, the last three pivots are trivial and took me about 2 hours total. I started the exam at 8AM and had fully compromised the exam network by 6PM.  

I strongly recommend getting familiar with BloodHound and learning what each node/ edge represents.

In the end my lab report totaled about 20 pages and for my efforts I was awarded the CRTP two days after submitting it.

## Conclusion  
I highly recommend CRTP for those like me who have OSCP but feel as though they lack active directory experience. I greatly enjoyed how I did not have to use a VM for the course since students RDP directly into their foothold machine. Everything in the course is done via PowerShell which provided a great learning experience. Moreover, the course can be completed relatively quickly in just 30 days. In the future I will definitely consider taking the level 2 AD course: CRTE.


![](/assets/images/CRTP/2.png)   



![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.github.io%2FCRTP-Review%2F)


