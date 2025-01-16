#!/bin/bash

# Capture the first argument passed to the script
password="$1"

# Remove the '{xor}' prefix from the string
password="${password#'{xor}'}"

# Decode the string from Base64 using OpenSSL
decoded_password=$(echo -n "$password" | openssl enc -base64 -d)

# Initialize a variable to store the XOR operation result
output=""

# Iterate over each character of the decoded string
for ((i = 0; i < ${#decoded_password}; i++)); do
    # Retrieve the character at the current position
    char="${decoded_password:$i:1}"
    # Convert the character to its ASCII code and
    # perform an XOR operation with 95
    xor_result=$(( $(printf "%d" "'$char") ^ 95 ))
    # Append the result to the output variable
    output+=$(printf "\\$(printf '%03o' $xor_result)")
done

# Display the result
echo "$output"
