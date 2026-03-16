from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hub import Hub
    from connection import Connection

from collections import deque


class Drone:
    """
    Represents an autonomous drone within the simulation.

    The drone navigates through the graph using a pre-calculated path
    of hubs and connections, while respecting capacity constraints.

    Attributes:
        id (str): Unique identifier for the drone.
        current_pos (Hub | Connection): The current location of the drone.
        path (deque[Hub | Connection]): A queue representing the remaining
            sequence of locations to visit.
        turn_drone (int): Counter for the number of turns the drone has acted.
        state (list[str]): History of the drone's position IDs for each turn.
    """

    def __init__(self, id: str, start_hub: Hub) -> None:
        """
        Initializes a new Drone instance.

        Args:
            id (str): Unique string identifier for the drone.
            start_hub (Hub): The initial hub where the drone starts.
        """
        self.id: str = id
        self.current_pos: Hub | Connection = start_hub
        self.path: deque[Hub | Connection] = deque()
        self.turn_drone = 0
        self.state: list[str] = [self.current_pos.id]

    def _add_path(self, path: list[Hub | Connection]) -> None:
        """
        Assigns a navigation path to the drone.

        Args:
            path (list[Hub | Connection]): Sequence of hubs and connections
                to follow.
        """
        self.path = deque(path)

    def _wait(self) -> None:
        """
        Increments the drone's turn counter
        without changing its position.
        """
        self.turn_drone += 1

    def _can_move(self) -> bool:
        """
        Checks if the drone can move to the next step in its path.

        Verifies if the next destination has reached its maximum
        drone capacity.

        Returns:
            bool: True if the drone can move, False if the destination is full.
        """
        destination: Hub | Connection = self.path[0]
        if len(destination.current_drones) == destination.max_capacity:
            return False
        return True

    def _move(self) -> None:
        """
        Moves the drone to the next destination in its path.

        Updates the occupation status of both the current and next
        locations, updates the current position, and increments
        the turn counter.
        """
        destination: Hub | Connection = self.path.popleft()
        self.current_pos.current_drones.pop(self.current_pos.id, None)
        destination.current_drones[destination.id] = destination
        self.current_pos = destination
        self.turn_drone += 1
