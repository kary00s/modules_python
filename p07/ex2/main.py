from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def main():
    print("=== DataDeck Ability System ===")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    # attack_power=5, defense=3, mana_pool=8
    # defend(5): blocked=min(3,5)=3, taken=5-3=2  ✓
    # cast_spell 2 targets: mana_used=4, pool: 8-4=4
    # channel_mana(3): pool: 4+3=7                ✓
    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 8)

    print(f"\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    class _Target:
        def __init__(self, name): self.name = name

    enemy  = _Target("Enemy")
    print(f"Attack result: {warrior.attack(enemy)}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    e1, e2 = _Target("Enemy1"), _Target("Enemy2")
    print(f"Spell cast: {warrior.cast_spell('Fireball', [e1, e2])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
    print("How do multiple interfaces enable flexible card design?")
    print("What are the advantages of separating combat and magic concerns")


if __name__ == "__main__":
    main()