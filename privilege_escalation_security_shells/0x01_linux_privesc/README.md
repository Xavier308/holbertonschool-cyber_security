# Linux Privilege Escalation - 0x01_linux_privesc

This directory contains solutions and documentation for Linux privilege escalation challenges focused on practical exploitation techniques commonly found in real-world environments.

### Learning Objectives

Master fundamental privilege escalation techniques including:
- **SUID/SGID Executables**: Identify and exploit misconfigured binaries
- **Cron Job Misconfiguration**: Exploit writable scripts executed with elevated privileges  
- **Buffer Overflow Exploitation**: Custom SUID binary analysis and exploitation
- **sudo Privilege Abuse**: Leverage specific sudo permissions for escalation

## Tasks Completed

### Task 0: Flag File Privilege Escalation
- **Target**: `cyber shell 0x02 linux privesc task1`
- **Technique**: sudo privilege abuse with `choom` command
- **Flag Location**: `/root/flag.txt`
- **Output**: `0-flag.txt`

### Task 1: Cron Job Misconfiguration
- **Target**: `cyber shell 0x02 linux privesc task2`
- **Technique**: Wildcard injection in tar command via cron job
- **Vulnerability**: Misconfigured backup script with user-writable directory
- **Output**: `1-flag.txt`

### Task 2: SUID Binary Buffer Overflow
- **Target**: `cyber shell 0x02 linux privesc task3`  
- **Technique**: Buffer overflow + string comparison bypass
- **Binary**: `/home/user/service` (custom SUID binary)
- **Exploit**: Memory corruption to bypass `strcmp()` validation
- **Output**: `2-flag.txt`

## Tools & Resources Used

- **LinPEAS**: Automated privilege escalation enumeration
- **GTFOBins**: SUID/sudo exploitation techniques
- **GDB**: Binary analysis and debugging
- **objdump**: Static binary analysis
- **Custom Scripts**: Payload generation and exploitation

## Quick Reference Commands

### SUID Binary Enumeration
```bash
find / -perm -4000 -type f 2>/dev/null
```

### Cron Job Analysis  
```bash
cat /etc/crontab
ls -la /etc/cron.d/
```

### sudo Permission Check
```bash
sudo -l
```

## Security Implications

These exercises demonstrate critical security weaknesses:

1. **Improper sudo Configuration**: Overly permissive sudo rules
2. **Insecure Cron Jobs**: Scripts with wildcards in user-writable directories
3. **Vulnerable Custom Binaries**: Buffer overflows in SUID programs
4. **Inadequate Input Validation**: Memory corruption leading to privilege escalation


## Connection Information

```bash
ssh user@CONTAINER_IP
# password: user
```
