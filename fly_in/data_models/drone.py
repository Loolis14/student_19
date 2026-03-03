# Méthodes utiles : move_to(destination), wait().
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.hub import Hub
    from graph import Graph

from collections import deque


class Drone:
    def __init__(self, id: str, start_hub: Hub):
        self.id: str = id
        self.current_location: Hub = start_hub
        self.path: deque[Hub] = deque()
        self.progression: int = 0
        self.turn_drone = 0

        # a voir ?
        self.state = 0

    def can_move(self) -> bool:
        return True

    def move_to(self) -> None:
        destination = self.path.popleft()
        if destination.zone_type == 'restricted':
            pass  # a voir quoi faire
        else:
            self.current_location = destination
            self.progression -= 1
            self.turn_drone += 1
