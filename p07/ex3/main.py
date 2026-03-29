from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex0.Card import Card


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print(f"Factory: {FantasyCardFactory().__class__.__name__}")
    print(f"Strategy: {AggressiveStrategy().__class__.__name__}")

    factory = FantasyCardFactory()
    factory.available = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    engine = GameEngine()
    engine.hand = ["Fire Dragon (5)", "Goblin Warrior (2)", "Lightning Bolt (3)"]
    print(f"Hand: {engine.simulate_turn()}")

    print("\nTurn execution:")
    print(f"Strategy: {AggressiveStrategy().__class__.__name__}")
    strategy = AggressiveStrategy()

    strategy.action = {
            "cards_played": ["Goblin Warrior", "Lightning Bolt"],
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
            }
    print(f"Acrions: {strategy.execute_turn(None, None)}")

    print("\nGame Report:", end="\n")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
