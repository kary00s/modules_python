from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        id_card: str,
        name: str,
        cost: int,
        rarity: int,
        rating: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.rating = rating
        self.win: int = 0
        self.lose: int = 0
        self.id_card = id_card

    def play(self, game_state: dict) -> dict:
        _ = game_state
        self.rating = self.calculate_rating()
        print(f"{self.name} (ID: {self.id_card})")
        print(
            f"- Interfaces: [{Card.__name__},"
            f" {Combatable.__name__},"
            f" {Rankable.__name__}]"
        )
        print(f"- Rating: {self.rating}")
        print("- Record: 0-0\n")

    def get_card_info(self) -> dict:
        return {
            "id_card": self.id_card,
            "name": self.name,
            "cost": self.cost,
            "rating": self.rating,
        }

    def attack(self, target) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "incoming_damage": incoming_damage,
        }

    def get_combat_stats(self) -> str:
        return "active" if self.stats else "inactive"

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.win += wins
        return self.win

    def update_losses(self, losses: int) -> None:
        self.lose += losses
        return self.lose

    def get_rank_info(self) -> str:
        return f"{self.name} - Rating : {self.rating}"
