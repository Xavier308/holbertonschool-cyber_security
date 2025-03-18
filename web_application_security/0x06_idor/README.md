# Insecure Direct Object Reference (IDOR)

This project explores IDOR vulnerabilities through a simulated banking application called CyberBank. By understanding and exploiting these vulnerabilities, security professionals can better identify and protect against them in real-world applications.

## Overview

IDOR vulnerabilities occur when applications expose direct references to internal objects without proper access controls. The project consists of tasks that progressively demonstrate the potential impact of IDOR in financial applications:

- **Uncovering User IDs**: Identifying how user information is exposed
- **Enumerating Account Numbers**: Using discovered user IDs to access account information
- **Manipulating Wire Transfers**: Exploiting transaction functionality to inflate account balances
- **Bypassing 3D Secure Verification**: Redirecting payment verification to unauthorized accounts
- **Vulnerability Reporting**: Creating a comprehensive security assessment report

## Requirements

- All scripts must be exactly one line long
- Testing will be performed on Kali Linux
- Focus is on the target Cyber - WebSec 0x06

## Target Application

- CyberBank simulation environment
- Various endpoints including `/dashboard`, `/upgrade`, and `/confirmation`

## Learning Objectives

Upon completion of this project, you should be able to explain:

- What IDOR vulnerabilities are and how they work
- Different types of IDOR vulnerabilities
- The potential impact of IDOR on application security
- Methods to detect IDOR vulnerabilities
- Best practices for preventing IDOR attacks
- Effective techniques for reporting security issues

## Resources

- OWASP documentation on IDOR
- Various articles and guides on identification and exploitation of IDOR vulnerabilities
- IDOR mitigation best practices

## Important Note
- All activities in this project are for educational purposes only.