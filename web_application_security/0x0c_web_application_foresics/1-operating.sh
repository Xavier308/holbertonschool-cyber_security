#!/bin/bash

# This script extracts the target system's Linux kernel version information
# Searches for the first occurrence of "Linux version" in the dmesg log
grep -m 1 "Linux version" dmesg