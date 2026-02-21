"""Concret class for elite card."""

from ex0.Card import Card, Rarity
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    """Generate an elite card."""

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 health: int, defense: int, attack_: int, mana: int) -> None:
        """Initialize an elite card."""
        super().__init__(name, cost, rarity)
        self.health = health
        self.defense = defense
        self.attack_ = attack_
        self.mana = mana
        self.magic = {'Fireball': 4}

    def play(self, game_state: dict) -> dict:
        """Play a turn."""
        if not self.is_playable(game_state['mana']):
            return {}
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
        }

    def attack(self, target: str) -> dict:
        """Attack a target."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_,
            'combat_type': 'melee'
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell."""
        self.mana -= self.magic[spell_name]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.magic[spell_name]
        }

    def channel_mana(self, amount: int) -> dict:
        """Return the mana used and the mana left."""
        return {
            'channeled': amount,
            'total_mana': self.mana + amount
        }

    def defend(self, incoming_damage) -> dict:
        """Return the result of the attack."""
        damage_taken = (incoming_damage - self.defense
                        if incoming_damage - self.defense > 0 else 0)
        alive = True if damage_taken < self.health else False
        return {
            'defender': 'Arcane Warrior',
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': alive
        }

    def get_combat_stats(self) -> dict:
        """Get the stats of the combat."""
        return {
            'attacker': self.name,
            'damage': self.attack_,
            'combat_type': 'melee'
        }

    def get_magic_stats(self) -> dict:
        """Get state of magic."""
        return {
            'mana': self.mana,
            'magic cards': self.magic
        }
