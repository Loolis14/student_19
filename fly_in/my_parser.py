import re
from typing import Optional


class ConfigError(Exception):
    """Exception raised for configuration errors in the parser."""
    pass


class Line:
    """Stores the content and the line number of a configuration entry.

    Attributes:
        nb (int): The line number in the original file.
        content (str): The raw text content of the line.
        key (str): The key extracted on the content.
        value (str): The value associated with the key.
    """

    def __init__(self, nb: int, content: str) -> None:
        """Initalizes a line object."""
        self.nb: int = nb
        self.content: str = content
        self.key: str = ""
        self.value: str = ""


class Parser:
    """Parse a file for the fly in simulation.

    This class reads a text file, validates its structure, and transforms
    the data into dictionaries and lists usable by the simulator.

    Attributes:
        lines (list[Line]): Store the Line objects.
        nb_drones (int): Total number of drones.
        start_hub (dict): Datas for the starting hub.
        end_hub (dict): Datas for the destination hub.
        hub (list[dict]): List of intermediate hubs.
        connection (list[tuple]): List of connections (hub_a, hub_b, capacity).
        coord (list[tuple[int, int]]): List of all hub coordinates.
        names (list[str]): list of all hub names.
    """

    def __init__(self) -> None:
        """Initalizes a parser file object."""
        self.lines: list[Line] = []
        self.nb_drones: int = 0
        self.start_hub: dict[str, Optional[str | int]] = {}
        self.end_hub: dict[str, Optional[str | int]] = {}
        self.hub: list[dict[str, Optional[str | int]]] = []
        self.connection: list[tuple[str, str, int]] = []
        self.coord: list[tuple[int, int]] = []
        self.names: list[str] = []

    def _file_reader(self, file: str) -> None:
        """Reads the file and ignores comments and empty lines.

        Args:
            file (str): Path to the configuration file.

        Raises:
            ConfigError: If the file is not found.
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
        """Pre-processes lines to extract key/value pairs.

        Performs initial structure validations (presence of drone count,
        uniqueness of start/end hubs, and formatting via ':').

        Raises:
            ConfigError: If the basic file structure is invalid.
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
        """Verifies that all mandatory keys are present and valid.

        Raises:
            ConfigError: If a mandatory key is missing or
            an unknown key is found.
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
        """Parses the number of drones.

        Args:
            drone_line (Line): The line containing 'nb_drones'.

        Raises:
            ConfigError: If the value is not a positive integer.
        """
        nb_drones: str = drone_line.value
        if nb_drones.isdigit():
            self.nb_drones = int(nb_drones)
        else:
            raise ConfigError(f"line {drone_line.nb} '{nb_drones}' "
                              "not a positive integer.")

    @staticmethod
    def _parse_hub_metadata(metadata: Optional[str],
                            line: Optional[int]) -> dict[str,
                                                         Optional[str | int]]:
        """Parses optional bracketed metadata for a hub. Zone, color and
            the maximum drones on the hub can be defined.

        Args:
            metadata (str, optional): Metadata string.
            line (int): Line number for error reporting.

        Returns:
            dict: Parsed metadata with default values for missing fields.

        Raises:
            ConfigError: If the metadata syntax or values are invalid.
        """
        data: dict[str, Optional[str | int]] = {
            'zone': 'normal',
            'color': None,
            'max_drones': 1}

        if not metadata:
            return data

        pattern = re.compile(r"(zone|color|max_drones)=([^ ]+)")
        for match in metadata.split():
            line_match = pattern.match(match)
            if not line_match:
                raise ConfigError(f"line {line} '{match}' not a valid syntax."
                                  "\nUsage: <zone|color|max_drones>=<value>")
            groups = line_match.groups()
            if not groups:
                raise ConfigError(f"line {line} '{match}' not a valid syntax."
                                  "\nUsage: <zone|color|max_drones>=<value>")
            key, value = groups
            if key == 'zone':
                zone_type: list[str] = ['blocked', 'normal',
                                        'restricted', 'priority']
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
        """Extracts coordinates and metadata for a hub.

        Args:
            hub_config (Line): A line of type 'hub', 'start_hub', or 'end_hub'.

        Raises:
            ConfigError: If the 'Name X Y [metadata]' format is not respected.
        """
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
        x, y = map(int, (x, y))
        if (x, y) in self.coord:
            raise ConfigError(f"line {hub_config.nb} coordinates {x, y}."
                              "There is already a hub with these coordinates.")
        self.coord.append((x, y))
        if name in self.names:
            raise ConfigError(f"line {hub_config.nb} name {name}."
                              "There is already a hub with these name.")
        self.names.append(name)
        dict_config: dict[str, Optional[str | int]] = {
            'name': name,
            'x': x,
            'y': y
            }
        dict_metadata = Parser._parse_hub_metadata(metadata, hub_config.nb)
        dict_config.update(dict_metadata)
        attr_name: str = hub_config.key
        if attr_name == 'hub':
            self.hub.append(dict_config)
        else:
            setattr(self, attr_name, dict_config)

    @staticmethod
    def _parse_metadata_connection(metadata: Optional[str], line: int) -> int:
        """Parses the maximum capacity of a connection.

        Args:
            metadata (str, optional): Configure the max link capacity.
            line (int): Line number.

        Returns:
            int: The parsed max link capacity or 1 by default.

        Raises:
            ConfigError: If the syntax or value is incorrect.
        """
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
        """Parses a link between two hubs.

        Args:
            co_line (Line): Line defining a connection.

        Raises:
            ConfigError: If hubs do not exist or
            if the connection is a duplicate.
        """
        hub_names: list[Optional[str | int]] = [hub['name']
                                                for hub in self.hub]
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

        for hub1, hub2, data in self.connection:
            if not ({hub1, hub2} - {hub_a, hub_b}):
                raise ConfigError(f"line {co_line.nb} '{hub_a}-{hub_b}' "
                                  "connection appear more than once.")
        capacity = Parser._parse_metadata_connection(metadata, co_line.nb)
        self.connection.append((hub_a, hub_b, capacity))

    def _check_unique_start(self) -> None:
        """Verifies that the start and end hubs are
        not at the same coordinates.

        Raises:
            ConfigError: If start_hub and end_hub
            share the same (X, Y) coordinates.
        """
        if self.start_hub['x'] == self.end_hub['x']:
            if self.start_hub['y'] == self.end_hub['y']:
                raise ConfigError("The start and end zone have "
                                  "the same coordinates.")

    def main_parsing(self, file: str) -> tuple[int,
                                               dict[str, Optional[str | int]],
                                               dict[str, Optional[str | int]],
                                               list[dict[str,
                                                         Optional[str | int]]],
                                               list[tuple[str, str, int]]]:
        """Executes the full parsing pipeline for the file.

        Args:
            file (str): Path to the configuration file.

        Returns:
            dict: A dictionary containing 'nb_drones', 'start_hub', 'end_hub',
                'hub' (list), and 'connection' (list).

        Raises:
            ConfigError: If an error occurs at any stage of parsing.
        """
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

        return (self.nb_drones, self.start_hub, self.end_hub, self.hub,
                self.connection)
