#!/usr/bin/env python3

"""
Install a virtuel environnement and execute:
'pip install pydantic'
"""

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime, timezone
from typing import Optional
from typing_extensions import Self


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telephatic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(gt=0.0, lt=10.0)
    duration_minutes: int = Field(gt=1, lt=1440)
    witness_count: int = Field(gt=1, lt=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_contact_id(self) -> 'Self':
        if self.contact_id[:2] != "AC":
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        return self

    @model_validator(mode='after')
    def check_physical_contact(self) -> 'Self':
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError('Physical contact reports must be verified')
        return self

    @model_validator(mode='after')
    def check_telephatic_contact(self) -> 'Self':
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
                )
        return self

    @model_validator(mode='after')
    def check_strong_signal(self) -> 'Self':
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages'
                )
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        contact_1 = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])
    else:
        print("Valid contact report:")
        print(f"ID: {contact_1.contact_id}")
        print(f"Type: {contact_1.contact_type}")
        print(f"Location; {contact_1.location}")
        print(f"Signal: {contact_1.signal_strength}/10")
        print(f"Duration: {contact_1.duration_minutes} minutes")
        print(f"Witnesses: {contact_1.witness_count}")
        print(f"Message: {contact_1.message_received}")

    print("\n======================================")
    try:
        contact_2 = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])
    else:
        print("Valid contact report:")
        print(f"ID: {contact_2.contact_id}")
        print(f"Type: {contact_2.contact_type}")
        print(f"Location; {contact_2.location}")
        print(f"Signal: {contact_2.signal_strength}/10")
        print(f"Duration: {contact_2.duration_minutes} minutes")
        print(f"Witnesses: {contact_2.witness_count}")
        print(f"Message: {contact_2.message_received}")


if __name__ == "__main__":
    main()
