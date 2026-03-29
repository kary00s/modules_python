from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        super().__init__()
        self.action: dict = None

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        _ = hand
        _ = battlefield
        return self.action

    def get_strategy_name(self) -> str:
        strategy_name = "AggressiveStrategy"
        return strategy_name

    def prioritize_targets(self, available_targets: list) -> list:
        enemy = ["Enemy Player"]
        return enemy
