#!/bin/bash
sudo nmap -sU -sV -p200-300 -T4 --reason -v $1
