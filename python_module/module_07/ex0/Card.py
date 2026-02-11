#!/usr/bin/env python3

from abc import abstractmethod, ABC
from enum import Enum


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity.value

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost


class Rarity(Enum):
    LEGENDARY = "legendary"
    COMMON = "common"
