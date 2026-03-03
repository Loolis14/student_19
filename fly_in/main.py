"""
main program.
"""

import sys
from my_parser import Parser, ConfigError
from engine import Engine, PathError


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No network of drones given.")
        sys.exit(1)

    file_parser = Parser()
    try:
        config = file_parser.main_parsing(sys.argv[1])
    except ConfigError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    my_engine = Engine()
    try:
        my_engine.main(config)
    except PathError as e:
        print(e)
        sys.exit(1)
