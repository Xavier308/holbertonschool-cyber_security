#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 '{xor}<base64_string>'"
    exit 1
fi

# Remove the "{xor}" prefix and decode from base64
encoded="${1#'{xor}'}"
decoded=$(echo "$encoded" | base64 --decode 2>/dev/null)

# Check if decoding was successful
if [ $? -ne 0 ]; then
    echo "Error decoding base64."
    exit 2
fi

# Initialize output variable
output=""

# XOR each character with 95
for (( i=0; i<${#decoded}; i++ )); do
    # Get ASCII value of character
    ord=$(printf "%d" "'${decoded:$i:1}")
    # Perform XOR with 95 and convert back to character
    xored_char=$(printf \\$(printf "%o" $((ord ^ 95))))
    output+="$xored_char"
done

# Output the result
echo "$output"
