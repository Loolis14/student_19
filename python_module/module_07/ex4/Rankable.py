"""Rankable abstract class."""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """Ranks players."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update rating score if win."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update rating score if lose."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Get rank info."""
        pass
