"""Run: pytest -s"""

import pytest
from my_parser import Parser, ConfigError
from pathlib import Path

BASE = Path(__file__).parent / "test_config"


@pytest.mark.parametrize("filename", [
    BASE / "connection_double.txt",
    BASE / "connection_invalid_syntax.txt",
    BASE / "connection_invalid_syntax2.txt",
    BASE / "connection_meta_invalid.txt",
    BASE / "connection_meta_not_int.txt",
    BASE / "connection_meta_not_positive.txt",
    BASE / "connection_name_invalid.txt",
    BASE / "drone_missing.txt",
    BASE / "drone_not_first.txt",
    BASE / "drone_not_int.txt",
    BASE / "g_doublepoint_missing.txt",
    BASE / "g_empty_file.txt",
    BASE / "g_mistake_in_name.txt",
    BASE / "hub_incorrect_syntax.txt",
    BASE / "hub_incorrect_syntax2.txt",
    BASE / "hub_meta_invalid_syntax.txt",
    BASE / "hub_meta_invalid_syntax2.txt",
    BASE / "hub_x_not_int.txt",
    BASE / "missing_hub.txt",
    BASE / "start_double.txt",
])
def test_invalid_configs(filename):
    p = Parser()
    with pytest.raises(ConfigError) as excinfo:
        p.main_parsing(filename)
    name = Path(filename).name
    print(name)
    print(excinfo.value)
    print()
