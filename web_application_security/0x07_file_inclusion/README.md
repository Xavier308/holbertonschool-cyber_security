# File Inclusion

## Description
This project explores file inclusion vulnerabilities in web applications. Through practical exercises, you'll learn to identify, exploit, and understand both Local File Inclusion (LFI) and Remote File Inclusion (RFI) vulnerabilities, as well as techniques to escalate these vulnerabilities to achieve remote code execution.

## Learning Objectives
- Understand what Local File Inclusion (LFI) and Remote File Inclusion (RFI) are
- Learn how directory traversal attacks work using `../` sequences
- Discover how file inclusion vulnerabilities can lead to Remote Code Execution (RCE)
- Explore various exploitation techniques for file inclusion vulnerabilities
- Understand the security impact of successful file inclusion attacks
- Learn detection methods for identifying file inclusion vulnerabilities
- Master mitigation strategies to protect applications from file inclusion attacks

## Tasks Overview
1. **File Hub**: Identify vulnerable endpoints and access hidden flag files
2. **Filter Bypass**: Exploit path traversal vulnerabilities by navigating around filters
3. **Advanced Filter Bypass**: Challenge multiple layers of filtering and validation
4. **Template Injection**: Exploit Jinja template vulnerabilities for file access
5. **Log Poisoning**: Leverage log files to achieve shell access for flag capture

## Requirements
- Kali Linux environment
- All scripts must be exactly one line long
- All files must end with a newline
- Target machine: Cyber - WebSec 0x07

## Tools Used
- Web browsers for testing vulnerabilities
- Burp Suite for intercepting and modifying requests
- URL encoding tools for bypassing filters
- Shell scripts for automating exploitation

## Resources
- OWASP guides on Local File Inclusion (LFI) and Remote File Inclusion (RFI)
- File inclusion exploitation guides
- Path traversal techniques
- PHP documentation on include() and require() functions
- File inclusion cheat sheets and payload collections

## Setup
```bash
# Add the target domain to your hosts file
sudo bash -c "echo web0x07.hbtn >> /etc/hosts"

# Access the main domain
http://web0x07.hbtn
```
