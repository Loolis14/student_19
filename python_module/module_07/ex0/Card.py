#!/usr/bin/env python3

from abc import abstractmethod, ABC

"""Mettre la valeur de mana en enum ?"""


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info: dict = {}
        info['name'] = self.name
        info['cost'] = self.cost
        info['rarity'] = self.rarity
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana > 5:
            return True
        return False
