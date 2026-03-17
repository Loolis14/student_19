from graph import Graph
from drone import Drone
from hub import Hub
from connection import Connection
from pathfinder import Pathfinder
from simulation import Simulation
from typing import Optional


class PathError(Exception):
    pass


class Path:
    def __init__(self, path: list[Hub | Connection], flow: int) -> None:
        self.path: list[Hub | Connection] = path
        self.flow: int = flow
        self.weight: int = len(path)


class Engine:

    def __init__(self) -> None:
        self.turn_total: int = 0
        self.total_path_cost: int = 0
        self.total_moved: int = 0
        self.drones_in_mouvement: list[Drone] = []
        self.drones_at_start: list[Drone] = []
        self.paths: list[Path] = []
        self.max_flow: int = 0

    def _create_graph(self, config: tuple[int,
                                          dict[str, Optional[str | int]],
                                          dict[str, Optional[str | int]],
                                          list[dict[str, Optional[str | int]]],
                                          list[tuple[str, str, int]]]) -> None:
        graph = Graph()
        graph._graph_init(config)
        self.graph: Graph = graph

    def _paths_str_to_obj(self,
                          paths_l: list[tuple[list[str], int]]) -> None:
        """Transform str name in object."""
        for path_tuple in paths_l:
            path, flow = path_tuple
            path_in_hub: list[Hub | Connection] = self.graph._str_to_obj(path)
            path_objet: Path = Path(path_in_hub, flow)
            self.paths.append(path_objet)

    def _drones_in_movement(self) -> list[Drone]:
        drone_moved: list[Drone] = []
        self.drones_in_mouvement.sort(key=lambda d: len(d.path))
        for drone in self.drones_in_mouvement:
            if drone._can_move():
                drone._move()
                drone_moved.append(drone)
            else:
                drone._wait()
        return drone_moved

    def _drones_at_start(self) -> list[Drone]:
        drones_moved: list[Drone] = []
        while len(drones_moved) < self.max_flow:
            if not self.drones_at_start:
                break
            min_path: Path = min(self.paths, key=lambda p: p.weight)
            for i in range(1, min_path.flow + 1):
                if not self.drones_at_start:
                    break
                drone = self.drones_at_start.pop()
                drone._add_path(min_path.path)
                self.total_path_cost += len(drone.path)
                if drone._can_move():
                    self.drones_in_mouvement.append(drone)
                    drone._move()
                    drones_moved.append(drone)
                    min_path.weight += 1
                else:
                    drone._wait()
        for drone in self.drones_at_start:
            if drone not in drones_moved:
                drone._wait()
        return drones_moved

    def _drones_turn_state(self, simulation: Simulation) -> None:
        for drone in self.graph.drones.values():
            drone.state.append(drone.current_pos.id)
            if drone.current_pos.__class__.__name__ == 'Connection':
                simulation.connections_used.append(drone.current_pos)

    def _run_turns(self, simulation: Simulation) -> None:
        self.drones_at_start = [d for d in self.graph.drones.values()]
        while self.drones_in_mouvement or self.drones_at_start:
            self.turn_total += 1
            movements_turn: list[str] = []
            drone_moved: list[Drone] = self._drones_in_movement()
            drone_moved += self._drones_at_start()
            for drone in drone_moved:
                movements_turn.append(f'{drone.id}-{drone.current_pos.id}')
                if drone.current_pos.id == self.graph.end_name:
                    if drone in self.drones_in_mouvement:
                        self.drones_in_mouvement.remove(drone)
            self.total_moved += len(drone_moved)
            self._drones_turn_state(simulation)
            print(f'Tour {self.turn_total}:', " ".join(movements_turn))
        simulation.turn_total = self.turn_total

    def _stats(self) -> None:
        drones = self.graph.drones
        acc_turn_drone: int = sum(d.turn_drone for d in drones.values())
        average = acc_turn_drone / len(drones)
        efficiency = self.total_moved // self.turn_total

        print('\n=== Additionnal evaluation metrics ===')
        print(f'Efficiency of path allocation: {efficiency} '
              'drones per tour in average')
        print(f'Average number of turns per drone: {average:.2f}')
        print('Total path cost:', self.total_path_cost)

    def main(self, config: tuple[int,
                                 dict[str, Optional[str | int]],
                                 dict[str, Optional[str | int]],
                                 list[dict[str, Optional[str | int]]],
                                 list[tuple[str, str, int]]]) -> None:
        self._create_graph(config)
        if len(self.graph.drones) == 0:
            print('No drone registered, no simulation needed.')
        else:
            rek = Pathfinder(self.graph)
            max_flow, paths = rek._revisited_edmonds_karp()
            if not paths:
                raise PathError("No connection between "
                                f"'{self.graph.start_name}' "
                                f"hub and '{self.graph.end_name}' hub.")
            simulation = Simulation(self.graph)
            self.max_flow = max_flow
            self._paths_str_to_obj(paths)
            self._run_turns(simulation)
            self._stats()
            simulation.interface_control()
