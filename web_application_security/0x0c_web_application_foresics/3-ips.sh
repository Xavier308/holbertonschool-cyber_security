#!/bin/bash 
grep "Accepted password for root" auth.log | grep -Eo '[0-9]{1,3}(\.[0-9]{1,3}){3}' | sort -u | wc -l