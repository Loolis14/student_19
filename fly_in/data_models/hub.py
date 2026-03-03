from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.drone import Drone
    from data_models.connection import Connection
# Méthodes utiles : is_full(), add_drone(), remove_drone().


class Hub:
    def __init__(self, position: str, dict: dict) -> None:
        self.position: str = position
        self.name: str = dict['name']
        self.coord: tuple[int] = (dict['x'], dict['y'])
        self.zone_type: str = dict['zone']
        self.color: str = dict['color']
        self.max_capacity: int = dict['max_drones']
        self.current_drones: dict[str, Drone] = {}

    def get_neighbors(self, connections: list[Connection]) -> list[Hub]:
        neighbors: list[Hub] = []
        for connection in connections:
            if self.name == connection.hub_a.name:
                if connection.hub_b.zone_type == 'blocked':
                    continue
                neighbors.append(connection.hub_b)
            elif self.name == connection.hub_b.name:
                if connection.hub_a.zone_type == 'blocked':
                    continue
                neighbors.append(connection.hub_a)
        return neighbors
