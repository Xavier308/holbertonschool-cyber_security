#!/bin/bash
hashcat -a 0 -m 0 $1 /usr/share/wordlists/rockyou.txt
