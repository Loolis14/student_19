#!/usr/bin/env python3

"""Fourth exercise."""

import sys


if __name__ == "__main__":
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        item, qty = arg.split(":")
        inventory[item] = int(qty)

    print("=== Inventory System Analysis ===")
    total: int = sum(inventory.values())
    print(f'Total items in inventory: {total}')
    print(f'Unique item types: {len(inventory)}')

    print("\n=== Current Inventory ===")
    for item, qty in inventory.items():
        print(f'{item}: {qty} units ({qty / total * 100:.1f}%)')

    print("\n=== Inventory Statistics ===")
    max_ = max(inventory.values())
    min_ = min(inventory.values())
    for item, qty in inventory.items():
        if qty == max_:
            print(f'Most abundant: {item} ({max_} units)')
        if qty == min_:
            print(f'Least abundant: {item} ({min_} unit)')

    print("\n=== Item Categories ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    for item, qty in inventory.items():
        if qty > 3:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print(f'Moderate: {moderate}')
    print(f'Scarce: {scarce}')

    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    for item, qty in inventory.items():
        if qty < 2:
            restock.append(item)
    print(f'Restock needed: {restock}')

    print("\n=== Dictionary Properties Demo ===")
    print(f'Dictionary keys: {list(inventory.keys())}')
    print(f'Dictionary values: {list(inventory.values())}')
    if inventory.get('sword'):
        print("Sample lookup - 'sword' in inventory: True")
    else:
        print("No 'sword' in inventory")
