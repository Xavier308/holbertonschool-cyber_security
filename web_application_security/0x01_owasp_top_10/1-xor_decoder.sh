#!/bin/bash

# Check if exactly one argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 '{xor}<base64_string>'"
    exit 1
fi

# Remove the '{xor}' prefix and decode from base64, remove null bytes immediately
encoded="${1#'{xor}'}"
decoded=$(echo "$encoded" | base64 --decode | tr -d '\000')

# Verify successful decoding
if [ $? -ne 0 ]; then
    echo "Error decoding base64."
    exit 2
fi

# Initialize an output variable
output=""

# XOR each character with 95
for (( i=0; i<${#decoded}; i++ )); do
    ord=$(printf "%d" "'${decoded:$i:1}")
    xor_result=$((ord ^ 95))
    # Convert the XOR result back to ASCII and append to output
    if [ $xor_result -ne 0 ]; then  # Check to ensure not to add null bytes
        output+=$(printf "\\$(printf '%03o' $xor_result)")
    fi
done

# Output the result without a newline
echo -n "$output"
