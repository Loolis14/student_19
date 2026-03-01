"""
main program.
"""

import sys
from parser import Parser


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No network of drones given.")
        sys.exit(1)

    file_parser = Parser()
    file_parser.main_parsing(sys.argv[1])
    print('drones', file_parser.map_data['nb_drones'])
    print('hub', file_parser.map_data['hub'])
    print('start', file_parser.map_data['start_hub'])
    print('end', file_parser.map_data['end_hub'])
    print('connection', file_parser.map_data['connection'])
