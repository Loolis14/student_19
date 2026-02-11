#!/usr/bin/env python3

"""Fifth Exercise."""


class InventoryMaster:
    """Manage inventory of players."""

    player_inventory: list["InventoryMaster"] = []
    data: dict[str, tuple[str, str, int]] = {
            "helmet": ("armor", "common", 400),
            "shield": ("armor", "common", 600),
            "potion": ("consommable", "common", 10),
            "elixir_de_temps": ("consommable", "rare", 1000),
            "poison": ("consommable", "uncommon", 100),
            "sword": ("weapon", "common", 500),
            "bow": ("weapon", "uncommon", 750),
            "royal_bow": ("weapon", "rare", 1200),
            }

    def __init__(self, name: str, inventory: dict[str, int]) -> None:
        """Initialize an inventory."""
        self.name: str = name
        self.inventory: dict[str, int] = inventory
        self.gold: int = 0
        self.weight: int = 0
        for item, qty in inventory.items():
            item_datas = InventoryMaster.data[item]
            self.gold += item_datas[2] * qty
            self.weight += qty
        InventoryMaster.player_inventory.append(self)

    def add_items(self, item: str, qty: int) -> None:
        """Get in a certain quantity of an item."""
        datas: tuple[str, str, int] = InventoryMaster.data[item]
        self.gold += datas[2] * qty
        self.weight += qty
        qty_init: int = self.inventory.get(item, 0)
        self.inventory.update({item: qty_init + qty})

    def lose_items(self, item: str, qty: int) -> None:
        """Get off a certain quantity of an item."""
        datas: tuple[str, str, int] = InventoryMaster.data[item]
        self.gold -= datas[2] * qty
        self.inventory[item] -= qty
        self.weight -= qty

    def inside_bag(self) -> None:
        """Give all the player inventory: type, rarity and value and some stats."""
        print(f"=== {self.name}'s inventory ===")
        print(f"All inventory: {self.inventory.keys()}")
        item_type: dict[str, int] = {"weapon": 0, "consommable": 0, "armor": 0}
        for item, nbr in self.inventory.items():
            type, rarity, value = InventoryMaster.data[item]
            item_type[type] += nbr
            print(
                f"{item} ({type}, {rarity}): "
                f"{int(nbr)}x @ {value} gold each = {nbr * value} gold")
        # more stats
        print(f"\nInventory value: {self.gold} gold")
        print(f"Item count: {sum(self.inventory.values())} items")
        print(
            f"Categories: weapon({item_type['weapon']}), "
            f"consumable({item_type['consommable']}), "
            f"armor({item_type['armor']})")

    @classmethod
    def game_stats(cls) -> None:
        """Print some stats on the game."""
        print("=== Inventory Analytics ===")
        richest: dict = {"name": "", "gold": 0}
        weighter: dict = {"name": "", "weight": 0}
        for player in cls.player_inventory:
            if int(player.gold) > richest["gold"]:
                richest["name"] = player.name
                richest["gold"] = player.gold
            if int(player.weight) > weighter["weight"]:
                weighter["name"] = player.name
                weighter["weight"] = player.weight
        print(
            f"Most valuable player: {richest['name']} "
            f"({richest['gold']} gold)")
        print(f"Most items: {weighter['name']} ({weighter['weight']} items)")

    @classmethod
    def rarity_item(cls) -> None:
        """Find rarity item."""
        rare: list[str] = []
        for player in cls.player_inventory:
            for item in player.inventory:
                if cls.data[item][1] == "rare":
                    rare.append(item)
        print(f"Rarest items: {', '.join(rare)}")


def transaction(player1: InventoryMaster, player2: InventoryMaster, item: str, qty: int) -> str:
    """Exchange items."""
    print(f"=== Transaction: {player1.name} "
          f"gives {player2.name} 2 potions ===")
    if player1.inventory[item] < qty:
        return f'Not enough {item} in {player1.name} inventory'
    player1.lose_items(item, qty)
    player2.add_items(item, qty)
    return "Transaction successful!"


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    alice_bag = InventoryMaster(
        'Alice', {'royal_bow': 1, 'potion': 10, 'shield': 1})
    bob_bag = InventoryMaster(
        'Bob', {'sword': 2, 'potion': 2, 'shield': 1})
    alice_bag.inside_bag()
    print()
    InventoryMaster.game_stats()
    InventoryMaster.rarity_item()
    print()
    print(transaction(alice_bag, bob_bag, "potion", 2))
    print("\n=== Updated Inventories ===")
    print(f"{alice_bag.name} potions : {alice_bag.inventory.get('potion')}")
    print(f"{bob_bag.name} potions : {bob_bag.inventory.get('potion')}")
