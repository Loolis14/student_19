from data_models.drone import Drone
# Méthodes utiles : is_full(), add_drone(), remove_drone().


class Hub:
    def __init__(self, position: str, dict: dict) -> None:
        self.position: str = position
        self.name: str = dict['name']
        self.coord: tuple[int] = (dict['x'], dict['y'])
        self.zone_type: str = dict['zone']
        self.color: str = dict['color']
        self.max_drones: int = dict['max_drones']
        self.current_drones: list['Drone'] = []
