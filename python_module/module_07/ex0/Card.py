#!/usr/bin/env python3

from abc import abstractmethod, ABC
from enum import Enum
"""Mettre la valeur de mana en enum ?"""


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = Rarity(rarity)

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.name.capitalize()
            }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost


class Rarity(Enum):
    LEGENDARY = "legendary"
    COMMON = 2
