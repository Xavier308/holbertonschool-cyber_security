# Web Fundamentals

## Description
This project introduces foundational web application security concepts and provides hands-on experience with common web vulnerabilities. Through a series of practical exercises, you'll learn how to identify and exploit security issues in web applications.

## Learning Objectives
- Understand how the web works fundamentally
- Differentiate between Web 1.0, Web 2.0, and Web 3.0
- Learn about Progressive Web Applications (PWA)
- Understand front-end and back-end communication
- Explore stateful vs. stateless applications
- Differentiate between structured and unstructured data
- Identify common web application security risks
- Learn about bug bounty programs

## Tasks Overview
1. **Host Header Injection**: Exploit vulnerabilities in HTTP host headers
2. **Password Reset Exploitation**: Capture flags by exploiting a password reset feature
3. **Cross-Site Scripting (XSS)**: Create JavaScript payloads to steal cookies
4. **SQL Injection**: Exploit database vulnerabilities to access unauthorized data
5. **Remote Code Execution (RCE)**: Execute commands on a target server through input validation flaws

## Requirements
- Kali Linux 2023.3
- Scripts must be exactly two lines long
- Scripts should substitute the IP range with $1
- All files must end with a newline
- First line of all files must be #!/bin/bash
- Files must follow Betty coding style
- All files must be executable

## Tools Used
- curl
- SQLmap
- Python's HTTP server
- Firefox web browser

## Installation
```bash
# Install curl
sudo apt install curl

# Install SQLmap
sudo apt install sqlmap
```

## Resources
- How the Web works
- Web Development Fundamentals
- Web 1.0 vs. Web 2.0 vs. Web 3.0
- Progressive Web Apps
- Stateful vs Stateless Web App Design
- Structured vs. Unstructured Data
- Web Application Security
- OWASP Top Ten
- Cross-Origin Resource Sharing (CORS)
- Bug Bounty Programs
