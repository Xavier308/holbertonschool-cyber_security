# Windows Privilege Escalation - Task 0

## Objective
Extract sensitive data from unattended installation files to gain administrative access and retrieve the target flag from LAB01 VM.

## Target Information
- **Virtual Machine**: LAB01
- **Student Account Password**: Student
- **Goal**: Extract administrator credentials and retrieve flag from admin desktop

## Technique Overview

### Unattended Installation Files
Unattended installation files are automated setup configurations that can contain sensitive information including:
- Administrator passwords
- Service account credentials
- Domain join credentials
- Auto-logon passwords

### Common File Locations
The script searches these typical locations:
- `C:\Windows\Panther\Unattend.xml`
- `C:\Windows\Panther\Unattended.xml`
- `C:\Windows\system32\sysprep\sysprep.inf`
- `C:\Windows\system32\sysprep\sysprep.xml`
- `C:\unattend.xml`
- `C:\autounattend.xml`

## Script Functionality

### 1. File Discovery
- Scans common locations for unattended installation files
- Checks file existence and accessibility
- Reports found files for analysis

### 2. Password Extraction
Uses regular expressions to identify password patterns:
```regex
<AdministratorPassword>\s*<Value>(.*?)</Value>
<Password>\s*<Value>(.*?)</Value>
<PlainText>false</PlainText>\s*<Value>(.*?)</Value>
AdminPassword\s*=\s*[\"'](.*?)[\"']
```

### 3. Password Decoding
- Attempts Base64 decoding for encoded passwords
- Handles UTF-16 LE encoding (common in Windows)
- Falls back to plaintext if decoding fails

### 4. Administrative Session
- Uses `runas` command to establish elevated session
- Tests multiple common administrator account names
- Executes commands with elevated privileges

### 5. Flag Retrieval
- Searches administrator desktop locations
- Reads and extracts flag content
- Saves flag to required output file

## Usage Instructions

### Prerequisites
- Python 3.x installed
- Access to target Windows system (LAB01)
- Student account credentials

### Execution Steps
1. Copy the script to the target system
2. Open Command Prompt or PowerShell
3. Navigate to script directory
4. Execute the script:
   ```bash
   python extract_password.py
   ```

### Expected Output
```
============================================================
Windows Privilege Escalation - Unattended File Extractor
============================================================
[+] Scanning for unattended installation files...
[+] Found file: C:\Windows\Panther\Unattend.xml
[+] Analyzing file: C:\Windows\Panther\Unattend.xml
[+] Found encoded password: [encoded_string]
[+] Decoded password: [admin_password]
[+] Attempting to establish admin session with user: Administrator
[+] Admin session established successfully!
[+] Searching for flag in Administrator desktop...
[+] FLAG FOUND: [flag_content]
[+] Flag saved to 0-flag.txt
[+] Privilege escalation completed successfully!
```

## Security Implications

### Vulnerability Analysis
- **Risk Level**: High
- **Impact**: Complete system compromise
- **Attack Vector**: Local file access

### Why This Works
1. **Weak File Permissions**: Unattended files often have readable permissions for standard users
2. **Credential Storage**: Passwords stored in plaintext or weakly encoded
3. **Persistent Access**: Files remain on system after installation

## Mitigation Strategies

### For System Administrators
1. **Remove Unattended Files**: Delete installation files after deployment
2. **Secure File Permissions**: Restrict access to sensitive configuration files
3. **Encrypt Credentials**: Use proper encryption for stored passwords
4. **Regular Audits**: Scan for leftover installation artifacts

### Best Practices
- Use temporary passwords that expire after first login
- Implement least privilege access controls
- Monitor file system access logs
- Regular security assessments

## Ethical Considerations
- This script is for educational and authorized testing purposes only
- Ensure proper authorization before testing on any system
- Follow responsible disclosure practices
- Respect privacy and legal boundaries

## File Structure
```
windows_privsec/
├── extract_password.py    # Main extraction script
├── 0-flag.txt            # Retrieved flag output
└── README.md             # This documentation
```

## Dependencies
- Python 3.x standard library
- Windows operating system
- Appropriate file system permissions

