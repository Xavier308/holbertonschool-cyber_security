#!/bin/bash
nmap -p 21,80,443 --script http-vuln-cve2017-5638,ssl-enum-ciphers,ftp-anon $1 -oN comprehensive_scan_results.txt