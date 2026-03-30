from typing import Any, Dict

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def deck_creator() -> Deck:
    deck = Deck()

    creature_deck = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell_deck = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    artifact_deck = ArtifactCard("Mana Crystal", 2,
                                 "Uncommon", 3, "+1 mana per turn")

    deck.add_card(creature_deck)
    deck.add_card(spell_deck)
    deck.add_card(artifact_deck)
    deck.shuffle()
    return deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = deck_creator()
    deck_stats = deck.get_deck_stats()
    print(f"Deck stats: {deck_stats}\n")
    print("Drawing and playing cards:")
    for _ in range(deck_stats.get("total_cards", 0)):
        card = deck.draw_card()
        card_type = "Card"
        if isinstance(card, CreatureCard):
            card_type = "Creature"
        if isinstance(card, SpellCard):
            card_type = "spell"
        if isinstance(card, ArtifactCard):
            card_type = "Artifact"
        print(f"Drew: {card.name} ({card_type})")
        play_result: Dict[str, Any] = card.play({})
        print(f"Play result: {play_result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
