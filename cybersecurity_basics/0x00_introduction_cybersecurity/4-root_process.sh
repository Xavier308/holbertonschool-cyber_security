#!/bin/bash
ps -eo user,pid,pcpu,pmem,vsz,rss,tty,stat,start,time,cmd --sort user | grep "^$1" | awk '$5!=0 && $6!=0'
