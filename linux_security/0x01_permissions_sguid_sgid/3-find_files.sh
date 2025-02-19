#!/bin/bash
find "$1" -perm -u=s -type f 2>/dev/null -exec ls -l {} \;
