# Command Injection

## Description
This project focuses on command injection vulnerabilities, including the infamous CVE-2021-44228 (Log4Shell). Through a series of practical exercises, you'll learn to identify, exploit, and mitigate command injection vulnerabilities in web applications, gaining hands-on experience with various bypass techniques and understanding their security implications.

## Learning Objectives
- Understand what command injection is and how it works
- Learn common payloads used for command injection attacks
- Identify typical attack vectors for command injection vulnerabilities
- Understand Bash special variables and their role in exploitation
- Learn the differences between command operators (`&&`, `;`, etc.) in Bash
- Understand the Internal Field Separator (IFS) in Bash scripting
- Discover techniques to manipulate IFS for command execution
- Explore hacker tricks for exploiting command injection vulnerabilities
- Assess the potential impact of successful command injection attacks
- Learn security measures to protect applications against command injection

## Tasks Overview
1. **Basic Command Injection**: Exploit a vulnerable ping tool to execute commands
2. **Filter Bypass**: Overcome basic security measures using advanced injection techniques
3. **Environment Variable Exploitation**: Use environment variables to bypass filters and access restricted files
4. **Blind Command Injection**: Perform blind command injection using DNS exfiltration techniques
5. **Tool Integration Vulnerabilities**: Exploit command injection in integrated tools like nmap

## Requirements
- Kali Linux environment
- All scripts must be exactly two lines long
- Scripts should substitute the IP range with $1
- All files must end with a newline
- Target application: Various web0x09.hbtn endpoints

## Tools Used
- Web browsers for accessing the vulnerable applications
- Burp Suite for intercepting and modifying requests
- Interactsh for receiving DNS exfiltration data
- Basic command-line tools (ping, nmap, etc.)

## Resources
- Command injection overview and techniques
- BashGuide for understanding Bash scripting
- Payload collections for command injection
- Bash special variables documentation
- IFS manipulation techniques
- Prevention strategies for command injection vulnerabilities

## Setup
```bash
# Add the target domains to your hosts file
sudo bash -c "echo web0x09.hbtn-task0 >> /etc/hosts"
sudo bash -c "echo web0x09.hbtn-task1 >> /etc/hosts"
sudo bash -c "echo web0x09.hbtn-task2 >> /etc/hosts"
sudo bash -c "echo web0x09.hbtn >> /etc/hosts"

# Access the applications
http://web0x09.hbtn-task0/
http://web0x09.hbtn-task1/
http://web0x09.hbtn-task2/
http://web0x09.hbtn/app4/
http://web0x09.hbtn/app5/
```
