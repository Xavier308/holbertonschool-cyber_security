#!/usr/bin/python3

"""
read_write_heap.py - Script to search and replace a string in
the heap of a running process.

Usage:
    python3 read_write_heap.py pid search_string replace_string

Arguments:
    pid - Process ID of the target process
    search_string - ASCII string to search for in the heap
    replace_string - ASCII string to replace the search_string
"""

import sys


def find_and_replace_in_heap(pid, search_string, replace_string):
    """
    Find and replace a string in the heap memory of a running process.

    Parameters:
        pid (int): Process ID of the target process
        search_string (bytes): String to search for in the heap
        replace_string (bytes): String to replace the search_string
    """
    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"

    try:
        # Open the maps file to locate the heap segment
        with open(maps_path, "r") as maps_file:
            heap = None
            for line in maps_file:
                if "[heap]" in line:
                    heap = line
                    break

            if not heap:
                print("Error: Could not find the heap segment.")

            # Parse the heap segment's memory range
            heap_start, heap_end = [int(x, 16)
                                    for x in heap.split()[0].split("-")]
        # Open the memory file to search and replace in the heap
        with open(mem_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            # Ensure the replacement string is not longer
            # than the search string
            if len(replace_string) > len(search_string):
                print(
                    "Warning: Replacement string is longer"
                    "than the search string."
                    "This may cause memory corruption."
                    )

            # Search for the target string in the heap
            offset = heap_data.find(search_string)
            if offset == -1:
                print("Error: Search string not found in the heap.")
                sys.exit(1)

            # Replace the string in the memory
            mem_file.seek(heap_start + offset)
            mem_file.write(replace_string.ljust(len(search_string), b'\x00'))

            print(
                "SUCCESS!")

    except PermissionError:
        print("Error: Permission denied. Try running as sudo.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Process not found. Is the PID correct?")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle input arguments
    and execute the heap string replacement.
    """

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be an integer.")

    search_string = sys.argv[2].encode()
    replace_string = sys.argv[3].encode()

    find_and_replace_in_heap(pid, search_string, replace_string)


if __name__ == "__main__":
    main()
