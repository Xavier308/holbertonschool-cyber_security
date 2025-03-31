#!/usr/bin/env python3
"""
Replace a string in the heap memory of a running process.
"""

import os
import sys
import re


def usage():
    """Print usage and exit."""
    print("Usage: ./read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def read_write_heap(pid, search_string, replace_string):
    """Search and replace a string in process heap."""
    try:
        # Validate PID
        pid = int(pid)
    except ValueError:
        print("Error: PID must be an integer.")
        usage()

    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        # Find heap segment
        with open(maps_path, "r") as maps_file:
            heap = None
            for line in maps_file:
                if "[heap]" in line:
                    heap = line
                    break

            if not heap:
                print("Error: Could not find the heap segment.")
                sys.exit(1)

            # Get heap start and end
            heap_start, heap_end = [int(x, 16) for x in heap.split()[0].split("-")]

        # Open memory
        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            search_bytes = search_string.encode()
            replace_bytes = replace_string.encode()

            if len(replace_bytes) > len(search_bytes):
                print("Error: Replacement string must not be longer than the search string.")
                sys.exit(1)

            offset = heap_data.find(search_bytes)
            if offset == -1:
                print("Error: Search string not found in the heap.")
                sys.exit(1)

            # Write replacement
            mem_file.seek(heap_start + offset)
            mem_file.write(replace_bytes.ljust(len(search_bytes), b'\x00'))

            print(f"Successfully replaced '{search_string}' with '{replace_string}' in the heap.")

    except PermissionError:
        print("Error: Permission denied. Try running as sudo.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Process not found. Is the PID correct?")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()

    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    read_write_heap(pid, search_string, replace_string)
