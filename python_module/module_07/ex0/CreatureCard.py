"""Concret class for creature cards."""

from .Card import Card


class CreatureCard(Card):
    """Define a card with a creature."""

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        """Initialize a creature card."""
        super().__init__(name, cost, rarity)
        self._attack: int = attack
        self._health: int = health
        self.mana: int = 6

    @property
    def health(self) -> int:
        """Give access to card's health."""
        return self._health

    @health.setter
    def set_health(self, health: int) -> None:
        """Set heath if condition is aplayble."""
        if health < 0:
            raise ValueError("Health can't be negative.")
        self._health = health

    @property
    def attack(self) -> int:
        """Give access to card's attack."""
        return self._attack

    @attack.setter
    def set_attack(self, attack: int) -> None:
        """Set attack if condition is aplayble."""
        if attack < 0:
            raise ValueError("Attack can't be negative.")
        self._attack = attack

    def play(self, game_state: dict) -> dict:
        """Play a creature card."""
        if not self.is_playable(game_state['mana']):
            return {}
        game_state['mana'] -= self.cost
        game_state['creature'].append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: str) -> dict:
        """Give the stats of the attack."""
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': 7,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        """Get card info."""
        parent: dict = super().get_card_info()
        parent['attack'] = self.attack
        parent['health'] = self.health
        return parent
