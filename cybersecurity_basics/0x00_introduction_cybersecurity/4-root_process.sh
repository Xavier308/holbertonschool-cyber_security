#!/bin/bash
ps aux | grep "^$1" | grep -vE ' 0\s+0 '
