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
        self.drones_moved_stats: list[int] = []
        self.path_cost: int = 0

    def create_graph(self, config: dict) -> None:
        graph = Graph()
        graph.graph_init_dict_config(config)
        self.graph = graph
        self.drone_in_mouvement = copy(self.graph.drones)  # à voir pour le mettre à un autre moment peut être ?

    def run_simulation(self, path: deque[Hub]) -> None:
        # Si tous les drones ont le même chemin
        for drone in self.drone_in_mouvement.values():
            clean_path = copy(path)
            if clean_path and clean_path[0].name == drone.current_hub.name:
                clean_path.popleft()
            drone.path = clean_path
            drone.progression = len(path)
        while self.drone_in_mouvement:
            self.turn_total += 1
            movements_turn = []
            drone_finished: list[str] = []
            for drone in self.drone_in_mouvement.values():
                if drone.can_move():
                    drone.move_to()
                    self.path_cost += 1
                    movements_turn.append(
                        f'{drone.id}-{drone.current_hub.name}'
                        )
                    if drone.current_hub.name == self.graph.end_name:
                        drone_finished.append(drone.id)
                else:
                    drone.wait()
            print(" ".join(movements_turn), self.turn_total)
            self.drones_moved_stats.append(len(movements_turn))
            for drone_name in drone_finished:
                self.drone_in_mouvement.pop(drone_name, None)

    def _path_cost(self, path: dict) -> int:
        return (sum(2 if self.graph.hubs[p].zone_type == 'restricted' else 1
                    for p in path['path']))

    def _drones_repartition(self, paths: list[dict[str, list | int]]) -> None:
        for path in paths:
            path_cost = self._path_cost(path)
            path['cost'] = path_cost
            path['drones_on_path'] = []
        paths.sort(key=lambda p: p['cost'])
        nb_drones = len(self.graph.drones)
        acc_drones = 1
        while acc_drones <= nb_drones:
            min_path = min(paths, key=lambda x: x['cost'])
            for _ in range(min_path['flow']):
                if acc_drones > nb_drones:
                    break
                min_path['drones_on_path'].append(
                    self.drone_in_mouvement[f'D{acc_drones}'])
                acc_drones += 1
                min_path['cost'] += 1

    def _run_edmonds_karp(self) -> None:
        max_flow, paths = self.graph.edmonds_karp()
        if not paths:
            raise PathError(f"No connection between '{self.graph.start_name}'"
                            f"hub and '{self.graph.end_name}' hub.")
        self._drones_repartition(paths)
        """ a chaque tour :
            - regarder le type de la zone :
                - si restricted: truc specifique: prend le nombre de drone du flow et l'envoie dans la connection
                - si normal: prend le nb de drones du flow dans la liste et l'envoie dans le hub !
            -  """
        acc_zone = 1
        while self.drone_in_mouvement:
            drones_moved = 0
            turn = 0
            while drones_moved < max_flow:
                hub_name = paths[turn]['path'][acc_zone]
                if self.graph.hubs[hub_name].zone_type == 'restricted':
                    print(1)
                else:
                    for _ in range(paths[turn]['flow']):
                        drone_to_move = paths[turn]['drones_on_path'][drones_moved]
                        self.graph.drones[drone_to_move].move_to()
                        """TRANSFERER LES PATHS DANS CHAQUE DRONE PLUTOT QUE DE LES LAISSER EN DICTIONNAIRE !!!!"""
                        break

            print(max_flow)
            print(paths)
            break

    def main(self, config: dict) -> None:
        self.create_graph(config)
        # path: deque = self.graph.bfs_shortest_path()
        # print(self.graph.edmonds_karp())
        # path = self.graph.find_path_dijkstra()
        self._run_edmonds_karp()
        # self.run_simulation(path)
