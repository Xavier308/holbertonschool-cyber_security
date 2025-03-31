#!/usr/bin/python3
import sys


def usage():
    print("Usage: {} pid search_string replace_string".format(sys.argv[0]))
    sys.exit(1)


def main():
    # Check the number of arguments
    if len(sys.argv) != 4:
        usage()

    # Get and validate the process ID
    try:
        pid = int(sys.argv[1])
    except ValueError:
        usage()

    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    # Convert the strings to bytes (ASCII only)
    try:
        search_bytes = search_str.encode('ascii')
        replace_bytes = replace_str.encode('ascii')
    except UnicodeEncodeError:
        print("Error: Only ASCII strings are allowed.")
        sys.exit(1)

    # Ensure the replacement string is not longer than the search string.
    # If it is shorter, we'll pad with null bytes.
    if len(replace_bytes) > len(search_bytes):
        print("Error: Replacement string must not be longer than "
              "the search string.")
        sys.exit(1)

    maps_path = "/proc/{}/maps".format(pid)
    mem_path = "/proc/{}/mem".format(pid)

    # Locate the heap segment in the process's memory maps
    try:
        with open(maps_path, 'r') as maps_file:
            heap_range = None
            for line in maps_file:
                if "[heap]" in line:
                    # The first field is the address range
                    # in the form start-end (hexadecimal)
                    addr_range = line.split()[0]
                    start_str, end_str = addr_range.split('-')
                    heap_range = (int(start_str, 16), int(end_str, 16))
                    break
            if not heap_range:
                print("Error: Heap segment not found.")
                sys.exit(1)
    except IOError as e:
        print("Error opening {}: {}".format(maps_path, e))
        sys.exit(1)

    # Open the process's memory and search for
    # the target string in the heap region
    try:
        with open(mem_path, 'rb+') as mem_file:
            start, end = heap_range
            mem_file.seek(start)
            heap_data = mem_file.read(end - start)

            index = heap_data.find(search_bytes)
            if index == -1:
                print("String '{}' not found in heap.".format(search_str))
                sys.exit(1)
            else:
                print("Found '{}' at heap offset 0x{:x}".format(
                    search_str, index))
                # Seek to the exact position in memory and
                # write the replacement
                mem_file.seek(start + index)
                # If replacement string is shorter,
                # pad with null bytes to clear the rest
                new_bytes = replace_bytes + b'\x00' * (
                    len(search_bytes) - len(replace_bytes))
                mem_file.write(new_bytes)
                print("Replaced '{}' with '{}'.".format(
                    search_str, replace_str))
    except IOError as e:
        print("Error opening {}: {}".format(mem_path, e))
        sys.exit(1)


if __name__ == '__main__':
    main()
