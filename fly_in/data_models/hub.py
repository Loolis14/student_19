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
        """Si un neighbor == Priority: passe avant les autres ! A AJOUTER"""
        neighbors: list[Hub] = []
        for connection in connections:
            if self in connection.hubs:
                neighbor_set = connection.hubs - {self}
                neighbor: Hub = next(iter(neighbor_set))
                if neighbor.zone_type == 'blocked':
                    continue
                neighbors.append(neighbor)
        return neighbors
