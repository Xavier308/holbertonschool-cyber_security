# Upload Vulnerabilities

## Description
This project explores file upload vulnerabilities in web applications. Through practical exercises, you'll learn to identify and exploit unrestricted file upload vulnerabilities, bypass various security controls, and understand the risks associated with insecure file upload implementations.

## Learning Objectives
- Understand unrestricted file upload vulnerabilities and their security implications
- Learn how to bypass client-side validation mechanisms
- Discover techniques to circumvent server-side file type validation
- Explore magic number manipulation to disguise malicious files
- Learn methods to bypass file size restrictions
- Understand what web shells are and how they can be deployed
- Recognize the relationship between MIME types and upload security
- Learn about content-type spoofing techniques
- Understand secure file upload practices and mitigation strategies

## Tasks Overview
1. **Subdomain Discovery**: Identify which subdomain contains a vulnerable file upload feature
2. **Client-Side Filter Bypass**: Bypass JavaScript-based file type restrictions
3. **Special Character Exploitation**: Use special characters in filenames to bypass server-side validation
4. **Magic Number Manipulation**: Modify file signatures to disguise malicious files as benign types
5. **File Length Restriction Bypass**: Overcome file size limitations to upload larger payloads

## Requirements
- Kali Linux environment
- All scripts must be exactly one line long
- All files must end with a newline
- Target machine: Cyber - WebSec 0x05

## Tools Used
- Burp Suite for intercepting and modifying upload requests
- Browser developer tools for analyzing client-side validation
- Hex editors for manipulating file content and magic numbers
- PHP scripts for testing and payload delivery

## Resources
- Comprehensive guides on file upload vulnerabilities
- Techniques for bypassing upload restrictions
- Understanding of Content-Type and Content-Disposition headers
- OWASP resources on secure file upload practices
- File upload protection cheat sheets and security checklists

## Setup
```bash
# Add the target domain to your hosts file
sudo bash -c "echo web0x05.hbtn >> /etc/hosts"

# Access the main domain
http://web0x05.hbtn
```
