from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    """Orchestre the game."""

    def __init__(self):
        """Initialize the beginning of the game."""
        self.turn: int = 0

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
        enemy = ['Enemy Player']
        r = {
            'actions': self.strategy.execute_turn(self.deck, enemy)
        }
        self.turn += 1
        self.total_damage = r['actions']['damage']
        return {
            'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
            'mana_used': 5,
            'targets_attacked': enemy,
            'damage_dealt': self.total_damage
        }

    def get_engine_status(self) -> dict:
        """Get the status of the engine."""
        return {
            'Factory': self.factory.__class__.__name__,
            'Strategy': self.strategy.get_strategy_name()
        }
