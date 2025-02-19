#!/bin/bash
find "$1" (-perm /4000 -o -perm /2000) -mtime -1 -type f 2>/dev/null -exec ls -l {} \;
