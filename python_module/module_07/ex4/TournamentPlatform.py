from ex0 import Card
from ex4 import TournamentCard


class TournamentPlatform():
    """Manages the plateform tournament."""

    def __init__(self) -> None:
        self.cards: dict[str, Card] = {}

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id] = card
        return (f"{card.name} (ID: {card.id}):\n"
                f"- Interfaces: [Card, Combatable, Rankable]\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.record['win']}-{card.record['lose']}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        return {
            'winner': 'dragon_001',
            'loser': 'wizard_001',
            'winner_rating': 1216,
            'loser_rating': 1134
            }

    def get_leaderboard(self) -> list:
        """Get the leaderboard of the tournament."""
        leaderboard: list[tuple] = []
        for card in self.cards.values():
            leaderboard.append((card.name, card.rating,
                                card.record['win'], card.record['lose']))
        return leaderboard

    def generate_tournament_report(self) -> dict:
        pass
