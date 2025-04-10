#!/bin/bash
grep -iE "iptables" auth.log | grep "A INPUT" | sort -u | wc -l