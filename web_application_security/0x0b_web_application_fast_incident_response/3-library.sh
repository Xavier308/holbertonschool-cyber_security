#!/bin/bash
grep "^$(awk '{print $1}' ${1:-logs.txt} | sort | uniq -c | sort -nr | head -n1 | awk '{print $2}')" ${1:-logs.txt} | awk -F\" '{print $6}' | sort | uniq -c | sort -nr | head -n1 | awk '{$1=""; print $0}' | sed 's/^ //'