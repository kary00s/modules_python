from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine():
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.total_simulation = 0
        self.hand = None

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.total_simulation += 1
        return self.hand

    def get_engine_status(self) -> dict:
        damage = self.total_simulation * 4
        cards = len(self.hand)
        return {
            "turns_simulated": self.total_simulation,
            "strategy_used": self.strategy,
            "total_damage": damage,
            "cards_created": cards
        }