import re
from typing import Optional


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
                # creer une classe ligne pour stocker la ligne et son numero
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                config_load.append(line.split("#")[0])
        return config_load

    def _create_dictionnary(self, config: list[str]) -> None:
        """
        Create a dictionnary
        Check if the first line is 'nb_drones'
        Check if start and end hub are not duplicates
        Check if the line are correctly formated with ':'
        """
        if "nb_drones" not in config[0]:
            raise ConfigError("The first line must define "
                              "the number of drones using: "
                              "'nb_drones: <x>'")

        if sum(1 for start in config if "start_hub" in start) > 1:
            raise ConfigError("There must be exactly one start_hub")
        if sum(1 for end in config if "end_hub" in end) > 1:
            raise ConfigError("There must be exactly one end_hub")

        config_mission = {}
        for line in config:
            try:
                variable, content = line.split(":")
            except ValueError:
                raise ConfigError(f"'{line}' not correctly formated.\n\n"
                                  "Usage: <key>: <content>")
            else:
                content = content.strip()
                if variable in {"hub", "connection"}:
                    config_mission.setdefault(variable, []).append(content)
                else:
                    config_mission[variable] = content
        self.map_data = config_mission

    def _missing_config(self) -> None:
        """
        Check if all mandatory keys are present.
        """
        config_key = set(self.map_data.keys())
        config_need = {"nb_drones", "start_hub",
                       "end_hub", "hub", "connection"}
        config_missing = config_need - config_key
        if config_missing:
            raise ConfigError('missing configuration'
                              f' \'{", ".join(config_missing)}\' ')

    def _parse_drones(self) -> None:
        """Create an int which represente the number of drones."""
        nb_drones = self.map_data.get("nb_drones", "").strip()
        if nb_drones.isdigit():
            self.nb_drones = int(nb_drones)
        else:
            raise ConfigError(f"'{nb_drones}' not a positive "
                              "integer in nb_drones.")

    @staticmethod
    def _parse_metadata_hub(metadata: Optional[str]) -> tuple[str]:
        """
        Create a tuple with the metadata, if nothing is given,
        default values are given.
        """
        data = {'zone': 'normal',
                'color': None,
                'max_drones': 1}

        if not metadata:
            return tuple(data.values())

        pattern = re.compile(r"(zone|color|max_drones)=([^ ]+)")
        for match in metadata.split():
            if not pattern.match(match):
                raise ConfigError(f"'{match}' not a valid syntax.")
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
                    raise ConfigError(f"'{value}' not a valid color. \n"
                                      "Values for color are any valid "
                                      "single-word strings.")
            data[key] = value
        return tuple(data.values())

    @staticmethod
    def _parse_hub(value: str) -> dict:
        """Parse hub in a dictionnary."""
        pattern = re.compile(r"^([^- ]+) (\d+) (\d+)(?: \[([^\]]+)\])?$")
        match = pattern.match(value)
        if not match:
            raise ConfigError(f"'{value}' not a valid syntax\n\n"
                              "Usage: <name> <x> <y> [metadata]\n"
                              "Zone names can use any valid characters "
                              "but dashes and spaces.\nx et y should "
                              "be positive integers.\nAll metadata is "
                              "optional and enclosed in brackets.")
        name, x, y, metadata = match.groups()
        tuple_metadata = Parser._parse_metadata_hub(metadata)
        return {
            'name': name,
            'x': int(x),
            'y': int(y),
            'metadata': tuple_metadata
            }

    def _parse_metadata_connection(metadata: Optional[str]) -> int:
        if not metadata:
            return 1

        pattern = re.compile(r"^max_link_capacity=(\d+)$")
        match = pattern.match(metadata)
        if not match:
            raise ConfigError(f"'{metadata}' connection metadata block "
                              "not valid\n\n"
                              "Usage: max_link_capacity=<x>\nx should be"
                              " a positive integer.")
        value = match.groups()
        if not value.isdigit():
            raise ConfigError(f"{value}.\nCapacity values "
                              "max_link_capacity must be positive integers.")
        return value

    def _parse_connections(self) -> list[set, Optional[tuple]]:
        """The same connection must not appear more than once"""
        connections = []
        hub_names = [hub.get('name') for hub in self.map_data['hub']]
        hub_names.append(self.map_data['start_hub']['name'])
        hub_names.append(self.map_data['end_hub']['name'])

        pattern = re.compile(r"^([^ -]+)-([^ -]+)(?: \[([^\]]+)\])?$")
        temp_co = []
        for connection in self.map_data['connection']:
            match = pattern.match(connection.strip())
            if not match:
                raise ConfigError(f"'{connection}' connection invalid syntax\n"
                                  "\nUsage: <zone1>-<zone2> [metadata]"
                                  "\nZone names can use any valid characters "
                                  "but dashes and spaces.")
            connection_b, connection_a, metadata = match.groups()
            if connection_a not in hub_names:
                raise ConfigError(f"{connection_a} not a valid hub name.")
            if connection_b not in hub_names:
                raise ConfigError(f"{connection_b} not a valid hub name.")
            for set_ in temp_co:
                if not (set_ - {connection_a, connection_b}):
                    raise ConfigError(f"'{connection}' connection "
                                      "appear more than once.")
            temp_co.append({connection_a, connection_b})
            max_capacity = Parser._parse_metadata_connection(metadata)
            connections.append(({connection_a, connection_b}, max_capacity))

            self.map_data['connection'] = connections

    def main_parsing(self, file: str) -> None:
        file_read = Parser._file_reader(file)
        if not file_read:
            raise ConfigError("Empty file configuration.")
        self._create_dictionnary(file_read)
        self._missing_config()

        # parsing of the different config keys
        self._parse_drones()

        dict_start = Parser._parse_hub(self.map_data['start_hub'])
        self.map_data['start_hub'] = dict_start

        dict_end = Parser._parse_hub(self.map_data['end_hub'])
        self.map_data['end_hub'] = dict_end

        for i, hub in enumerate(self.map_data['hub']):
            dict_hub = Parser._parse_hub(hub)
            self.map_data['hub'][i] = dict_hub

        self._parse_connections()
