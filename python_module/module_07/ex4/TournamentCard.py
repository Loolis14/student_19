"""Tournament card."""

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    """Tracks tournament performance with ranking updates."""

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 health: int, attack_: int, defense: int,
                 id_: str, rating: int):
        """Initialize cards for tournament."""
        super().__init__(name, cost, rarity)
        self._health = health
        self.attack_ = attack_
        self.defense = defense
        self.mana = 6
        self.id = id_
        self.record = {'win': 0, 'lose': 0}
        self.rating = rating

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
        """Attack stats."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_,
            'combat_type': 'melee'
        }

    def calculate_rating(self) -> int:
        """Calculate the rating."""
        return 16 * self.record['win'] - 16 * self.record['lose']

    def get_tournament_stats(self) -> dict:
        """Get tournament stats."""
        return {
            'id': self.id,
            'record': self.record,
            'rating': self.rating
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend vs an attack."""
        damage_taken = (incoming_damage - self.defense
                        if incoming_damage - self.defense > 0 else 0)
        alive = True if damage_taken < self.health else False
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.defense,
            'still_alive': alive
        }

    def get_combat_stats(self) -> dict:
        """Get the stats of the combat."""
        return {
            'attacker': self.name,
            'attack': self.attack_,
            'defend': self.defense
        }

    def update_wins(self, wins: int) -> None:
        """Update rating when winning."""
        self.record['win'] += wins
        self.rating += self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        """Update rating when losing."""
        self.record['lose'] += losses
        self.rating += self.calculate_rating()

    def get_rank_info(self) -> dict:
        """Get rank info."""
        return {
            'name': self.name,
            'rating': self.rating,
            'score': self.record
        }
