from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    """Tracks tournament performance with ranking updates."""

    def __init__(self, name, cost, rarity,
                 health, attack_, defense, id_, rating):
        super().__init__(name, cost, rarity)
        self._health: int = health
        self.attack_: int = attack_
        self.defense: int = defense
        self.mana: int = 6
        self.id = id_
        self.record = {'win': 0, 'lose': 0}
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state['mana']):
            return {}
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_,
            'combat_type': 'melee'
        }

    def calculate_rating(self) -> int:
        return 16 * self.record['win'] - 16 * self.record['lose']

    def get_tournament_stats(self) -> dict:
        pass

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
        self.record['win'] += wins
        self.rating += self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.record['lose'] += losses
        self.rating += self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'score': self.record
        }
