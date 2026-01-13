#!/usr/bin/env python3
# print(self.inventory.get("sword"))
# exemple de tests pour la methode get(). A ecrire dans le carnet !

class InventoryMaster:
    player_inventory = []
    data = {
            "helmet": ("armor", "common", 400),
            "shield": ("armor", "common", 600),
            "potion": ("consommable", "common", 10),
            "elixir_de_temps": ("consommable", "rare", 1000),
            "poison": ("consommable", "uncommon", 100),
            "sword": ("weapon", "common", 500),
            "bow": ("weapon", "uncommon", 750),
            "royal_bow": ("weapon", "rare", 1200),
            }

    def __init__(self, name, *inventory):
        """Inventory initalisation"""
        self.name = name
        self.inventory = {}
        self.gold = 0
        self.weight = 0
        for item, qty in inventory:
            self.inventory[item] = qty
            datas = InventoryMaster.data[item]
            self.gold += datas[2] * qty
            self.weight += qty
        InventoryMaster.player_inventory.append(self)

    def add_items(self, *inventory):
        """get in a certain quantity of an item"""
        for item, qty in inventory:
            datas = InventoryMaster.data[item]
            self.gold += datas[2] * qty
            self.weight += qty
            if item in self.inventory:
                self.inventory[item] += qty
            else:
                self.inventory[item] = qty

    def lose_items(self, *inventory):
        """get off a certain quantity of an item"""
        for item, qty in inventory:
            if self.inventory[item] < qty:
                return f'Not enough {item} in {self.name} inventory'
            else:
                datas = InventoryMaster.data[item]
                self.gold -= datas[2] * qty
                self.inventory[item] -= qty
                self.weight -= qty

    def inside_bag(self):
        """All the player inventory: type, rarity and value and some stats"""
        print(f"=== {self.name.capitalize()}'s inventory ===")
        item_type = {"weapon": 0, "consommable": 0, "armor": 0}
        for item, nbr in self.inventory.items():
            type, rarity, value = InventoryMaster.data[item]
            item_type[type] += nbr
            print(
                f"{item} ({type}, {rarity}): "
                f"{int(nbr)}x @ {value} gold each = {nbr * value} gold")
        # more stats
        print(f"\nInventory value: {self.gold} gold")
        print(f"Item count: {self.weight} items")
        print(
            f"Categories: weapon({item_type['weapon']}), "
            f"consumable({item_type['consommable']}), "
            f"armor({item_type['armor']})")

    @classmethod
    def game_stats(cls):
        """To print some stats on the game"""
        print("=== Inventory Analytics ===")
        richest = {"name": "", "gold": 0}
        weighter = {"name": "", "weight": 0}
        for player in cls.player_inventory:
            if int(player.gold) > richest["gold"]:
                richest["name"] = player.name.capitalize()
                richest["gold"] = player.gold
            if int(player.weight) > weighter["weight"]:
                weighter["name"] = player.name.capitalize()
                weighter["weight"] = player.weight
        print(
            f"Most valuable player: {richest['name']} "
            f"({richest['gold']} gold)")
        print(f"Most items: {weighter['name']} ({weighter['weight']} items)")

    @classmethod
    def rarity_item(cls):
        rare = []
        for player in cls.player_inventory:
            for item in player.inventory:
                if cls.data[item][1] == "rare":
                    rare.append(item)
        print(f"Rarest items: {rare}")


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    alice_bag = InventoryMaster(
        'alice', ('royal_bow', 1), ('potion', 10), ('shield', 1))
    bob_bag = InventoryMaster(
        'bob', ('sword', 2), ('potion', 2), ('shield', 1))
    alice_bag.inside_bag()
    InventoryMaster.game_stats()
    InventoryMaster.rarity_item()
