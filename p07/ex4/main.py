from ex4.TournamentCard import TournamentCard 
from ex4.TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform_data = TournamentPlatform()
    
    game_state = {
        "name": "Fire Dragon",
        "id": "dragon_001"
    }
    fire_dragon = TournamentCard("Fire Dragon", "Lege5, ndary", 7, 5, 1200)
    fire_dragon.play(game_state)
    platform_data.register_card(fire_dragon)

    game_state = {
        "name": "Ice Wizard",
        "id": "wizard_001"
    }
    Ice_Wizard = TournamentCard("Ice Wizard", 5, "Legendary", 7, 5, 1150)
    Ice_Wizard.play(game_state)
    platform_data.register_card(Ice_Wizard)

    print("Creating tournament match...")


main()