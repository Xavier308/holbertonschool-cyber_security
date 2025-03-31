#!/bin/bash
grep -Eo 'POST [^ ]|GET [^ ]+' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $3}'