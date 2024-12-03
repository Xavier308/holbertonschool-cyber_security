#!/bin/bash
echo "$2  $1" | sha256sum -c - && echo "$1: OK" || echo "$1: FAIL"
