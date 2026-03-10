from data_models import Connection, Drone, Hub
from collections import deque
from typing import Optional
# Méthodes utiles :
# get_neighbors(zone), get_connection_between(zone_a, zone_b).


class Graph:

    def __init__(self) -> None:
        self.drones: dict[str, Drone] = {}
        self.connections: list[Connection] = []
        self.start_name: str = ''
        self.end_name: str = ''
        self.hubs: dict[str, Hub] = {}

    def add_hub(self, config: dict, type: str) -> None:
        hub_name = config['name']
        new_hub = Hub(hub_name, config)
        self.hubs[hub_name] = new_hub
        match type:
            case 'start_hub':
                self.start_name = hub_name
            case 'end_hub':
                self.end_name = hub_name

    def add_drones(self, nb_drones: int) -> None:
        start_hub = self.hubs[self.start_name]
        for i in range(nb_drones):
            new_drone = Drone(f'D{i + 1}', start_hub)
            self.drones[new_drone.id] = new_drone
            self.hubs[start_hub.name].current_drones[new_drone.id] = new_drone

    def add_connections(self, config: list[tuple[Hub, Hub, int]]) -> None:
        i = 1
        for tuple_connection in config:
            hub_a_name, hub_b_name, max_capacity = tuple_connection
            hub_a = self.hubs[hub_a_name]
            hub_b = self.hubs[hub_b_name]
            new_connection = Connection(f'C{i}', hub_a, hub_b, max_capacity)
            i += 1
            self.connections.append(new_connection)

    def graph_init_dict_config(self, config: dict) -> None:
        self.add_hub(config['start_hub'], 'start_hub')
        self.add_hub(config['end_hub'], 'end_hub')
        for hub in config['hub']:
            self.add_hub(hub, 'hub')
        self.add_drones(config['nb_drones'])
        self.add_connections(config['connection'])
        self.hubs[self.start_name].max_capacity = config['nb_drones']
        self.hubs[self.end_name].max_capacity = config['nb_drones']

    def bfs_shortest_path(self) -> Optional[list[Hub]]:
        start_hub = self.hubs[self.start_name]
        queu: deque[tuple[Hub, list[Hub]]] = deque([(start_hub, [start_hub])])
        visited: set[str] = {self.start_name}
        new_path = []

        while queu:
            current_hub, path = queu.popleft()
            if current_hub.name == self.end_name:
                return path
            for neighbor in current_hub.get_neighbors(self.connections):
                if neighbor.name not in visited:
                    visited.add(neighbor.name)
                    new_path.append(neighbor)
                    queu.append((neighbor, new_path))
        return None

    def add_path_to_drone(self, path: list[Hub]) -> None:
        for drone in self.drones.values():
            drone.path = deque(path)
