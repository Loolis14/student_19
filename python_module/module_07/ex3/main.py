from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def create_factory(factory: FantasyCardFactory, engine: GameEngine) -> None:
    factory.create_creature("dragon")
    factory.create_creature("goblin")
    factory.create_spell('lightning')
    engine.hand = factory.cards


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")
    engine = GameEngine()

    print("\nConfiguring Fantasy Card Game...")
    my_factory = FantasyCardFactory()
    my_strategy = AggressiveStrategy()
    engine.configure_engine(my_factory, my_strategy)
    battlefield = []  # a ecrire
    status: dict = engine.get_engine_status()
    print(f"Factory: {status['Factory']}")
    print(f"Strategy: {status['Strategy']}")

    print("Configuring Fantasy Card Game...")
    print(f'Available types: {my_factory.get_supported_types()}')
    create_factory(my_factory, engine)

    print("\nSimulating aggressive turn...")
    hand = []
    for card in my_factory.cards:
        hand.append(f'{card.name} ({card.cost})')
    print(f'Hand: {hand}')

    print("\nTurn execution:")
    print(f"Strategy: {engine.strategy.__class__.__name__}")
    # print(engine.simulate_turn())
    print(engine.hand)

"""
Simulating aggressive turn...
Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]
Turn execution:
Strategy: AggressiveStrategy
Actions: {'cards_played': ['Goblin Warrior'
,
'Lightning Bolt'],
'mana_used': 5,'targets_attacked': ['Enemy Player'],
'damage_dealt': 8}
Game Report:
{'turns_simulated': 1,'strategy_used': 'AggressiveStrategy'
,
'total_damage': 8,'cards_created': 3}
Abstract Factory + Strategy Pattern: Maximum flexibility achieved!
"""
