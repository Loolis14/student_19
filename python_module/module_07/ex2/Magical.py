"""Abstract class for magical card."""

from abc import ABC, abstractmethod


class Magical(ABC):
    """Define a magical class."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on a target."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Store mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Get state of magic."""
        pass
