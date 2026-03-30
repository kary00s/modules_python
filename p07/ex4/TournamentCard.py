
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_value: int = attack
        self.health: int = health
        self.rating: int = rating
        self.win: int = 0
        self.lose: int = 0

    #__Card
    def play(self, game_state: dict) -> dict:
        self.id = game_state["id"]
        # if self.name == "Ice Wizard":
        #     self.rating = 1150
        # else:
        self.rating = self.calculate_rating()
        
        print(f"{self.name} (ID: {self.id})")
        print(f"- Interfaces: [{Card.__name__}," 
              f" {Combatable.__name__},"
              f" {Rankable.__name__}]")
        print(f"- Rating: {self.rating}")
        print("- Record: 0-0\n")

    #_Compatable
    def attack(self, target) -> dict:
        self.win += 10
        return {
            "name": self.name,
            "cost": self.cost,
            "target": target

        }

    def defend(self, incoming_damage: int) -> dict:
        self.lose = incoming_damage
        return {
            "name": self.name,
            "cost": self.cost,
            "incoming_damage": incoming_damage
        }
    def get_combat_stats(self) -> dict:
        pass
    
    #_ Rankable
    def calculate_rating(self) -> int:
        return self.rating
    
    def update_wins(self, wins: int) -> None:
        pass
    def update_losses(self, losses: int) -> None:
        pass
    def get_rank_info(self) -> dict:
        pass