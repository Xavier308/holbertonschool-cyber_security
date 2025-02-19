#!/bin/bash
find "$1" -type f -empty -exec chmod 777 {} \;
