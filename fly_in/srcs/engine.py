# Le chef d'orchestre qui fait avancer le temps tour par tour et génère
# l'output attendu (D1-roof1 D2-corridorA).

# Attributs : network (Graph), drones (list[Drone]), turn_count (int).

# Méthodes utiles : run(), execute_turn(), print_state()
# (pour gérer l'output console avec les couleurs demandées).
from data_models.graph import Graph
from data_models import Drone, Hub, Connection
from srcs.pathfinder import Pathfinder


class PathError(Exception):
    pass


class Engine:

    def __init__(self) -> None:
        self.turn_total: int = 0
        self.graph: Graph = None
        self.drone_not_arrived: dict[str, Drone] = {}
        self.drones_moved_stats: list[int] = []
        self.path_cost: int = 0
        self.rek: Pathfinder = None
        self.paths: list[dict[str, list[Hub | Connection] | int]] = []
        self.max_flow: int = 0

    def _create_graph(self, config: dict) -> None:
        graph = Graph()
        graph.graph_init_dict_config(config)
        self.graph = graph

    def _create_pathfinder(self, graph: Graph) -> None:
        rek = Pathfinder(graph)
        self.rek = rek

    def run_bfs(self, path: list[Hub]) -> None:
        self.graph.add_path_to_drone(path)
        self.drone_not_arrived = {n: d for n, d in self.graph.drones.items()}
        while self.drone_not_arrived:
            self.turn_total += 1
            movements_turn = []
            drones_arrived = []
            for drone_name, drone in self.drone_not_arrived.items():
                if drone.can_move():
                    drone.move_to()
                    self.path_cost += 1
                    movements_turn.append(
                        f'{drone_name}-{drone.current_hub.name}'
                        )
                    if drone.current_hub.name == self.graph.end_name:
                        drones_arrived.append(drone_name)
                else:
                    drone.wait()
            print(" ".join(movements_turn), self.turn_total)
            self.drones_moved_stats.append(len(movements_turn))
            for drone_name in drones_arrived:
                self.drone_not_arrived.pop(drone_name)

    def add_weight(self) -> None:
        for path in self.paths:
            path['weight'] = len(path['path'])

    def drones_spread(self) -> None:
        """Drones spread."""
        self.drone_not_arrived = {n: d for n, d in self.graph.drones.items()}
        self.add_weight()
        for drone in self.drone_not_arrived.values():
            min_path = min(self.paths, key=lambda p: p['weight'])
            drone.add_path(min_path)
            min_path['weight'] += 1

    def _paths_str_to_obj(self,
                          paths: list[dict[str, list[str] | int]]) -> None:
        """Transform str name in object."""
        for path_dict in paths:
            path_in_hub = self.graph.str_to_obj(path_dict['path'])
            path_dict['path'] = path_in_hub
            self.paths.append(path_dict)

    def run_simulation(self) -> None:
        while self.drone_not_arrived:
            self.turn_total += 1
            movements_turn = []
            drones_arrived = []
            for drone_name, drone in self.drone_not_arrived.items():
                if drone.can_move():
                    drone.move_to()
                    self.path_cost += 1
                    movements_turn.append(
                        f'{drone_name}-{drone.current_hub.name}'
                        )
                    if drone.current_hub.name == self.graph.end_name:
                        drones_arrived.append(drone_name)
                else:
                    drone.wait()
            print(" ".join(movements_turn), self.turn_total)
            self.drones_moved_stats.append(len(movements_turn))
            for drone_name in drones_arrived:
                self.drone_not_arrived.pop(drone_name)

    def main(self, config: dict) -> None:
        self._create_graph(config)
        if len(self.graph.drones) == 0:
            print('Mais que faire ??')
        self._create_pathfinder(self.graph)
        max_flow, paths = self.rek.revisited_edmonds_karp()
        if not paths:
            raise PathError(f"No connection between '{self.graph.start_name}'"
                            f"hub and '{self.graph.end_name}' hub.")
        self.max_flow = max_flow
        self._paths_str_to_obj(paths)
        self.drones_spread()
        self.run_simulation()
        # déplacer les drones et afficher le message
