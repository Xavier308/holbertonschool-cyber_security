#!/bin/bash

# This script identifies the most frequently used authentication service by attackers
# Analyzes pam_unix entries in auth.log to determine attack patterns
LOG_FILE="auth.log"

# Check if log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found!"
    exit 1
fi

# Extract service names from pam_unix log entries, count occurrences
# and display the most frequently used service (likely the attack vector)
grep "pam_unix" "$LOG_FILE" | \
    grep -oP 'pam_unix\(\K[^:]+' | \
    sort | uniq -c | sort -nr | \
    head -n 1 | awk '{print $2}'
