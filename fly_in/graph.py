from drone import Drone
from hub import Hub
from connection import Connection
from collections import deque
from typing import Optional


class Graph:
    """
    Manages the simulation environment, including network topology and drones.

    The Graph class acts as the central data structure, handling the
    initialization of hubs, drone deployment, and the creation of connections
    between nodes based on a provided configuration.

    Attributes:
        drones (dict[str, Drone]): Collection of all drones in the simulation,
            indexed by their ID.
        connections (dict[str, Connection]): Collection of all network links,
            indexed by their ID.
        hubs (dict[str, Hub]): Collection of all hubs in the network,
            indexed by their ID.
        start_name (str): The ID of the designated starting hub.
        end_name (str): The ID of the designated destination hub.
    """

    def __init__(self) -> None:
        """Initializes an empty simulation graph."""
        self.drones: dict[str, Drone] = {}
        self.connections: dict[str, Connection] = {}
        self.hubs: dict[str, Hub] = {}
        self.start_name: str = ''
        self.end_name: str = ''

    def _add_hub(self, config: dict[str, Optional[str | int]],
                 type: str) -> None:
        """
        Creates and registers a new Hub instance in the graph.

        Args:
            config (dict): Configuration data for the hub
                (name, coordinates, type of zone, max drones and the color).
            type (str): The role of the hub ('start_hub', 'end_hub' or 'hub').
        """
        raw_x = config.get('x')
        raw_y = config.get('y')
        raw_max = config.get('max_drones')
        x = int(raw_x) if raw_x else 0
        y = int(raw_y) if raw_y else 0
        max_drones = int(raw_max) if raw_max else 1

        raw_color = config.get('color')
        color = str(raw_color) if raw_color else None

        name = str(config.get('name', 'unknown'))
        zone = str(config.get('zone', 'normal'))

        new_hub: Hub = Hub(name, x, y, zone, color, max_drones)
        self.hubs[name] = new_hub
        match type:
            case 'start_hub':
                self.start_name = name
            case 'end_hub':
                self.end_name = name

    def _add_drones(self, nb_drones: int) -> None:
        """
        Initializes and places drones at the starting hub.

        Args:
            nb_drones (int): Total number of drones to create.
        """
        start_hub: Hub = self.hubs[self.start_name]
        for i in range(nb_drones):
            new_drone: Drone = Drone(f'D{i + 1}', start_hub)
            self.drones[new_drone.id] = new_drone
            self.hubs[start_hub.id].current_drones[new_drone.id] = new_drone

    def _add_connections(self, config: list[tuple[str, str, int]]) -> None:
        """
        Creates network connections between hubs based on configuration.

        Args:
            config (list[tuple[str, str, int]]): A list of tuples containing
                (hub_a_id, hub_b_id, max_capacity).
        """
        i: int = 1
        for tuple_connection in config:
            hub_a_id, hub_b_id, max_capacity = tuple_connection
            hub_a: Hub = self.hubs[hub_a_id]
            hub_b: Hub = self.hubs[hub_b_id]
            new_connection = Connection(f'C{i}', hub_a, hub_b, max_capacity)
            self.connections[f'C{i}'] = new_connection
            i += 1

    def _graph_init(self, config: tuple[int,
                                        dict[str, Optional[str | int]],
                                        dict[str, Optional[str | int]],
                                        list[dict[str, Optional[str | int]]],
                                        list[tuple[str, str, int]]]) -> None:
        """
        Full graph initialization from a configuration dictionary.

        Args:
            config (dict[str, Any]): Complete configuration containing hubs,
                connections, and drone counts.
        """
        nb_drones, start_hub, end_hub, hubs, connection = config
        self._add_hub(start_hub, 'start_hub')
        self._add_hub(end_hub, 'end_hub')
        for hub in hubs:
            self._add_hub(hub, 'hub')
        self._add_drones(nb_drones)
        self._add_connections(connection)
        self.hubs[self.start_name].max_capacity = nb_drones
        self.hubs[self.end_name].max_capacity = nb_drones

    def _add_path_to_drone(self, path: list[Hub]) -> None:
        """
        Assigns a pre-calculated navigation path to all drones in the graph.

        Args:
            path (list[Hub]): A list of Hub objects defining the path.
        """
        for drone in self.drones.values():
            drone.path = deque(path)

    def _str_to_obj(self, path: list[str]) -> list[Hub | Connection]:
        """
        Converts a string-based path into a sequence of objects.

        This method converts IDs into actual Hub and Connection instances,
        specifically handling 'restricted' zones that require one turn
        connection transit.

        Args:
            path (list[str]): List of hub identifiers representing the path.

        Returns:
            list[Hub | Connection]: A list of objects that the drone will
                physically traverse.
        """
        path_in_obj: list[Hub | Connection] = []
        len_path: int = len(path)
        for i in range(0, len_path, 2):
            if path[i] == self.start_name:
                continue
            hub = self.hubs[path[i]]
            if hub.zone_type == 'restricted':
                path_in_obj.append(self.connections[path[i - 1]])
            path_in_obj.append(hub)
        return path_in_obj
