# Wireshark Basics

## Description
This project covers fundamental concepts of network packet analysis using Wireshark. Wireshark is a powerful network protocol analyzer that allows users to examine network traffic and troubleshoot network issues.

## Learning Objectives
- Understand what Wireshark is and its primary functions
- Learn how to use Wireshark filters effectively
- Analyze network packets with Wireshark
- Detect various network scanning techniques

## Tasks
The project includes creating Wireshark filters to detect:
1. IP protocol scanning
2. TCP SYN scanning
3. TCP Connect() scanning
4. TCP FIN scanning
5. TCP ping sweeps
6. UDP port scanning
7. UDP ping sweeps
8. ICMP ping sweeps
9. ARP scanning

## Requirements
- All filters should be written in text file format
- All files must end with a new line
- Testing environment: Kali Linux

## Installation
If Wireshark is not already installed:
```
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
sudo usermod -aG wireshark $USER
```

## Usage
To start Wireshark:
```
wireshark
```

## Resources
- TCP/IP Packet Formats and Ports
- Wireshark Filters
- Working With Captured Packets
- Examining captured packets using Wireshark
