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
