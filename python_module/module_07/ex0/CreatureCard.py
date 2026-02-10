#!/usr/bin/env python3

from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack: int = attack
        self._health: int = health
        self.mana: int = 6

    @property
    def health(self):
        return self._health

    @health.setter
    def set_health(self, health):
        if health < 0:
            raise ValueError("Health can't be negative.")
        self._health = health

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def set_attack(self, attack):
        if attack < 0:
            raise ValueError("Attack can't be negative.")
        self._attack = attack

    def play(self, game_state: dict) -> dict:
        if game_state['mana_used'] > self.mana:
            raise 'Not enough mana'
        self.mana -= game_state['mana_used']
        return game_state

    def attack_target(self, target) -> dict:
        attack: dict = {}
        attack['attacker'] = self.name
        attack['target'] = target
        attack['damage_dealt'] = 7
        attack['combat_resolved'] = True
        return attack

    def get_card_info(self) -> dict:
        parent: dict = super().get_card_info()
        parent['attack'] = self.attack
        parent['health'] = self.health
        return parent
