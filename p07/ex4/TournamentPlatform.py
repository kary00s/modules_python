from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.stats = True
        self.match = 1
        self.cards = {}

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.id_card] = card
        return card.id_card

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            card1 = self.cards[card1_id]
            card2 = self.cards[card2_id]

            return {
                "winner": card1.name,
                "loser": card2.name,
                "winner_rating": card1.rating,
                "loser_rating": card2.rating,
            }
        except KeyError:
            print(f"the card with id: {card1_id} does not exist")

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        avg = sum([card.rating for card in self.cards.values()])
        avg = avg / len(self.cards)
        status = TournamentCard.get_combat_stats(self)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.match,
            "avg_rating": avg,
            "platform_status": status,
        }
