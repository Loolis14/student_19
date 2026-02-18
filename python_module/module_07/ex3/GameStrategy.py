"""Game strategy abstract class."""

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Define the game strategy."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Exectue a turn."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get the strategy name."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Priorize target."""
        pass
