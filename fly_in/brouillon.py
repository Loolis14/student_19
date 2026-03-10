from data_models.graph import Graph
from collections import deque


class Pathfinder:

    def __init__(self, graph: Graph):
        self.graph: Graph = graph

    def _path_cost(self, path: dict) -> int:
        return (sum(2 if self.graph.hubs[p].zone_type == 'restricted' else 1
                    for p in path['path']))

    def _drones_repartition(self, paths: list[dict[str, list | int]]) -> None:
        for path in paths:
            path_cost = self._path_cost(path)
            path['cost'] = path_cost
        paths.sort(key=lambda p: p['cost'])
        nb_drones = len(self.graph.drones)
        acc_drones = 1
        while acc_drones <= nb_drones:
            min_path = min(paths, key=lambda x: x['cost'])
            for _ in range(int(min_path['flow'])):
                if acc_drones > nb_drones:
                    break
                self.graph.drones[f'D{acc_drones}'].path = deque(min_path['path'][1:])
                self.graph.drones[f'D{acc_drones}'].flow = min_path['flow']
                self.drone_in_mouvement.add(self.graph.drones[f'D{acc_drones}'])
                acc_drones += 1
                min_path['cost'] += 1

    def _run_edmonds_karp(self) -> None:
        max_flow, paths = self.graph.edmonds_karp()
        self._drones_repartition(paths)
        for n, d in self.graph.drones.items():
            print('drone',d.id)
            print('path', d.path)
            print('flow',d.flow)
            print(max_flow)
        while self.drone_in_mouvement:
            self.turn_total += 1
            movements_turn = []
            for drone_name, drone in self.graph.drones.items():
                if drone.can_move(self.graph):
                    drone.move(self.graph)
                    self.path_cost += 1
                    movements_turn.append(
                        f'{drone_name}-{drone.current_hub.name}'
                        )
                    if drone.current_hub.name == self.graph.end_name:
                        self.drone_in_mouvement.remove(drone)
                else:
                    drone.wait()
            print(" ".join(movements_turn), self.turn_total)
            self.drones_moved_stats.append(len(movements_turn))

        """while self.drone_in_mouvement:
            drones_moved = 0
            while drones_moved < max_flow:
                first_pack_drone = self.graph.drones[f'D{drones_moved + 1}']
                for _ in range(first_pack_drone.flow):
                    drone_to_move = self.graph.drones[f'D{drones_moved + 1}']
                    print()
                    print('drone a bouger: ',drone_to_move.id)
                    print()
                    drone_to_move.move(self.graph)
                    drones_moved += 1
                    if drone_to_move.current_hub.name == self.graph.end_name:
                        self.drone_in_mouvement.remove(drone_to_move)
                if drones_moved == max_flow:
                    self.turn_total += 1
                print('drones restants: ',self.drone_in_mouvement)
        print('Tours totaux: ',self.turn_total)"""

    def build_residual_graph(self) -> dict[str, dict[str, int]]:
        res_cap = {}
        for hub_name, hub in self.hubs.items():
            name_in = f'{hub_name}_in'
            name_out = f'{hub_name}_out'

            # Capacity of Hub (Node Splitting)
            res_cap.setdefault(name_in, {})[name_out] = hub.max_capacity
            res_cap.setdefault(name_out, {})[name_in] = 0

        # links a faire !
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
        paths = self.extract_paths(res_cap, initial_cap)
        return max_flow, paths

    """
    # AUTRE ALGO

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
    """
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