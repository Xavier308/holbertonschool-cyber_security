#!/bin/bash
find "$1" -type f -exec chmod o=r {} \;
