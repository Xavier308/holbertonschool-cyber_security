# Acces Presistence Techniques


## Description
This project explores various Windows persistence techniques used by attackers to maintain long-term access to compromised systems. Through hands-on labs, we analyze and implement different persistence methods to understand their impact and detection mechanisms.

## Learning Objectives
- Understand Windows persistence and its importance in cybersecurity
- Learn different techniques to establish persistence on Windows systems
- Explore Startup folder, registry keys, scheduled tasks, and services manipulation
- Understand risks of DLL hijacking and WMI abuse
- Learn to leverage BITS jobs for malicious payload delivery

## Environment
- **VM Platform**: VMware Workstation
- **Target OS**: Windows
- **Credentials**:
  - Student account: `Student`
  - SuperAdministrator account: `Root@123`

## Tasks Overview

### Task 0: Persistence Using Startup Folder
Explore how attackers use Windows Startup folders to achieve persistence by placing malicious files that execute automatically on user login.

### Task 1: Persistence Using Registry Autorun
Learn registry manipulation techniques to configure programs for automatic execution through HKEY_CURRENT_USER and HKEY_LOCAL_MACHINE registry keys.

### Task 2: Persistence Using Services
Investigate how Windows Services can be exploited to run malicious programs in the background with system-level privileges.

### Task 3: Persistence Using Scheduled Tasks
Understand how attackers abuse Windows Task Scheduler to establish persistent access through time-based and event-based triggers.

### Task 4: Persistence Using BITSAdmin
Explore Background Intelligent Transfer Service (BITS) abuse for stealthy payload download and execution with built-in persistence capabilities.
