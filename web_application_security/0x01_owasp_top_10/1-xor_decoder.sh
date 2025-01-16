#!/bin/bash

# Verify RGUMENT
if [ $# -ne 1 ]; then
    echo "Usage: $0 {xor}base64_string"
    exit 1
fi

#  Extract code
encoded=${1#"{xor}"}

# Decode base64
echo "$encoded" | base64 -d | perl -pe 's/(.)/chr(ord($1) ^ 0x5F)/ge'
