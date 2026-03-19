"""Entry point of the drone network simulation program.

This module orchestrates the full execution pipeline:
    1. Parse the input configuration file
    2. Validate data and handle parsing errors
    3. Run the simulation engine
    4. Handle runtime and pathfinding errors

Raises:
    SystemExit: If an error occurs during parsing or execution.

Usage:
    python main.py <config_file>
"""

import sys
from my_parser import Parser, ConfigError
from engine import Engine, PathError


def main() -> None:
    """Run the drone simulation program.

    Handles:
        - Argument parsing
        - Configuration loading
        - Engine execution

    Exits the program with an appropriate status code on error.
    """
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
    except (PathError, ImportError, ValueError, NameError) as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
