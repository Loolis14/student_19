import re
from typing import Optional


class ConfigError(Exception):
    pass


class Line:
    """Keep the content and the number of the line."""

    def __init__(self, nb: int, content: str) -> None:
        self.nb = nb
        self.content = content
        self.key = ""
        self.value = ""


class Parser:
    """Parse the file in a dictionnary."""

    def __init__(self) -> None:
        self.lines: list[Line] = []
        self.nb_drones = 0
        self.start_hub = ""
        self.end_hub = ""
        self.hub = []
        self.connection = []

    def _file_reader(self, file: str) -> None:
        """
        Read the file and create a list of every line.
        (# and empty line not take in count)
        """
        try:
            with open(file) as f:
                for i, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    content = line.split("#")[0].strip()
                    self.lines.append(Line(i, content))
        except FileNotFoundError:
            raise ConfigError(f"'{file}' file not found.")

    def _create_dictionnary(self) -> None:
        """
        Create a dictionnary with the data
        Check if the first line is 'nb_drones'
        Check if start and end hub are not duplicates
        Check if the line are correctly formated with ':'
        """
        if "nb_drones" not in self.lines[0].content:
            raise ConfigError(f"line {self.lines[0].nb} error. The first "
                              "line must define the number of drones.\n"
                              "Usage: nb_drones: <x>")

        if sum(1 for start in self.lines if "start_hub" in start.content) > 1:
            raise ConfigError("More than one 'start_hub' is defined.")
        if sum(1 for end in self.lines if "end_hub" in end.content) > 1:
            raise ConfigError("More than one 'end_hub' is defined.")

        for line in self.lines:
            try:
                variable, content = line.content.split(":")
            except ValueError:
                raise ConfigError(f"line {line.nb} '{line.content}' not "
                                  "correctly formated.\n"
                                  "Usage: <key>: <content>")
            else:
                line.key = variable
                line.value = content.strip()

    def _check_keys_config(self) -> None:
        """
        Check if all mandatory keys are present and if
        something must not be present.
        """
        config_keys = {line.key for line in self.lines}
        config_mandatory = {"nb_drones", "start_hub",
                            "end_hub", "hub", "connection"}
        config_missing = config_mandatory - config_keys
        if config_missing:
            raise ConfigError('missing configuration'
                              f' \'{", ".join(config_missing)}\' ')

        config_not_allowed = config_keys - config_mandatory
        result_printable = []
        if config_not_allowed:
            for key in config_not_allowed:
                for line in self.lines:
                    if key == line.key:
                        result_printable.append(f'line {line.nb} "{key}"')
            raise ConfigError("configuration's key not valid\n"
                              f"{','.join(result_printable)}")

    def _parse_drones(self, drone_line: Line) -> None:
        """Create an int which represente the number of drones."""
        nb_drones = drone_line.value
        if nb_drones.isdigit():
            self.nb_drones = int(nb_drones)
        else:
            raise ConfigError(f"line {drone_line.nb} '{nb_drones}' "
                              "not a positive integer.")

    @staticmethod
    def _parse_hub_metadata(metadata: Optional[str],
                            line: Optional[int]) -> dict:
        """
        Create a tuple with the metadata, if nothing is given,
        default values are given.
        """
        data = {'zone': 'normal',
                'color': None,
                'max_drones': 1}

        if not metadata:
            return data

        pattern = re.compile(r"(zone|color|max_drones)=([^ ]+)")
        for match in metadata.split():
            if not pattern.match(match):
                raise ConfigError(f"line {line} '{match}' not a valid syntax."
                                  "\nUsage: <zone|color|max_drones>=<value>")
            key, value = pattern.match(match).groups()
            if key == 'zone':
                zone_type = ['blocked', 'normal', 'restricted', 'priority']
                if value not in zone_type:
                    raise ConfigError(f"line {line} '{value}' not valid.\n"
                                      "Zone types must be one of: normal, "
                                      "blocked, restricted, priority.")
            if key == 'max_drones':
                if not value.isdigit():
                    raise ConfigError(f"line {line} '{value}' not valid.\n"
                                      "Max drones data should be "
                                      "a positive integer.")
                value = int(value)
            if key == 'color':
                if not value.isalpha():
                    raise ConfigError(f"line {line} '{value}' not a valid "
                                      "color.\nValues for color are any valid "
                                      "single-word strings.")
            data[key] = value
        return data

    def _parse_hub(self, hub_config: Line) -> None:
        """Parse the configuration on hub line."""
        pattern = re.compile(r"^([^- ]+) (-?\d+) (-?\d+)(?: \[([^\]]+)\])?$")
        match = pattern.match(hub_config.value)
        if not match:
            raise ConfigError(f"line {hub_config.nb} '{hub_config.value}' not "
                              "a valid syntax\n\n"
                              "Usage: <name> <x> <y> [metadata]\n"
                              "Zone names can use any valid characters but "
                              "dashes and spaces.\nx and y should be integers."
                              "\nAll metadata is optional and "
                              "enclosed in brackets.")
        name, x, y, metadata = match.groups()
        dict_config = {
            'name': name,
            'x': int(x),
            'y': int(y)
            }
        dict_metadata = Parser._parse_hub_metadata(metadata, hub_config.nb)
        dict_config.update(dict_metadata)
        attr_name = hub_config.key
        if attr_name == 'hub':
            self.hub.append(dict_config)
        else:
            setattr(self, attr_name, dict_config)

    @staticmethod
    def _parse_metadata_connection(metadata: Optional[str], line: int) -> int:
        if not metadata:
            return 1

        pattern = re.compile(r"^max_link_capacity=(\d+)$")
        match = pattern.match(metadata)
        if not match:
            raise ConfigError(f"line {line} '{metadata}' connection metadata "
                              "block not valid\n\n"
                              "Usage: max_link_capacity=<x>\nx should be"
                              " a positive integer.")
        value = match.group(1)
        if not value.isdigit():
            raise ConfigError(f"line {line} '{value}' not a positive integers")
        return int(value)

    def _parse_connection(self, co_line: Line) -> None:
        """Parse connection line."""
        hub_names = [hub['name'] for hub in self.hub]
        hub_names.append(self.start_hub['name'])
        hub_names.append(self.end_hub['name'])
        pattern = re.compile(r"^([^ -]+)-([^ -]+)(?: \[([^\]]+)\])?$")
        match = pattern.match(co_line.value)
        if not match:
            raise ConfigError(f"line {co_line.nb} '{co_line.value}' invalid "
                              "syntax\n\nUsage: <zone1>-<zone2> "
                              "[max_link_capacity=<x>]"
                              "\nZone names can use any valid characters but"
                              " dashes and spaces.")
        hub_b, hub_a, metadata = match.groups()
        if hub_a not in hub_names:
            raise ConfigError(f"line {co_line.nb} '{hub_a}' "
                              "not a registered hub name.")
        if hub_b not in hub_names:
            raise ConfigError(f"line {co_line.nb} '{hub_b}' "
                              "not a registered hub name.")

        for tuple in self.connection:
            hub1, hub2, data = tuple
            if not ({hub1, hub2} - {hub_a, hub_b}):
                raise ConfigError(f"line {co_line.nb} '{hub_a}-{hub_b}' "
                                  "connection appear more than once.")
        capacity = Parser._parse_metadata_connection(metadata, co_line.nb)
        self.connection.append((hub_a, hub_b, capacity))

    def _check_unique_start(self) -> None:
        if self.start_hub['x'] == self.end_hub['x']:
            if self.start_hub['y'] == self.end_hub['y']:
                raise ConfigError("The start and end zone have "
                                  "the same coordinates.")

    def main_parsing(self, file: str) -> dict:
        self._file_reader(file)
        if not self.lines:
            raise ConfigError("Empty configuration file.")
        self._create_dictionnary()
        self._check_keys_config()

        for config_line in self.lines:
            match config_line.key:
                case 'nb_drones':
                    self._parse_drones(config_line)
                case 'start_hub' | 'end_hub' | 'hub':
                    self._parse_hub(config_line)
        for config_line in self.lines:
            if config_line.key == 'connection':
                self._parse_connection(config_line)
        self._check_unique_start()

        return {
            'nb_drones': self.nb_drones,
            'start_hub': self.start_hub,
            'end_hub': self.end_hub,
            'hub': self.hub,
            'connection': self.connection,
        }
