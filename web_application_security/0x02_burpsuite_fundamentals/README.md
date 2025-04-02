# BurpSuite Fundamentals

## Description
This project provides hands-on experience with BurpSuite, an essential web application security testing tool. Through a series of practical exercises, you'll learn to configure and use different BurpSuite components to intercept, analyze, and manipulate web traffic to discover security vulnerabilities.

## Learning Objectives
- Understand what BurpSuite is and its role in web application security testing
- Configure proxy settings in BurpSuite to intercept web traffic
- Work with BurpSuite's main components and their functions
- Use the Spider tool to crawl web applications
- Apply the Repeater tool to modify and resend requests
- Utilize the Intruder tool for automated attack testing
- Implement the Scanner to identify security issues
- Interpret results from BurpSuite scans
- Configure BurpSuite for HTTPS traffic interception
- Recognize common web application vulnerabilities

## Tasks Overview
1. **Getting Started**: Configure BurpSuite proxy and discover hidden data in TLS certificates
2. **Client-Side TLS Authentication**: Install and configure client certificates for authentication
3. **Response Modification**: Intercept and modify web page responses to reveal hidden information
4. **Repeater Tool**: Use Repeater to test login credentials on a simulated router portal
5. **Intruder Tool**: Automate attacks to discover hidden user profiles
6. **Sequencer**: Analyze and exploit patterns in session tokens
7. **Decoder**: Manipulate Base64 encoded Bearer tokens to escalate privileges

## Requirements
- Kali Linux environment
- All scripts must be exactly one line long
- All files must end with a newline
- Target website: https://web0x02.hbtn

## Installation
BurpSuite Community Edition is pre-installed on Kali Linux. If needed, you can download it from the [official PortSwigger website](https://portswigger.net/burp/communitydownload).

## Resources
- Burp Suite Tutorials for beginners
- Getting Started guides
- OWASP Top Ten testing with Burp Suite
- Official Burp Suite Documentation
- Web vulnerability scanning with Burp Suite

## Setting Up Environment
- Configure browser proxy settings to use BurpSuite (typically 127.0.0.1:8080)
- Install BurpSuite's CA certificate in your browser
- Configure hostname resolution for web0x02.hbtn target

