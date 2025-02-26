#!/bin/bash
find / -xdev -type d -perm -0002 ! -path "/proc/*" -print -exec chmod o-w {} +