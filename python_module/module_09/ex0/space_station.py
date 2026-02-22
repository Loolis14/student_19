#!/usr/bin/env python3
"""
Install a virtuel environnement and execute:
'pip install pydantic'
"""

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=1, lt=20)
    power_level: float = Field(gt=0.0, lt=100.0)
    oxygen_level: float = Field(gt=0.0, lt=100.0)
    last_maintenance: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("========================================")
    try:
        station = SpaceStation(station_id="ISS001",
                               name="International Space Station",
                               crew_size=6, power_level=85.5,
                               oxygen_level=92.3)
    except Exception as e:
        print(e)
    else:
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Not'}")

    print("\n========================================")
    try:
        station = SpaceStation(station_id="ISS001",
                               name="International Space Station",
                               crew_size=50, power_level=85.5,
                               oxygen_level=92.3)
    except Exception as e:
        print("Expected validation error:")
        print(e)
    else:
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Not'}")


if __name__ == "__main__":
    main()
