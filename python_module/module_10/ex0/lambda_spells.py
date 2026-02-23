#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '*' + spell + '*', spells))


def mage_stats(mages: list[dict]) -> dict:
    powerful = max(mages, key=lambda mage: mage["power"])
    powerless = min(mages, key=lambda mage: mage["power"])
    average = sum(map(lambda mage: mage["power"], mages)) / len(mages)
    return {
        'max_power': powerful,
        'min_power': powerless,
        'avg_power': average
    }


def test() -> None:
    print("Testing artifact sorter...")
    artifacts = [{'name': 'Earth Shield', 'power': 119, 'type': 'armor'},
                 {'name': 'Earth Shield', 'power': 119, 'type': 'accessory'},
                 {'name': 'Water Chalice', 'power': 98, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 115, 'type': 'relic'}]
    sort = artifact_sorter(artifacts)
    print(
        " comes before ".join(f'{s["name"]} '
                              f'({s["power"]} power)' for s in sort)
        )

    print("Testing power filter...")
    mages = [{'name': 'Kai', 'power': 97, 'element': 'shadow'},
             {'name': 'Luna', 'power': 95, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 79, 'element': 'wind'},
             {'name': 'Ember', 'power': 65, 'element': 'earth'},
             {'name': 'Luna', 'power': 88, 'element': 'shadow'}]
    filter = power_filter(mages, 80)
    print(", ".join(f'{f["name"]} ({f["power"]} power)' for f in filter))

    print("Testing spell transformer...")
    spells = ['lightning', 'earthquake', 'freeze', 'flash']
    print(" ".join(spell_transformer(spells)))

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(", ".join(f'{key}: {value}' for key, value in stats.items()))


if __name__ == "__main__":
    test()
