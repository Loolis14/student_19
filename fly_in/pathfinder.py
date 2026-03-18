from graph import Graph
from hub import Hub
from connection import Connection
import heapq
from collections import deque
from typing import Optional
import sys


class Pathfinder:
    """Compute optimal paths for drones using flow algorithms.

    This class implements a variation of the Edmonds-Karp algorithm
    with weighted nodes to prioritize certain zones.

    It supports:
        - Capacity constraints on hubs and connections
        - Zone-based traversal costs
        - Extraction of actual paths from the computed flow

    Attributes:
        nb_drones (int): Total number of drones to route.
        hubs (dict[str, Hub]): All hubs in the graph.
        connections (dict[str, Connection]): All connections in the graph.
        start_name (str): Starting hub ID.
        end_name (str): Destination hub ID.
    """

    def __init__(self, graph: Graph) -> None:
        """Initialize the pathfinder with a graph.

        Args:
            graph (Graph): Graph containing hubs, connections, and drones.
        """
        self.nb_drones: int = len(graph.drones)
        self.hubs: dict[str, Hub] = graph.hubs
        self.connections: dict[str, Connection] = graph.connections
        self.start_name: str = graph.start_name
        self.end_name: str = graph.end_name

    def _build_residual_graph(self) -> dict[str, dict[str, int]]:
        """Build the residual graph with node splitting.

        Each hub is split into two nodes (in/out) to enforce capacity
        constraints on nodes. Connections are also modeled with capacities.

        Blocked hubs and connections are ignored.

        Returns:
            dict[str, dict[str, int]]: Residual capacity graph where:
                - Keys are node IDs
                - Values are dicts of neighbor nodes with capacities
        """
        res_cap: dict[str, dict[str, int]] = {}
        for hub_id, hub in self.hubs.items():
            if hub.zone_type == 'blocked':
                continue
            id_in = f'{hub_id}_in'
            id_out = f'{hub_id}_out'

            # Capacity of Hub (Node Splitting)
            res_cap.setdefault(id_in, {})[id_out] = hub.max_capacity
            res_cap.setdefault(id_out, {})[id_in] = 0

        for link_id, link in self.connections.items():
            h1, h2 = list(link.hubs)
            if h1.zone_type == 'blocked' or h2.zone_type == 'blocked':
                continue
            c_in, c_out = f"{link_id}_in", f"{link_id}_out"
            res_cap.setdefault(c_in, {})[c_out] = link.max_capacity
            res_cap.setdefault(c_out, {})[c_in] = 0

            # --- Sens 1 : Hub1 vers Hub2 ---
            res_cap.setdefault(f"{h1.id}_out", {})[c_in] = link.max_capacity
            res_cap.setdefault(c_in, {})[f"{h1.id}_out"] = 0
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
                       ) -> list[tuple[list[str], int]]:
        """Extract paths and associated flow values from the residual graph.

        This method reconstructs actual paths taken by the flow by analyzing
        reverse edges in the residual graph.

        Args:
            res_cap (dict[str, dict[str, int]]): Final residual capacities.
            init_cap (dict[str, dict[str, int]]): Initial capacities.

        Returns:
            list[tuple[list[str], int]]: List of (path, flow) where:
                - path is a list of hub/connection IDs
                - flow is the number of drones assigned to that path
        """
        flow_graph: dict[str, dict[str, int]] = {}
        for u in res_cap:
            for v in res_cap[u]:
                if v in init_cap and u in init_cap[v]:
                    if init_cap[u][v] == 0:
                        flow_sent = res_cap[u][v]
                        if flow_sent > 0:
                            flow_graph.setdefault(v, {})[u] = flow_sent

        paths_with_flow: list[tuple[list[str], int]] = []
        s: str = f"{self.start_name}_out"
        t: str = f"{self.end_name}_in"

        while True:
            queue: deque[tuple[str, int]] = deque([(s, sys.maxsize)])
            visited: dict[str, Optional[str]] = {s: None}
            found_path: bool = False
            bottleneck: int = 0

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

            new_curr: Optional[str] = t
            temp_path: list[str] = []
            while new_curr:
                clean_name = "_".join(new_curr.split('_')[:-1])
                if not temp_path or temp_path[-1] != clean_name:
                    temp_path.append(clean_name)
                prev = visited[new_curr]
                if prev:
                    flow_graph[prev][new_curr] -= bottleneck
                new_curr = prev
            temp_path.reverse()
            paths_with_flow.append((temp_path, bottleneck))
        return paths_with_flow

    def _revisited_edmonds_karp(self) -> tuple[int,
                                               list[tuple[list[str], int]]]:
        """Compute max flow using a modified Edmonds-Karp algorithm.

        This implementation:
            - Uses Dijkstra instead of BFS to account for weighted zones
            - Prioritizes paths through certain hub types
            - Stops early when all drones are routed

        Returns:
            tuple[int, list[tuple[list[str], int]]]:
                - max_flow: Total flow sent (number of drones routed)
                - paths_with_flow: Extracted paths with assigned flow
        """
        res_cap = self._build_residual_graph()
        initial_cap = {u: dict(v) for u, v in res_cap.items()}
        max_flow: int = 0
        parent: dict[str, str] = {}

        def _get_weight(curr_id: str, ngbr_id: str) -> int:
            """Compute traversal cost between two nodes.

            Cost is applied only when crossing a hub (in → out),
            based on zone type:
                - priority: low cost
                - normal: medium cost
                - restricted: high cost

            Args:
                curr_id (str): Current node ID.
                ngbr_id (str): Neighbor node ID.

            Returns:
                int: Traversal cost.
            """
            curr: str = "_".join(curr_id.split('_')[:-1])
            neighbor: str = "_".join(ngbr_id.split('_')[:-1])
            if self.connections.get(curr) or self.connections.get(neighbor):
                return 0
            if "_in" in curr_id and "_out" in ngbr_id and curr == neighbor:
                zone: str = self.hubs[curr].zone_type
                if zone == 'restricted':
                    return 3
                if zone == 'priority':
                    return 1
                return 2
            return 0

        def _dijkstra() -> bool:
            """Find shortest augmenting path using Dijkstra.

            This method searches for a path from source to sink in the residual
            graph while minimizing traversal cost.

            Updates:
                parent (dict[str, str]): Stores the path.

            Returns:
                bool: True if a path to the destination was found,
                    False otherwise.
            """
            start_hub: str = f'{self.start_name}_out'
            queue: list[tuple[int, str]] = [(0, start_hub)]
            min_costs: dict[str, int] = {start_hub: 0}
            parent.clear()
            while queue:
                curr_cost, curr_id = heapq.heappop(queue)
                if curr_id == f'{self.end_name}_in':
                    return True
                if curr_cost > min_costs.get(curr_id, sys.maxsize):
                    continue
                for ngbr_id, capacity in res_cap[curr_id].items():
                    if capacity > 0:
                        weight: int = _get_weight(curr_id, ngbr_id)
                        new_cost = curr_cost + weight
                        if new_cost < min_costs.get(ngbr_id, sys.maxsize):
                            min_costs[ngbr_id] = new_cost
                            parent[ngbr_id] = curr_id
                            heapq.heappush(queue, (new_cost, ngbr_id))
            return False

        while _dijkstra():
            if max_flow >= self.nb_drones:
                break
            path_flow: int = sys.maxsize
            end: str = f"{self.end_name}_in"
            start: str = f"{self.start_name}_out"

            current = end
            while current != start:
                prev: str = parent[current]
                path_flow = min(path_flow, res_cap[prev][current])
                current = prev

            current = end
            while current != start:
                prev = parent[current]
                res_cap[prev][current] -= path_flow
                res_cap[current][prev] += path_flow
                current = prev
            max_flow += path_flow

        paths_with_flow = self._extract_paths(res_cap, initial_cap)
        return max_flow, paths_with_flow
