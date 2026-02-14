from abc import ABC, abstractmethod


class Combatable(ABC):
    """Define a combatable class."""

    @abstractmethod
    def attack(self, target: str) -> dict:
        """Attack a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend vs an attack."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Get the stats of the combat."""
        pass
