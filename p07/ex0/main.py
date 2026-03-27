from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info(), "\n")

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    play_result = dragon.play({})
    print(f"Play result: {play_result}\n")

    name_target = "Goblin Warrior"
    print("Fire Dragon attacks Goblin Warrior:")
    attack_result = dragon.attack_target(name_target)
    print(f"Attack result: {attack_result}", "\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
