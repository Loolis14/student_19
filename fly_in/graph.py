from data_models import Connection, Drone, Hub
from collections import deque
from typing import Optional, Any
import heapq
from copy import deepcopy
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

    def bfs_shortest_path(self) -> Optional[deque[Hub]]:
        start_hub = self.hubs[self.start_name]
        queu: deque[tuple[Hub, list[Hub]]] = deque([(start_hub, [start_hub])])
        visited: set[str] = {self.start_name}
        new_path = []

        while queu:
            current_hub, path = queu.popleft()
            if current_hub.name == self.end_name:
                return deque(path)
            for neighbor in current_hub.get_neighbors(self.connections):
                if neighbor.name not in visited:
                    visited.add(neighbor.name)
                    new_path.append(neighbor)
                    queu.append((neighbor, new_path))
        return None

    def find_path_dijkstra(self) -> Optional[list]:
        start_hub = self.hubs[self.start_name]
        queue = [(0, id(start_hub), start_hub, [start_hub])]
        min_costs: dict = {self.start_name: 0}
        while queue:
            current_cost, _, current_hub, path = heapq.heappop(queue)
            if current_hub.name == self.end_name:
                return path
            if current_cost > min_costs.get(current_hub.name, float('inf')):
                continue
            for neighbor in current_hub.get_neighbors(self.connections):
                weight = 2 if neighbor.zone_type == 'restricted' else 1
                new_cost = current_cost + weight
                if new_cost < min_costs.get(neighbor.name, float('inf')):
                    min_costs[neighbor.name] = new_cost
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, id(neighbor),
                                           neighbor, new_path))
        return None

    def build_residual_graph(self) -> dict[str, dict[str, int]]:
        res_cap = {}
        for hub_name, hub in self.hubs.items():
            name_in = f'{hub_name}_in'
            name_out = f'{hub_name}_out'

            # Capacity of Hub (Node Splitting)
            res_cap.setdefault(name_in, {})[name_out] = hub.max_capacity
            res_cap.setdefault(name_out, {})[name_in] = 0

        # links
        for link in self.connections:
            hub1, hub2 = list(link.hubs)

            h1_in = f'{hub1.name}_in'
            h1_out = f'{hub1.name}_out'
            h2_in = f'{hub2.name}_in'
            h2_out = f'{hub2.name}_out'

            res_cap.setdefault(h1_out, {})[h2_in] = link.max_capacity
            res_cap.setdefault(h2_in, {})[h1_out] = 0

            res_cap.setdefault(h2_out, {})[h1_in] = link.max_capacity
            res_cap.setdefault(h1_in, {})[h2_out] = 0
        return res_cap

    def extract_paths(self, res_cap: dict[str, dict[str, int]],
                      init_cap: dict[str, dict[str, int]]) -> list[dict[str, list, str, int]]:
        flow_graph = {}
        for u in init_cap:
            for v, cap in init_cap[u].items():
                actual_flow = cap - res_cap[u][v]
                if actual_flow > 0:
                    flow_graph.setdefault(u, {})[v] = actual_flow
        print(flow_graph)

        paths_with_flow: list[dict[str, Any]] = []
        s: str = f"{self.start_name}_out"
        t: str = f"{self.end_name}_in"

        while True:
            stack = [(s, float('inf'))]
            visited = {s: None}
            found_path = False
            bottleneck = float('inf')

            while stack:
                curr, curr_flow = stack.pop()
                if curr == t:
                    bottleneck = curr_flow
                    found_path = True
                    break
                for neighbor, flow in flow_graph.get(curr, {}).items():
                    if flow > 0 and neighbor not in visited:
                        visited[neighbor] = curr
                        stack.append((neighbor, min(curr_flow, flow)))
            if not found_path:
                break

            curr = t
            temp_path = []
            while curr:
                clean_name = "_".join(curr.split('_')[:-1])
                if not temp_path or temp_path[-1] != clean_name:
                    temp_path.append(clean_name)
                prev = visited[curr]
                if prev:
                    flow_graph[prev][curr] -= bottleneck
                curr = prev
            temp_path.reverse()
            paths_with_flow.append({'path': temp_path, 'flow': bottleneck})
        return paths_with_flow

    def edmonds_karp(self) -> dict:
        res_cap = self.build_residual_graph()
        initial_cap = {u: dict(neighbors) for u, neighbors in res_cap.items()}
        max_flow = 0
        parent: dict = {}

        def bfs() -> bool:
            visited = {f'{self.start_name}_out'}
            queue = deque([f'{self.start_name}_out'])
            parent.clear()
            while queue:
                curr_hub_name = queue.popleft()
                for neighbor_name, capacity in res_cap[curr_hub_name].items():
                    if neighbor_name not in visited and capacity > 0:
                        parent[neighbor_name] = curr_hub_name
                        visited.add(neighbor_name)
                        if neighbor_name == f'{self.end_name}_in':
                            return True
                        queue.append(neighbor_name)
            return False

        while bfs():
            path_flow = float('inf')
            end = f"{self.end_name}_in"
            start = f"{self.start_name}_out"

            current = end
            while current != start:
                prev = parent[current]
                path_flow = min(path_flow, res_cap[prev][current])
                current = prev

            current = end
            while current != start:
                prev = parent[current]
                res_cap[prev][current] -= path_flow
                res_cap[current][prev] += path_flow
                current = prev
            max_flow += path_flow
            print(max_flow)
        paths = self.extract_paths(res_cap, initial_cap)
        return paths
