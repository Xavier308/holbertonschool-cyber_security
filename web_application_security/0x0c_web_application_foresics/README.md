# Web Application Forensics

## Description
This project focuses on analyzing web application logs to identify security breaches, trace attacks, and develop protective strategies. By examining log files, we can gather crucial information about attackers, compromised accounts, and system vulnerabilities.

## Learning Objectives
* Understand core concepts of Digital Forensics and Web Application Forensics
* Analyze Web Application Logs to identify attack patterns
* Use Log Files and Access Logs to trace attack origins
* Implement tools like Wireshark and Burp Suite for forensic investigations
* Follow Legal Frameworks and best practices for forensic investigations

## Requirements
* All scripts must be written for Kali Linux
* All files should end with a new line
* First line must be `#!/bin/bash`
* No backticks, &&, ||, or ; allowed
* All files must be executable
* Use `$1` without quotes in scripts

## Tasks
1. **Attacker Service**: Identify which service attackers used to gain access to the system
2. **Operating System**: Determine the operating system version of the targeted system
3. **Account Compromised**: Find the name of the compromised account
4. **Sum Attack**: Count how many distinct attackers gained access to the system
5. **Mitigation Firewalls**: Analyze how many rules were added to the firewall
6. **User Accounts**: Identify multiple accounts created on the target system
7. **Future Mitigations**: Create a comprehensive incident report with mitigation strategies

## Files Used
* `auth.log`: Authentication logs containing login attempts and session information
* `dmesg`: System boot and kernel messages

## Usage
Scripts analyze provided log files:
```bash
./script_name.sh
```

## Files
* `0-service.sh`: Scans logs to determine the service used by attackers
* `1-operating.sh`: Identifies the operating system version
* `2-accounts.sh`: Finds the compromised account by analyzing login patterns
* `3-ips.sh`: Counts distinct attackers based on unique IP addresses
* `4-firewall.sh`: Determines how many firewall rules were added
* `5-users.sh`: Lists user accounts created on the target system