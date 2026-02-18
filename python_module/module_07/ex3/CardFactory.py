"""Abstract class for card factory."""

from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Create cards."""

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        """Create a creature."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        """Create a spell."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        """Create an artifact."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Get supported types."""
        pass
