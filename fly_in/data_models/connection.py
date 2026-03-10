from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.drone import Drone
    from data_models.hub import Hub
# Méthodes utiles : has_capacity(), add_drone_to_transit(),
# process_transit_turn().


class Connection:
    def __init__(self, id: str, hub_a: Hub, hub_b: Hub, max_link: int):
        self.id: str = id
        self.hubs: set = {hub_a, hub_b}
        self.max_capacity: int = max_link
        self.current_drones: dict[str, Drone] = {}

    def get_neighbors(self):  # peut être avoir le hub où il doit aller ?
        return self.hubs - self
