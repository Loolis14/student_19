"""
nb_drones: 5
start_hub: hub 0 0 [color=green]
end_hub: goal 10 10 [color=yellow]
hub: roof1 3 4 [zone=restricted color=red]
hub: roof2 6 2 [zone=normal color=blue]
hub: corridorA 4 3 [zone=priority color=green max_drones=2]
hub: tunnelB 7 4 [zone=normal color=red]
hub: obstacleX 5 5 [zone=blocked color=gray]
connection: hub-roof1
connection: hub-corridorA
connection: roof1-roof2
connection: roof2-goal
connection: corridorA-tunnelB [max_link_capacity=2]
connection: tunnelB-goal
"""

import sys


class Parser():

    def __init__(self) -> None:
        self.content = []
        self.dictionnary = {}

    def file_reader(self, file: str) -> None:
        with open(file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                self.content.append(line)

    def file_parser(self) -> None:
        try:
            for item, content in self.content.split(":"):
        except ValueError:
            return ("File not correctly formated."
                    "Format accepted:"
					"<>: <>")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No network of drones given.")
        exit(1)
    parse = Parser()
    content = parse.file_reader(sys.argv[1])
    parse.file_parser(content)
