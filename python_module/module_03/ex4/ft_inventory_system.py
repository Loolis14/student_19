#!/usr/bin/env python3

class InventoryMaster:
    player_inventory = []

    def __init__(self, name, *inventory):
        self.name = name
        self.inventory = {}
        for item, qty in inventory:
            self.inventory[item] = qty
        InventoryMaster.player_inventory.append(self)

    def add_items(self, *inventory):
        for item, qty in inventory:
            if item in self.inventory:
                self.inventory[item] += qty
            else:
                self.inventory[item] = qty

    def lose_items(self, *inventory):
        for item, qty in inventory:
            if self.inventory[item] < qty:
                return f'Not enough {item} in {self.name} inventory'
            else:
                self.inventory[item] -= qty


if __name__ == "__main__":
    print("=== Player Inventory System ===")
    alice_inventory = InventoryMaster(
        'alice', ('sword', 1), ('potion', 10), ('shield', 1))
    print(alice_inventory.inventory)
    alice_inventory.add_items(('potion', 10))
    print(alice_inventory.inventory)
    alice_inventory.lose_items(('potion', 10))
    print(alice_inventory.inventory)
