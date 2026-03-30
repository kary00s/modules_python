from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform_data = TournamentPlatform()

    fire_dragon = TournamentCard("dragon_001", "Fire Dragon", 5, 7, 1200)
    Ice_Wizard = TournamentCard("wizard_001", "Ice Wizard", 5, 7, 1150)

    fire_dragon.play(fire_dragon.get_card_info())
    Ice_Wizard.play(Ice_Wizard.get_card_info())

    platform_data.register_card(Ice_Wizard)
    platform_data.register_card(fire_dragon)

    print("Creating tournament match...")
    print("Match result: ",
          platform_data.create_match("dragon_001", "wizard_001"))

    print("\nTournament Leaderboard:")
    print(f"1. {fire_dragon.get_rank_info()} (1-0)")
    print(f"2. {Ice_Wizard.get_rank_info()} (0-1)")

    print("\nPlatform Report:")
    print(platform_data.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
