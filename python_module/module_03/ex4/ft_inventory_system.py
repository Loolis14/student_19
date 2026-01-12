#!/usr/bin/env python3

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
        for item, qty in inventory:
            self.inventory[item] = qty
        InventoryMaster.player_inventory.append(self)

    def add_items(self, *inventory):
        """get in a certain quantity of an item"""
        for item, qty in inventory:
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
                self.inventory[item] -= qty

    def inside_bag(self):
        """Print all the player inventory: type, rarity and value"""
        print(f"=== {self.name.capitalize()}'s inventory ===")
        for item, nbr in self.inventory.items():
            type, rarity, value = InventoryMaster.data[item]
            print(
                f"{item} ({type}, {rarity}): "
                f"{int(nbr)}x @ {value} gold each = {nbr * value} gold")

    def bag_stats(self):
        """get some stats on the inventory"""
        print(self.inventory.get("sword"))
        # exemple de tests pour la methode get(). A reprendre ici


# valeur de l'inventaire du personnage, combien d'item et les categories
# inventaire analytics


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    alice_bag = InventoryMaster(
        'alice', ('sword', 1), ('potion', 10), ('shield', 1))
    alice_bag.inside_bag()
    alice_bag.bag_stats()
