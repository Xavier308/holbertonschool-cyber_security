#!/bin/bash
find "$1" -perm -u=s -type f -ls 2>/dev/null
