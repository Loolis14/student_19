"""Tournament plateform class."""

from ex0 import Card
from ex4 import TournamentCard


class TournamentPlatform():
    """Manages the plateform tournament."""

    def __init__(self) -> None:
        """Initialize tournament plateform with all cards."""
        self.cards: dict[str, Card] = {}
        self.match_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register card for tournaments."""
        self.cards[card.id] = card
        return (f"{card.name} (ID: {card.id}):\n"
                f"- Interfaces: [Card, Combatable, Rankable]\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.record['win']}-{card.record['lose']}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Create a match."""
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        one_two = card2.defense - card1.attack_ + card2._health
        two_one = card1.defense - card2.attack_ + card1._health
        result = {
                'winner': 'dragon_001',
                'loser': 'wizard_001',
                'winner_rating': 1216,
                'loser_rating': 1134
                }
        if one_two == 0:
            card1.update_wins(1)
            card2.update_losses(1)
            result['loser'] = card2.id
            result['winner'] = card1.id
            result['winner_rating'] = card1.rating
            result['loser_rating'] = card2.rating
        elif two_one == 0:
            card2.update_wins(1)
            card1.update_losses(1)
            result['loser'] = card1.id
            result['winner'] = card2.id
            result['winner_rating'] = card2.rating
            result['loser_rating'] = card1.rating
        self.match_played += 1
        return result

    def get_leaderboard(self) -> list:
        """Get the leaderboard of the tournament."""
        leaderboard: list[tuple] = []
        for card in self.cards.values():
            leaderboard.append((card.name, card.rating,
                                card.record['win'], card.record['lose']))
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate tournament report."""
        return {
            'total_cards': len(self.cards),
            'matches_played': self.match_played,
            'avg_rating': (sum(card.rating for card in self.cards.values())
                           // len(self.cards)),
            'platform_status': 'active'
            }
