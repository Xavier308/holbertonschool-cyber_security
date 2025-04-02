# OWASP Top 10

## Description
This project provides hands-on experience with the OWASP Top 10 web application security risks. Through practical exercises, you'll learn to identify, exploit, and mitigate common security vulnerabilities in web applications.

## Learning Objectives
- Understand the OWASP Top 10 security risks and their implications
- Learn how to identify and exploit injection vulnerabilities
- Recognize Cross-Site Scripting (XSS) attacks and their impact
- Understand broken authentication risks and mitigations
- Identify sensitive data exposure scenarios
- Detect and remediate security misconfigurations
- Learn about XML External Entity (XXE) attacks
- Understand broken access control vulnerabilities
- Recognize insecure deserialization issues
- Implement proper security logging and monitoring
- Identify risks of using components with known vulnerabilities
- Understand API security best practices

## Tasks Overview
1. **Broken Access Control (A1:2021)**: Exploit session handling vulnerabilities
2. **Cryptographic Failures (A2:2021)**: Decode XOR encryption and exploit weak cryptography
3. **Injection - Stored XSS (A3:2021)**: Multi-part challenge simulating the Samy worm attack
   - Identifying and following specific profiles
   - Discovering vulnerable input fields
   - Creating and deploying XSS payloads

## Requirements
- Kali Linux 2023.2
- Allowed editors: vi, vim, emacs
- All scripts must substitute IP range with $1
- First line of all files must be exactly #!/bin/bash
- All files must end with a newline
- No use of backticks, &&, || or ;
- Code must follow Betty style

## Target Environment
- Machine: Cyber - WebSec 0x01
- Setup:
  ```bash
  sudo bash -c "echo web0x01.hbtn >> /etc/hosts"
  ```

## Resources
- [OWASP Top 10:2021](https://owasp.org/Top10/)
- OWASP Top 10 explanations and examples
- Mitigation strategies for OWASP risks
- Password security best practices
- OWASP tools:
  - ZAP (Web Application Penetration Testing)
  - Amass (Subdomain Enumeration)
  - Juice Shop (Vulnerable Web Application)
  - Dependency-Check (Software Composition Analysis)

