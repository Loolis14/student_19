# Le chef d'orchestre qui fait avancer le temps tour par tour et génère
# l'output attendu (D1-roof1 D2-corridorA).

# Attributs : network (Graph), drones (list[Drone]), turn_count (int).

# Méthodes utiles : run(), execute_turn(), print_state()
# (pour gérer l'output console avec les couleurs demandées).
from graph import Graph
from data_models import Drone, Hub
from collections import deque
from copy import copy


class PathError(Exception):
    pass


class Engine:

    def __init__(self) -> None:
        self.turn_total: int = 0
        self.graph: Graph = None
        self.drone_in_mouvement: dict[str, Drone] = {}

    def create_graph(self, config: dict) -> None:
        graph = Graph()
        graph.graph_init_dict_config(config)
        self.graph = graph
        self.drone_in_mouvement = self.graph.drones  # à voir pour le mettre à un autre moment peut être ?

    def run_simulation(self, path: deque[Hub]) -> None:
        # Si tous les drones ont le même chemin
        for drone in self.drone_in_mouvement.values():
            drone.path = copy(path)
            drone.progression = len(path)
        while self.drone_in_mouvement:
            self.turn_total += 1
            movements_turn = []
            drone_finished: list[str] = []
            for drone in self.drone_in_mouvement.values():
                if drone.can_move():
                    drone.move_to()
                    movements_turn.append(drone)
                    if drone.current_location.name == self.graph.end_name:
                        drone_finished.append(drone.id)
            for drone_name in drone_finished:
                self.drone_in_mouvement.pop(drone_name, None)

    def main(self, config: dict) -> None:
        self.create_graph(config)
        path: deque = self.graph.find_first_path()
        if not path:
            raise PathError(f"No connection between '{self.graph.start_name}' "
                            f"hub and '{self.graph.end_name}' hub.")
        self.run_simulation(path)
