from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from drone import Drone
    from hub import Hub


class Connection:
    """
    Represents a bidirectional link between two hubs in the network.

    This class manages the transit capacity between hubs and keeps track
    of drones currently traversing the connection.

    Attributes:
        id (str): Unique identifier for the connection.
        hubs (set[Hub]): The two Hub instances connected by this link.
        max_capacity (int): Maximum number of drones
                            allowed on the link at once.
        current_drones (dict[str, Drone]): Collection of drones
                                        currently in transit
    """

    def __init__(self, id: str, hub_a: Hub, hub_b: Hub, max_link: int) -> None:
        """
        Initializes a new Connection instance.

        Args:
            id (str): The unique string identifier for this connection.
            hub_a and hub_b (Hub): The two hubs connected.
            max_link (int): The maximum capacity for this specific connection.
        """
        self.id: str = id
        self.hubs: set[Hub] = {hub_a, hub_b}
        self.max_capacity: int = max_link
        self.current_drones: dict[str, Drone] = {}
