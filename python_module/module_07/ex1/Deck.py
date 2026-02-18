"""Define decks."""

from ex0.Card import Card
from typing import List
import random


class Deck:
    """Manages cards."""

    def __init__(self) -> None:
        """Give a list of card in the deck."""
        self.cards: List[Card] = []

    def add_card(self, card: "Card") -> None:
        """Add a card to deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card to deck."""
        for card in self.cards:
            if card.name == card_name:
                return self.cards.remove(card)
        return False

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> "Card":
        """Pick a card."""
        return self.cards[0]

    def get_deck_stats(self) -> dict:
        """Give deck stats."""
        total_cards: int = len(self.cards)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        sum_cost: int = 0
        for card in self.cards:
            sum_cost += card.cost
            if card.__class__.__name__ == "CreatureCard":
                creatures += 1
            elif card.__class__.__name__ == "SpellCard":
                spells += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1
        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': f"{sum_cost / total_cards:.2f}"
        }
