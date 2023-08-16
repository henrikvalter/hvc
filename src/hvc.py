#!/usr/bin/env python3

import sys

def main():
    nr_input_files = len(sys.argv) - 1
    if nr_input_files == 0:
        print("ERROR: No input files.")

    for file in sys.argv[1:]:
        print(f"Compiling {file}")
        compile_file(file)

def compile_file(file):
    with open(file, 'r') as f:
        for cnt, line in enumerate(f):
            line_nr = cnt + 1
            stripped = line.strip()
            if stripped != "":
                print(f"{file}:{line_nr}: Syntax error")
                print(f"{line_nr} | ".rjust(8), end="")
                print(f"{stripped}".ljust(2))
                print(f"| ".rjust(8), end="")
                print(f"^~~")
                sys.exit(1)

if __name__ == "__main__":
    main()
