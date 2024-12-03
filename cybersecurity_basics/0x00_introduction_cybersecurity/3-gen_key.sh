#!/bin/bash
ssh-keygen -t rsa -b 4096 -f $1 -q -N ""
