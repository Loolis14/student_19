# Méthodes utiles : move_to(destination), wait().
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.hub import Hub
    from data_models.graph import Graph

from collections import deque


class Drone:
    def __init__(self, id: str, start_hub: Hub):
        self.id: str = id
        self.current_hub: Hub = start_hub
        self.path: deque[Hub] = deque()
        self.flow: int = 0
        self.progression: int = 0
        self.turn_drone = 0

        # a voir ?
        self.state = 0

    def wait(self):
        self.turn_drone += 1

    def can_move(self) -> bool:
        destination = self.path[0]
        if destination.zone_type == 'restricted':
            pass  # a voir quoi faire
        else:
            if len(destination.current_drones) == destination.max_capacity:
                return False
        return True

    def move_to(self) -> None:
        destination = self.path.popleft()
        current_hub = self.current_hub
        if destination.zone_type == 'restricted':
            pass  # a voir quoi faire
        else:
            current_hub.current_drones.pop(self.id, None)
            self.current_hub = destination
            destination.current_drones[self.id] = self
            self.progression -= 1
            self.turn_drone += 1

    def move(self, graph: Graph) -> None:
        destination = graph.hubs[self.path.popleft()]
        if destination.zone_type == 'restricted':
            pass  # a voir quoi faire peut etre ajouter la connection dans le pass ?
        else:
            self.current_hub.current_drones.pop(self.id, None)
            self.current_hub = destination
            destination.current_drones[self.id] = self
            self.progression -= 1
            self.turn_drone += 1
