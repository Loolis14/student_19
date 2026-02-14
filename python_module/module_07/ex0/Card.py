#!/usr/bin/env python3

from abc import abstractmethod, ABC
from enum import Enum


class Card(ABC):
    """Define a base card."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a card."""
        self.name = name
        self.cost = cost
        self.rarity = rarity.value

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the turn."""
        pass

    def get_card_info(self) -> dict:
        """Gives card info."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        """Return if a card is playable."""
        return available_mana >= self.cost


class Rarity(Enum):
    """Enumerate rarity card."""

    LEGENDARY = "legendary"
    COMMON = "common"
