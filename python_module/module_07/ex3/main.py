"""Fourth exercise main."""

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def create_factory(factory: FantasyCardFactory, engine: GameEngine) -> None:
    """Create a factory with cards."""
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
    battlefield = ['Enemy Player']
    print(f"Factory: {engine.factory.__class__.__name__}")
    print(f"Strategy: {engine.strategy.get_strategy_name()}")
    print(f'Available types: {my_factory.get_supported_types()}')
    create_factory(my_factory, engine)

    print("\nSimulating aggressive turn...")
    engine.simulate_turn()
    hand = [f"{c.name} ({c.cost})" for c in engine.hand]
    print(f"Hand: {hand}")

    print("\nTurn execution:")
    print(f"Strategy: {engine.strategy.__class__.__name__}")
    print("Actions:", my_strategy.execute_turn(engine.hand, battlefield))

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
