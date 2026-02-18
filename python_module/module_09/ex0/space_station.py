from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone
from typing import Optional
# Pydantic then ensures that any data entering
# that class matches your requirements.

"""
Key Features

    Data Parsing, not just Validation: If you pass the string "123"
    to an int field, Pydantic will automatically convert it for you.
    It doesn't just complain; it helps.

    Detailed Errors: If the data is wrong, it tells you exactly where
    and why (e.g., "Field 'age' must be greater than 0").

    JSON Support: It can instantly export your data models to JSON or
    dictionaries.

    Settings Management: It has a specialized BaseSettings class
    (often used with .env files, similar to your current exercise)
    that automatically reads environment variables into a typed object.

    Gemini a dit

In Pydantic (the library we just discussed), model_validator is the tool you use when you need to check if multiple fields make sense together.

Think of standard validation as checking if a single ingredient is fresh, while a model_validator checks if the whole recipe makes sense.
1. Why "mode='after'"?

Pydantic v2 processes data in stages. When you use mode='after', you are telling Python:

    First: Do the basic checks (Is the ID an integer? Is the Email valid?).

    Then: If the basic checks pass, give me the entire object so I can run my custom logic.

2. Concrete Example: Password Confirmation

Imagine a sign-up form. You have a password and a confirm_password. Individually, they are both valid strings. But they must match.

from pydantic import BaseModel, model_validator

class Signup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'Signup':
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match!")
        return self
    Abréviation,Signification (Anglais),Symbole Mathématique,Signification (Français)
gt,Greater Than,>,Strictement supérieur
ge,Greater or Equal,>=,Supérieur ou égal
lt,Less Than,<,Strictement inférieur
le,Less or Equal,<=,Inférieur ou égal
"""


class SpaceStation(BaseModel):
    station_id: str = Field(gt=3, lt=10)
    name: str = Field(gt=1, lt=50)
    crew_size: int = Field(gt=1, lt=20)
    power_level: float = Field(gt=0.0, lt=100.0)
    oxygen_level: float = Field(gt=0.0, lt=100.0)
    last_maintenance: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, le=200)


def main() -> None:
    try:
        station = SpaceStation(station_id="ic")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
""" • Creates a valid space station instance
• Displays the station information clearly
• Attempts to create an invalid station (e.g., crew_size > 20)
• Shows the validation error message """