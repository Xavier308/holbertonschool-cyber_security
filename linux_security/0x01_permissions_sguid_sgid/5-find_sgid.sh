#!/bin/bash
find "$1" -perm -g=s -type f 2>/dev/null
