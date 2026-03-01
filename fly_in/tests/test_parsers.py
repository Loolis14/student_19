import pytest
from parser import Parser, ConfigError
from pathlib import Path

BASE = Path(__file__).parent / "configs"

@pytest.mark.parametrize("filename", [
    BASE / "connection_meta_not_positive.txt",
    BASE / "drone_missing.txt",
    BASE / "drone_not_first.txt",
    BASE / "drone_not_int.txt",
    BASE / "g_doublepoint_missing.txt",
    BASE / "g_empty_file.txt",
    BASE / "g_mistake_in_name.txt",
    BASE / "hub_incorrect_syntax.txt",
    BASE / "hub_x_not_int.txt",
    BASE / "hub_x_not_positive.txt",
    BASE / "start_double.txt",
])
def test_invalid_configs(filename):
    p = Parser()
    with pytest.raises(ConfigError) as excinfo:
        p.main_parsing(filename)
    print(excinfo.value)
