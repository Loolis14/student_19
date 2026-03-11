from data_models.graph import Graph
from data_models import Hub, Connection
import heapq
from collections import deque


class Pathfinder:

    def __init__(self, graph: Graph):
        self.hubs: dict[str, Hub] = graph.hubs
        self.connections: dict[str, Connection] = graph.connections
        self.start_name: str = graph.start_name
        self.end_name: str = graph.end_name

    def _build_residual_graph(self) -> dict[str, dict[str, int]]:
        res_cap = {}
        for hub_id, hub in self.hubs.items():
            id_in = f'{hub_id}_in'
            id_out = f'{hub_id}_out'

            # Capacity of Hub (Node Splitting)
            res_cap.setdefault(id_in, {})[id_out] = hub.max_capacity
            res_cap.setdefault(id_out, {})[id_in] = 0

        for link_id, link in self.connections.items():
            c_in, c_out = f"{link_id}_in", f"{link_id}_out"
            res_cap.setdefault(c_in, {})[c_out] = link.max_capacity
            res_cap.setdefault(c_out, {})[c_in] = 0

            h1, h2 = list(link.hubs)

            # --- Sens 1 : Hub1 vers Hub2 ---
            # Sortie Hub1 -> Entrée Conn
            res_cap.setdefault(f"{h1.id}_out", {})[c_in] = link.max_capacity
            res_cap.setdefault(c_in, {})[f"{h1.id}_out"] = 0
            # Sortie Conn -> Entrée Hub2
            res_cap.setdefault(c_out, {})[f"{h2.id}_in"] = link.max_capacity
            res_cap.setdefault(f"{h2.id}_in", {})[c_out] = 0

            # --- Sens 2 : Hub2 vers Hub1 ---
            res_cap.setdefault(f"{h2.id}_out", {})[c_in] = link.max_capacity
            res_cap.setdefault(c_in, {})[f"{h2.id}_out"] = 0
            res_cap.setdefault(c_out, {})[f"{h1.id}_in"] = link.max_capacity
            res_cap.setdefault(f"{h1.id}_in", {})[c_out] = 0

        return res_cap

    def _extract_paths(self, res_cap: dict[str, dict[str, int]],
                       init_cap: dict[str, dict[str, int]]
                       ) -> list[dict[str, list[str] | int]]:
        flow_graph = {}
        for u in res_cap:
            for v in res_cap[u]:
                if v in init_cap and u in init_cap[v]:
                    if init_cap[u][v] == 0:
                        flow_sent = res_cap[u][v]
                        if flow_sent > 0:
                            flow_graph.setdefault(v, {})[u] = flow_sent

        paths_with_flow: list[dict[str, list[str] | int]] = []
        s: str = f"{self.start_name}_out"
        t: str = f"{self.end_name}_in"

        while True:
            queue = deque([(s, float('inf'))])
            visited = {s: None}
            found_path = False
            bottleneck = 0

            while queue:
                curr, curr_flow = queue.popleft()
                if curr == t:
                    bottleneck = curr_flow
                    found_path = True
                    break
                for neighbor, flow in flow_graph.get(curr, {}).items():
                    if flow > 0 and neighbor not in visited:
                        visited[neighbor] = curr
                        queue.append((neighbor, min(curr_flow, flow)))
            if not found_path or bottleneck == 0:
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

    def _revisited_edmonds_karp(self) -> dict:
        res_cap = self._build_residual_graph()
        initial_cap = {u: dict(v) for u, v in res_cap.items()}
        max_flow = 0
        parent: dict = {}

        def _get_weight(curr_id: str, ngbr_id: str) -> int:
            """Get the zone weight if a cross in hub is made (in -> out)."""
            curr = "_".join(curr_id.split('_')[:-1])
            neighbor = "_".join(ngbr_id.split('_')[:-1])
            if self.connections.get(curr) or self.connections.get(curr):
                return 0
            """ for c in self.connections:
                if c.id == curr or c.id == neighbor:
                    return 0 """
            if "_in" in curr_id and "_out" in ngbr_id and curr == neighbor:
                zone = self.hubs[curr].zone_type
                if zone == 'restricted':
                    return 3
                if zone == 'priority':
                    return 1
                return 2
            return 0

        def _dijkstra() -> bool:
            start_hub = f'{self.start_name}_out'
            queue = [(0, start_hub)]
            min_costs: dict = {start_hub: 0}
            parent.clear()
            while queue:
                curr_cost, curr_id = heapq.heappop(queue)
                if curr_id == f'{self.end_name}_in':
                    return True
                if curr_cost > min_costs.get(curr_id, float('inf')):
                    continue
                for ngbr_id, capacity in res_cap[curr_id].items():
                    if capacity > 0:
                        weight: int = _get_weight(curr_id, ngbr_id)
                        new_cost = curr_cost + weight
                        if new_cost < min_costs.get(ngbr_id, float('inf')):
                            min_costs[ngbr_id] = new_cost
                            parent[ngbr_id] = curr_id
                            heapq.heappush(queue, (new_cost, ngbr_id))
            return False

        while _dijkstra():
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
        paths = self._extract_paths(res_cap, initial_cap)
        return max_flow, paths
