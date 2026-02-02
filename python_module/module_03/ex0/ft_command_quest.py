#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    nbr_arg: int = len(sys.argv)
    if nbr_arg - 1 == 0:
        print("No argument provided!")
    else:
        print(f"Arguments received = {nbr_arg - 1}")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"Argument {i + 1}: {arg}")
    print(f"Total arguments: {nbr_arg}")
