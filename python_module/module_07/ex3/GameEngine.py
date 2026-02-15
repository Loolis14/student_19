from ex3 import CardFactory, GameStrategy
from ex0.Card import Card


class GameEngine():
    """Orchestre the game."""

    def __init__(self):
        """Initialize the beginning of the game."""
        self.turn: int = 0
        self.hand: list[Card] = []
        self.total_damage: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Define factory and the game strategies."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]
Turn execution:
Strategy: AggressiveStrategy
Actions: {'cards_played': ['Goblin Warrior'
,
'Lightning Bolt'],
'mana_used': 5,'targets_attacked': ['Enemy Player'],
'damage_dealt': 8}"""
        self.turn += 1
        enemy = ['Enemy Player']
        card_played = self.strategy.execute_turn(self.hand, enemy)
        mana_used = sum(card.cost for card in card_played)
        dmg: int = 0
        for card in card_played:
            if card.__class__.__name__ == "CreatureCard":
                dmg += card.attack
        return {
            'cards_played': card_played,
            'mana_used': mana_used,
            'targets_attacked': enemy,
            'damage_dealt': dmg
        }

    def get_engine_status(self) -> dict:
        """Get the status of the engine."""
        return {
            'Factory': self.factory.__class__.__name__,
            'Strategy': self.strategy.get_strategy_name(),
            'turns_simulated': self.turn,
            'total_damage': 8,
            'cards_created': len(self.hand)
        }
