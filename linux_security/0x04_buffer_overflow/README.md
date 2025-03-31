# Buffer Overflow Project

A practical exploration of buffer overflow concepts and memory manipulation in Linux systems.

## Description

This project demonstrates how to safely interact with a running process's memory using the `/proc` filesystem in Linux. The main task involves creating a Python script that can find and replace strings in the heap of a running process.

## Requirements

- Ubuntu 14.04 LTS
- Python 3 (version 3.4.3)
- Basic understanding of memory management and process structure

## Files

- `read_write_heap.py`: Python script to find and replace a string in a process's heap
- `main.c`: A sample C program that allocates a string on the heap for testing purposes

## Usage

1. Compile and run the test program:
   ```
   gcc -Wall -pedantic -Werror -Wextra main.c -o main
   ./main
   ```

2. In another terminal, find the PID of the running program:
   ```
   ps aux | grep ./main
   ```

3. Use the script to modify the string in memory:
   ```
   sudo python3 ./read_write_heap.py <PID> <search_string> <replace_string>
   ```
   Example:
   ```
   sudo python3 ./read_write_heap.py 6515 Holberton "Xavier"
   ```

## How It Works

The script:
1. Opens the memory map of the process via `/proc/<PID>/maps`
2. Locates the heap section in the memory map
3. Opens the process memory via `/proc/<PID>/mem`
4. Searches for the target string within the heap memory region
5. Replaces the string with the new string if found

## Learning Objectives

Through this project, you'll understand:
- What buffers are and how they're managed in memory
- How buffer overflow vulnerabilities occur
- How processes store data in memory
- How to safely manipulate process memory
- The principles behind buffer overflow attacks

## Security Note

This project is for educational purposes only. The techniques demonstrated should only be used on systems and processes you own or have permission to modify.