# Méthodes utiles : move_to(destination), wait().
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.hub import Hub
    from data_models.graph import Graph
    from data_models.connection import Connection

from collections import deque


class Drone:
    def __init__(self, id: str, start_hub: Hub):
        self.id: str = id
        self.current_hub: Hub = start_hub
        self.path: deque[Hub] = deque()
        self.progression: int = 0
        self.turn_drone = 0

        # a voir ?
        self.state = 0

    def add_path(self, path: list[Hub | Connection]):
        self.path = deque(path)

    def wait(self):
        self.turn_drone += 1

    def can_move(self) -> bool:
        destination = self.path[0]
        if len(destination.current_drones) == destination.max_capacity:
            return False
        return True

    def move_to(self) -> None:
        destination = self.path.popleft()
        current_hub = self.current_hub
        current_hub.current_drones.pop(self.id, None)
        self.current_hub = destination
        destination.current_drones[self.id] = self
        self.progression -= 1
        self.turn_drone += 1

    def move(self, graph: Graph) -> None:
        destination = graph.hubs[self.path.popleft()]
        self.current_hub.current_drones.pop(self.id, None)
        self.current_hub = destination
        destination.current_drones[self.id] = self
        self.progression -= 1
        self.turn_drone += 1
