# Nmap Advanced Port Scans

This project explores various advanced port scanning techniques using the powerful Nmap network scanning tool. By understanding and implementing these different scan types, security professionals can better identify network vulnerabilities and strengthen their defenses.

## Overview

The repository contains scripts implementing various Nmap scan techniques:

- **NULL Scan**: Uses empty TCP packets to detect open ports stealthily
- **FIN Scan**: Sends TCP packets with only the FIN flag set to bypass basic firewalls
- **Xmas Scan**: Utilizes packets with FIN, PSH, and URG flags for stealthy detection
- **Maimon Scan**: Employs TCP packets with both FIN and ACK flags
- **ACK Scan**: Determines firewall filtering rules by analyzing responses to ACK packets
- **Window Scan**: Analyzes TCP window size in RST packets to infer port status
- **Custom Scan**: Creates non-standard packets to probe for specific vulnerabilities

## Requirements

- Scripts are written for Kali Linux
- All scripts must be exactly 2 lines long
- Scripts must accept IP ranges/hosts as arguments
- All scripts require sudo permissions

## Usage

Each script accepts a host/IP as the first argument, with additional parameters for specific scan types:

```bash
sudo ./0-null_scan.sh example.com
sudo ./4-ask_scan.sh example.com 80,22,25
sudo ./5-window_scan.sh example.com 20-30 25-28
```

## Learning Objectives

- Understanding different advanced port scanning techniques
- Analyzing network security from an offensive perspective
- Identifying firewall configurations and potential vulnerabilities
- Implementing stealthy reconnaissance methods
