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
    ord=$(printf "%d" "'${decoded:$i:1}")
    # Perform XOR with 95 and convert back to character
    xored_char=$(printf \\$(printf "%o" $((ord ^ 95))))
    # Append only if it's not a null character
    if [[ $xored_char != $'\0' ]]; then
        output+="$xored_char"
    fi
done

# Output the result
echo -n "$output"
