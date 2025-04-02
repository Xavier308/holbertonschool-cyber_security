# SQL, noSQL Injection

## Description
This project provides hands-on experience with SQL and NoSQL injection vulnerabilities. You'll learn to identify, exploit, and understand the security implications of injection attacks in both SQL and NoSQL database environments.

## Learning Objectives
- Understand SQL and NoSQL injection vulnerabilities and their differences
- Identify vulnerable parameters in web applications
- Extract database information through SQL injection
- Perform blind SQL injection attacks
- Exploit second-order SQL injection vulnerabilities
- Discover and exploit NoSQL injection vulnerabilities
- Bypass authentication through NoSQL injection
- Understand parameterized queries and stored procedures
- Learn proper input validation techniques
- Implement effective prevention methods for injection attacks

## Tasks Overview
1. **Basic Injection Discovery**: Identify parameters vulnerable to SQL injection
2. **Database Information Extraction**: Extract database version and table information
3. **Data Exfiltration**: Extract sensitive data from specific database tables
4. **Time-Based Blind Injection**: Exploit blind SQL injection by observing response times
5. **Second-Order Blind Injection**: Craft payloads that activate during later processing
6. **NoSQL Injection Discovery**: Identify endpoints vulnerable to NoSQL injection
7. **NoSQL Authentication Bypass**: Exploit login forms to bypass authentication
8. **NoSQL Enumeration**: Leverage injection techniques to enumerate user profiles and perform actions

## Requirements
- Kali Linux environment
- All scripts must be exactly one line long
- All files must end with a newline
- Target machine: cyber_websec_0x01
- No use of sqlmap for this project

## Setup Instructions
```bash
# Edit your /etc/hosts file to include the target
sudo bash -c "echo web0x01.hbtn >> /etc/hosts"

# Access the target application
http://web0x01.hbtn/a3/sql_injection/
http://web0x01.hbtn/a3/nosql_injection/
```

## Resources
- SQL vs. NoSQL database differences
- Understanding SQL and NoSQL injection techniques
- Comprehensive guides to injection vulnerabilities
- OWASP SQL Injection Prevention Cheat Sheet
- MITRE Common Weakness Enumeration (CWE) resources
- Prevention strategies including parameterized queries and ORMs
