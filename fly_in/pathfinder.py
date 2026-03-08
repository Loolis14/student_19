from graph import Graph


class Pathfinder:

    def __init__(self, graph: Graph):
        self.graph = graph

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
