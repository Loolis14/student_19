"""Game engine class."""

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
        """Simulate a turn."""
        enemy = ['Enemy Player']
        result = {
            'strategy': self.strategy.get_strategy_name(),
            'actions': self.strategy.execute_turn(self.hand, enemy)
        }
        self.turn += 1
        self.total_damage = result['actions']['damage_dealt']
        return result

    def get_engine_status(self) -> dict:
        """Get the status of the engine."""
        return {
            'turns_simulated': self.turn,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': len(self.hand)
        }
