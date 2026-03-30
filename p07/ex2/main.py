from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 8)

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    enemy = "Enemy"
    print(f"Attack result: {warrior.attack(enemy)}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    e1, e2 = "Enemy1", "Enemy2"
    print(f"Spell cast: {warrior.cast_spell('Fireball', [e1, e2])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
