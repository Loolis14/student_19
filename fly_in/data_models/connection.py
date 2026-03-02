from data_models.hub import Hub
# Méthodes utiles : has_capacity(), add_drone_to_transit(),
# process_transit_turn().


class Connection:
    def __init__(self, hub_a: 'Hub', hub_b: 'Hub', max_link: int):
        self.hub_a: 'Hub' = hub_a
        self.hub_b: 'Hub' = hub_b
        self.max_link_capacity: int = max_link
        self.drones_in_transit: dict = {}
