from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        super().__init__()
        self.available = None

    def create_creature(self, name_or_power=None):
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Epic", 6, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    def create_spell(self, name_or_power=None):
        return SpellCard("Lightning Bolt", 3, "Rare", None)

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 1, "Rare", 3, "Gain mana")

    def create_themed_deck(self, size: int) -> dict:
        result = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell(),
        ]
        return {"deck": result, "size": len(result)}

    def get_supported_types(self) -> dict:

        return self.available
