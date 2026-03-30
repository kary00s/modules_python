from ex4.TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):
        self.match = None
        self.card = {}

    def register_card(self, card: TournamentCard) -> str:
        self.card += card
        return self.card[id]
        
    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.card[card1_id]
        card2 = self.card[card2_id]

        # card1.
    def get_leaderboard(self) -> list:
        pass
    def generate_tournament_report(self) -> dict:
        pass
