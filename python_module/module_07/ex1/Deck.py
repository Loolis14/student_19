from ex0.Card import Card
from typing import List


class Deck:
    """Manages cards."""

    cards: List[Card] = []

    def add_card(self, card: "Card") -> None:
        Deck.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> "Card":
        pass

    def get_deck_stats(self) -> dict:
        total_cards: int = len(Deck.cards)
        for card in Deck.cards:

"""
Deck stats: {'total_cards': 3,'creatures': 1,'spells': 1,
'artifacts': 1,'avg_cost': 4.0}
"""