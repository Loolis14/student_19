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
        """
        Deck stats: {'total_cards': 3,'creatures': 1,'spells': 1,
        'artifacts': 1,'avg_cost': 4.0}
        """
        total_cards: int = len(Deck.cards)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        sum_cost: int = 0
        for card in Deck.cards:
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
            'avg_cost': sum_cost / total_cards
        }
