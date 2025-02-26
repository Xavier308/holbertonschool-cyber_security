# Protocols and Servers

## Description
This project focuses on understanding and securing various network protocols and server configurations. Students will learn about network security, vulnerability assessment, and hardening techniques for different protocols including NFS, SMTP, SNMP, SMB, LDAP, and more.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the purpose of the NFS protocol
- Explain how SMTP works for email transmission
- Identify information provided by SNMP about network devices
- Understand how SMB enables file sharing across operating systems
- Explain LDAP's role in authentication and authorization
- Recognize security risks associated with RDP
- Differentiate between secure protocols (HTTPS, SFTP) and their insecure counterparts
- Understand the benefits of SSH for secure remote access
- Explain port numbers and their importance in network communication
- Identify different types of network encryption protocols
- Recognize the importance of keeping network protocols updated and patched

## Requirements
- All scripts run on Kali Linux 2023.2
- Allowed editors: vi, vim, emacs
- First line of all files must be `#!/bin/bash`
- All files should end with a new line
- All scripts should be 2 lines long (except where specified)
- Code should use Betty style

## Tasks

### 0. Analyze iptables Rules
Create a script to display all current iptables rules in a readable format with line numbers.

### 1. Audit SSH Configuration
Create a script to check and report non-standard SSH configuration settings in `/etc/ssh/sshd_config`.

### 2. Harden Linux Server
Create a script to list all world-writable directories and secure their permissions.

### 3. Identify Common Vulnerabilities
Create a script to check for unpatched common vulnerabilities using the Lynis audit tool.

### 4. Check for NFS Vulnerabilities
Create a script to scan for NFS shares that are accessible by anyone on the network.

### 5. Audit SNMP Configuration
Create a script to find SNMP configurations that allow public access.

### 6. Examine SMTP Server Settings
Create a script to check SMTP server configuration for security features like STARTTLS.

### 7. Simulate DoS Attack on HTTP Server
Create a script to simulate a basic Denial of Service attack on an HTTP server using hping3.

### 8. Check for Weak SSL/TLS Ciphers
Create a script to test an SSL/TLS server's ciphers and report any weak ciphers using nmap.

### 9. Implement Basic Firewall Rules
Create a script to set up basic iptables firewall rules that block all incoming traffic except SSH (3 lines).