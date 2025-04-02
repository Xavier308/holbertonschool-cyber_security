# Content Discovery

## Description
This project focuses on content discovery techniques used in web application security testing. Through a series of practical exercises, you'll learn how to uncover hidden files, directories, subdomains, and other resources that may not be readily visible but could represent security vulnerabilities.

## Learning Objectives
- Understand what content discovery is and its importance in security
- Learn directory bruteforcing techniques
- Master tools like Gobuster, ffuf, and Burp Suite for content discovery
- Understand the use of wordlists in discovery processes
- Learn about OSINT techniques for information gathering
- Discover how to identify frameworks and technologies used by websites
- Explore DNS subdomain enumeration and fuzzing techniques

## Tasks Overview
1. **Manual Discovery - Secrets in Plain Sight**: Find hidden information in common files like robots.txt and sitemap.xml
2. **Headers Analysis**: Discover secrets hidden in HTTP response headers
3. **Template Investigation**: Identify the origin of website templates using source code analysis
4. **OSINT with Wayback Machine**: Use the Internet Archive to discover historical website information
5. **Directory Bruteforcing with Gobuster**: Use Gobuster's dir mode to discover hidden directories
6. **Subdomain Enumeration with DNS**: Utilize Gobuster's dns mode to find subdomains
7. **Subdomain Fuzzing with ffuf**: Explore alternative ways to discover subdomains
8. **Fuzzing Parameters and Paths**: Use fuzzing techniques to find hidden endpoints
9. **TFTP Brute Forcing**: Discover files on TFTP servers using bruteforce techniques

## Requirements
- Kali Linux environment
- All scripts must be exactly one line long
- All files must end with a newline
- Target machine: Cyber - WebSec 0x04

## Tools Used
- Gobuster (various modes: dir, dns, fuzz, tftp)
- ffuf for fuzzing
- Curl for HTTP request analysis
- Browser developer tools
- Wayback Machine for historical website analysis
- Wappalyzer for technology stack identification

## Resources
- Content discovery guides and methodologies
- OWASP Testing Guide for Content Discovery
- Documentation for tools:
  - dirb
  - nikto
  - sfuzz
  - wfuzz
  - gobuster
  - dirbuster
  - feroxbuster
