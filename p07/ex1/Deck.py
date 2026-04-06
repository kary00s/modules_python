import random
from typing import Dict, List, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        spells = sum(1 for c in self.cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.cards if isinstance(c, ArtifactCard))
        creatures = sum(1 for c in self.cards if isinstance(c, CreatureCard))
        cost = 7
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": cost,
        }
