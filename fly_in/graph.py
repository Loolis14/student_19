from data_models import Connection, Drone, Hub
# Méthodes utiles : add_zone(), add_connection(),
# get_neighbors(zone), get_connection_between(zone_a, zone_b).


class Graph:

    def __init__(self) -> None:
        self.drones: dict[str, Drone] = {}
        self.connections: list[Connection] = []
        self.hubs: dict[str, Hub] = {}

        """ self.nb_drones: int = config['nb_drones']
        self.connection: list[tuple] = config['connection'] """

    def add_hub(self, config: dict):
        hub_name = config['name']
        new_hub = Hub(hub_name, config)
        self.hubs[hub_name] = new_hub

    def main(self, config: dict) -> None:
        self.add_hub(config['start_hub'])
        self.add_hub(config['end_hub'])
        for hub in config['hub']:
            self.add_hub(hub)
        print(self.hubs)

        for i in range(config['nb_drones']):
            pass
