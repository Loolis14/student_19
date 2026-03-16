from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from drone import Drone
    from connection import Connection


class Hub:
    """
    Represents a transit point (hub) within the logistics network.

    This class manages the physical properties of the hub, its drone
    hosting capacity, and its current occupancy state.

    Attributes:
        id (str): Unique name of the hub.
        coord (tuple[int, int]): Coordinates (x, y).
        zone_type (str): Type of zone.
            'blocked', 'priority', 'normal', 'restricted'.
        color (str): Color for visualization purposes.
        max_capacity (int): Maximum number of drones allowed simultaneously.
        current_drones (dict[str, Drone]): Dictionnary of drones currently at
            the hub, indexed by their ID.
    """

    def __init__(self, dict: dict[str, int | str]) -> None:
        """
        Initializes a new Hub instance using a data dictionary.

        Args:
            data (dict[str, int | str]): Dictionary containing
                hub configuration informations.
        """
        self.id: str = dict['name']
        self.coord: tuple[int] = (dict['x'], dict['y'])
        self.zone_type: str = dict['zone']
        self.color: str = dict['color']
        self.max_capacity: int = dict['max_drones']
        self.current_drones: dict[str, Drone] = {}

    def _get_neighbors(self, connections: list[Connection]) -> list[Hub]:
        """
        Identifies adjacent hubs accessible via the provided connections.
        Filters out neighboring hubs if their zone type is 'blocked'.

        Args:
            connections list[Connection]: A list of all available
                network connections.

        Returns:
            A list of directly connected Hub objects that are not blocked.
        """
        neighbors: list[Hub] = []
        for connection in connections:
            if self in connection.hubs:
                neighbor_set = connection.hubs - {self}
                neighbor: Hub = next(iter(neighbor_set))
                if neighbor.zone_type == 'blocked':
                    continue
                neighbors.append(neighbor)
        return neighbors
