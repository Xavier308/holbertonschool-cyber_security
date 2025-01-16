#!/bin/bash

# Check for the correct number of arguments
if [ $# -ne 1 ]; then
    echo "Usage: $0 '{xor}<base64_string>'"
    exit 1
fi

# Remove the '{xor}' prefix if present and decode the base64 string
decoded=$(echo "${1#'{xor}'}" | base64 --decode | tr -d '\000')

# Initialize an empty output variable
output=""

# Perform XOR on each byte, now that null bytes have been removed
for (( i=0; i<${#decoded}; i++ )); do
    # XOR each byte with 95 and convert it back to a character
    char=$(printf "%d" "'${decoded:$i:1}")
    xored_char=$((char ^ 95))
    output+=$(printf "\\x$(printf "%x" "$xored_char")")
done

# Print the output without a newline character
echo -n "$output"
