#!/bin/bash
curl -X POST $2 -H "Host: $1" -d $3
