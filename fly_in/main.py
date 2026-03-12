"""
main program.
"""

import sys
from srcs.my_parser import Parser, ConfigError
from srcs.engine import Engine, PathError


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No network of drones given.")
        sys.exit(0)

    file_parser = Parser()
    try:
        config = file_parser.main_parsing(sys.argv[1])
    except ConfigError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    my_engine = Engine()
    try:
        my_engine.main(config)
    except (PathError, ImportError) as e:
        print(e)
        sys.exit(1)
