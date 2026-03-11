from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.drone import Drone
    from data_models.hub import Hub


class Connection:
    def __init__(self, id: str, hub_a: Hub, hub_b: Hub, max_link: int) -> None:
        self.id: str = id
        self.hubs: set[Hub] = {hub_a, hub_b}
        self.max_capacity: int = max_link
        self.current_drones: dict[str, Drone] = {}
