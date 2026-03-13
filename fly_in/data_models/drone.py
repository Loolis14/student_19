from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.hub import Hub
    from data_models.connection import Connection

from collections import deque


class Drone:
    def __init__(self, id: str, start_hub: Hub) -> None:
        self.id: str = id
        self.current_pos: Hub = start_hub
        self.path: deque[Hub | Connection] = deque()
        self.turn_drone = 0
        self.state: list[str] = [self.current_pos.id]

    def _add_path(self, path: list[Hub | Connection]) -> None:
        self.path = deque(path)

    def _wait(self) -> None:
        self.turn_drone += 1

    def _can_move(self) -> bool:
        destination = self.path[0]
        if len(destination.current_drones) == destination.max_capacity:
            return False
        return True

    def _move(self) -> None:
        destination: Hub | Connection = self.path.popleft()
        self.current_pos.current_drones.pop(self.current_pos.id, None)
        destination.current_drones[destination.id] = destination
        self.current_pos = destination
        self.turn_drone += 1
