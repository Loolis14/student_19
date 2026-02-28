import sys
import re


class ConfigError(Exception):
    pass


class Parser:
    """Parse the file in a dictionnary."""

    def __init__(self) -> None:
        self.map_data: dict = {}

    @staticmethod
    def _file_reader(file: str) -> list[str]:
        """
        Read the file and create a list of every line.
        (# and empty line not take in count)
        """
        config_load = []
        with open(file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                config_load.append(line.split("#")[0])
        return config_load

    @staticmethod
    def _create_dictionnary(config: list[str]) -> dict[str, str]:
        """
        Create a dictionnary
        Check if the first line is 'nb_drones'
        Check if start and end hub are not duplicates
        Check if the line are correctly formated with ':'
        """
        if "nb_drones" not in config[0]:
            raise ConfigError("The first line must define "
                              "the number of drones using: "
                              "nb_drones: <positive_integer>")

        if sum(1 for start in config if "start_hub" in start) > 1:
            raise ConfigError("There must be exactly one start_hub")
        if sum(1 for end in config if "end_hub" in end) > 1:
            raise ConfigError("There must be exactly one end_hub")

        config_mission = {}
        for line in config:
            try:
                variable, content = line.split(":")
            except ValueError:
                return ("File not correctly formated.\n"
                        "Format accepted:\n"
                        "<variable>: <content>")
            else:
                config_mission[variable] = content
        return config_mission

    def parsing_in_map(self, file):
        config: dict[str, str] = self._file_parser(file)

        end_hub = config.get("end_hub", "").split()
        if not end_hub:
            raise ConfigError("An end_hub must be configured.")
        if len(end_hub) < 3 or len(end_hub) > 4:
            raise ConfigError("Ending zone should be defined: "
                              "<name> <x> <y> [metadata]")
        self.start_name = end_hub[0]
        if end_hub[1].isdigit():
            self.start_x = end_hub[1]
        else:
            raise ConfigError("Ending coordinate 'x' "
                              "should be an positive integer.")
        if end_hub[2].isdigit():
            self.start_y = end_hub[2]
        else:
            raise ConfigError("Ending coordinate 'x' "
                              "should be an postive integer.")
        if len(end_hub) == 4:
            if end_hub[3][0] == '[' and end_hub[3][-1] == ']':
                self.start_metadata = end_hub[3]
            else:
                raise ConfigError("Metadatas should be enclosed in brackets.")
        # connection = config.get("connection")
        # hub = config.get("hub")

    def missing_config(self) -> None:
        config_key = set(self.map_data.keys())
        config_need = {"nb_drones", "start_hub",
                       "end_hub", "hub", "connection"}
        config_missing = config_need - config_key
        if config_missing:
            raise ConfigError('Missing configuration: '
                              f'{", ".join(config_missing)}')

    def parse_drones(self) -> None:
        nb_drones = self.map_data.get("nb_drones", "").strip()
        if nb_drones.isdigit():
            self.nb_drones = int(nb_drones)
        else:
            raise ConfigError("nb_drones should be a positive integer.")

    @staticmethod
    def parse_metadata_zone(metadata: str) -> tuple[str]:
        data = {'zone': 'normal',
                'color': None,
                'max_drones': 1}

        pattern = re.compile(r"(zone|color|max_drones)=([^ ]+)")
        for match in metadata.split():
            if not pattern.match(match):
                raise ConfigError(f"{match} is not a valid syntax.")
            key, value = pattern.match(match).groups()
            if key == 'zone':
                if value not in ['blocked', 'normal', 'restricted', 'prority']:
                    raise ConfigError("Zone types must be one of: normal, "
                                      "blocked, restricted, priority.")
            if key == 'max_drones':
                if not value.isdigit():
                    raise ConfigError("Max drones data should be "
                                      "a positive integer.")
            if key == 'color':
                if not value.isalpha():
                    raise ConfigError("Values for color are any valid "
                                      "single-word strings.")
            data[key] = value
        return tuple(data.values())

    def parse_start(self, position: str) -> None:
        _hub = self.map_data.get(f"{position}_hub", "").split()
        if not _hub:
            raise ConfigError(f"A {position}_hub must be configured.")
        if len(_hub) < 3 or len(_hub) > 4:
            raise ConfigError(f"{position}ing zone should be defined: "
                              "<name> <x> <y> [metadata]")

        if _hub[1].isdigit():
            start_x = int(_hub[1])
        else:
            raise ConfigError(f"{position}ing coordinate 'x' "
                              "should be a positive integer.")
        if _hub[2].isdigit():
            start_y = int(_hub[2])
        else:
            raise ConfigError(f"{position}ing coordinate 'y' "
                              "should be a postive integer.")
        if len(_hub) == 4:
            if _hub[3][0] == '[' and _hub[3][-1] == ']':
                start_metadata = Parser.parse_metadata_zone(_hub[3][1:-1])
            else:
                raise ConfigError("Metadatas should be enclosed in brackets.")

        self.map_data[f'{position}_hub'] = {
            f'{position}_name': _hub[0],
            f'{position}_x': start_x,
            f'{position}_y': start_y,
            f'{position}_metadata': start_metadata
            }

    def main_parsing(self, file: str) -> None:
        file_read = Parser._file_reader(file)
        try:
            self.map_data = Parser._create_dictionnary(file_read)
            self.missing_config()
            self.parse_drones()
            self.parse_start('start')
            self.parse_start('end')
            self.parse_hub()
        except ConfigError as e:
            print(f"Configuration error: {e}")
            sys.exit()
