#!/usr/bin/env python3

"""
Install a virtuel environnement and execute:
'pip install pydantic'
"""

try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("Pydantic module not installed.\nRun:")
    print("pip install pydantic")
    exit(1)
from enum import Enum
from datetime import datetime, timezone
from typing_extensions import Self


class Rank(Enum):
    CADET = 'cadet'
    OFFICIER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(gt=18, lt=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(gt=0, lt=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    duration_days: int = Field(gt=1, lt=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(gt=1.0, lt=10000.0)

    @model_validator(mode='after')
    def checking_id(self) -> 'Self':
        if self.mission_id[0] != 'M':
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode='after')
    def checking_crew(self) -> 'Self':
        for member in self.crew:
            if (member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN):
                return self
        raise ValueError("Mission must have at least one Commander or Captain")

    @model_validator(mode='after')
    def checking_mission(self) -> 'Self':
        if self.duration_days <= 365:
            return self
        nbr_crew = len(self.crew)
        experienced_crew = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced_crew += 1
        if experienced_crew < nbr_crew / 2:
            raise ValueError(
                "Long missions (> 365 days) need 50% "
                "experienced crew (5+ years)"
                )
        return self

    @model_validator(mode='after')
    def checking_activity(self) -> 'Self':
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        mission1 = SpaceMission(mission_id="M2024_MARS",
                                mission_name="Mars Colony Establishment",
                                destination="Mars", duration_days=900,
                                crew=[
                                    {
                                        "member_id": "sarah025",
                                        "name": "Sarah Connor",
                                        "rank": "commander",
                                        "age": 50,
                                        "specialization": "Mission Command",
                                        "years_experience": 40,
                                    },
                                    {
                                        "member_id": "john689",
                                        "name": "John Smith",
                                        "rank": "lieutenant",
                                        "age": 35,
                                        "specialization": "Navigation",
                                        "years_experience": 25,
                                    },
                                    {
                                        "member_id": "alice8887",
                                        "name": "Alice Johnson",
                                        "rank": "officer",
                                        "age": 25,
                                        "specialization": "Engineering",
                                        "years_experience": 10,
                                    },
                                ],
                                budget_millions=2500.0)
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission1.mission_name}")
    print(f"ID: {mission1.mission_id}")
    print(f"Destination: {mission1.destination}")
    print(f"Duration: {mission1.duration_days} days")
    print(f"Budget: ${mission1.budget_millions}M")
    print(f"Crew size: {len(mission1.crew)}")
    print("Crew members:")
    for member in mission1.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")

    print("\n=========================================")
    try:
        mission1 = SpaceMission(mission_id="M2024_MARS",
                                mission_name="Mars Colony Establishment",
                                destination="Mars", duration_days=900,
                                crew=[
                                    {
                                        "member_id": "sarah025",
                                        "name": "Sarah Connor",
                                        "rank": "lieutenant",
                                        "age": 50,
                                        "specialization": "Mission Command",
                                        "years_experience": 40,
                                    },
                                    {
                                        "member_id": "john689",
                                        "name": "John Smith",
                                        "rank": "lieutenant",
                                        "age": 35,
                                        "specialization": "Navigation",
                                        "years_experience": 25,
                                    },
                                    {
                                        "member_id": "alice8887",
                                        "name": "Alice Johnson",
                                        "rank": "officer",
                                        "age": 25,
                                        "specialization": "Engineering",
                                        "years_experience": 10,
                                    },
                                ],
                                budget_millions=2500.0)
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
