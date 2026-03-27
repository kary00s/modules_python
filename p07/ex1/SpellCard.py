from typing import Any, Dict, List
from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        description = self.get_effect()
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": description,
        }

    def resolve_effect(self, targets: List[Any]) -> Dict[str, Any]:
        target_names = [getattr(t, "name", str(t)) for t in targets]
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": target_names,
        }

    def get_effect(self) -> str:
        if self.effect_type == "damage":
            return f"Deal {self.cost} damage to target"
        if self.effect_type == "heal":
            return f"Heal {self.cost} health on target"
        if self.effect_type == "buff":
            return "Buff target creature"
        if self.effect_type == "debuff":
            return "Debuff target creature"
        return "Apply mysterious magic effect"
