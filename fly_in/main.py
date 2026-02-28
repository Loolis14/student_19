"""
main program.
"""

import sys
from parser import Parser, ConfigError


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No network of drones given.")
        sys.exit(1)
    file_parser = Parser()
    file_parser.main_parsing(sys.argv[1])
    print(file_parser.map_data)
