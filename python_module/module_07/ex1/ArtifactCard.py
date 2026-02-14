from ex0.Card import Card


class ArtifactCard(Card):
    """Define an artifact who can influence on board."""

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        """Initiliaze artifact card."""
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        """Play the card."""
        if not self.is_playable(game_state['mana']):
            return {}
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        """Return is ability is available."""
        pass
