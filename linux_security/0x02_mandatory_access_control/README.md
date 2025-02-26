# Mandatory Access Control

## Description
This project focuses on understanding and implementing Mandatory Access Control (MAC) systems in Linux, specifically SELinux and AppArmor. Through a series of tasks, students explore security policies, port management, user mappings, and security booleans.

## Learning Objectives
- Understand what MAC is in Linux
- Learn how SELinux enforces MAC
- Compare SELinux and AppArmor
- Work with policy in MAC systems
- Understand SELinux labels and enforcement types
- Manage SELinux status and configurations
- Set file contexts in SELinux
- Work with AppArmor profiles
- Apply the concept of least privilege in MAC
- Troubleshoot SELinux issues
- Use `semanage` for SELinux management

## Requirements
- All scripts run on Kali Linux 2023.2
- Allowed editors: vi, vim, emacs
- First line of all files must be `#!/bin/bash`
- All files should end with a new line
- All scripts must be exactly 2 lines long
- No use of printf, backticks, &&, || or ;
- Scripts should follow Betty style

## Tasks

### 0. SELinux Mode Analysis
Create a script that prints the current SELinux mode on your system.

### 1. AppArmor Status Check
Create a script that displays the status of AppArmor security profiles.

### 2. SELinux HTTP Ports
Create a script that lists all SELinux-managed ports related to HTTP services.

### 3. Adding SELinux TCP Port
Create a script that adds TCP port 81 as an http_port_t in SELinux.

### 4. SELinux User Mappings
Create a script that lists all SELinux user mappings.

### 5. Adding SELinux User Mapping
Create a script that adds a new login mapping in SELinux, linking a login name with the SELinux user identity user_u.

### 6. SELinux Booleans
Create a script that lists all SELinux booleans defined on the system.

### 7. Setting SELinux Boolean
Create a script that sets the SELinux boolean httpd_can_sendmail to on permanently.