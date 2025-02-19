#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-MD5 $1
