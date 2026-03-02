# Méthodes utiles : move_to(destination), wait().
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_models.hub import Hub


class Drone:
    def __init__(self, id: str, start: 'Hub'):
        self.id: str = id
        self.current_location: 'Hub' = start

        # a voir ?
        self.state = 0
        self.path = ''
        self.turn_total = 0
