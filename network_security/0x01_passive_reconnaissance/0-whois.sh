#!/bin/bash
whois "$1" | awk -F': ' '
/^Registrant|^Admin|^Tech/ {
    sub(/^ +/, "", $1); sub(/^ +/, "", $2); sub(/ +$/, "", $2);  # Trimming white spaces
    if ($1 ~ /Name|Organization|Street|City|State\/Province|Postal Code|Country|Phone|Email/) {
        label = $1;
        sub(/Registrant |Admin |Tech /, "", label);
        print label "," $2
    }
}' OFS=',' > "$1.csv"
