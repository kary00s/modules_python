def player_creator(achievements, name):
    print(f"Player {name} achievements: {achievements}")


def unique_achievement(charlie_achiev, alice_achiev, bob_achiev):
    unique_achievement = set.union(charlie_achiev, alice_achiev, bob_achiev)
    print(f"All unique achievements: {unique_achievement}")
    print(f"Total unique achievements: {len(unique_achievement)}\n")


def common_achievement(alice_achiev, charlie_achiev, bob_achiev):
    common_achievement = set.intersection(
        alice_achiev, charlie_achiev, bob_achiev
    )
    print(f"Common to all players: {common_achievement}")


def rare_achievements(alice_achiev, bob_achiev, charlie_achiev):

    alice_difference = set.difference(alice_achiev, bob_achiev, charlie_achiev)
    bob_difference = set.difference(bob_achiev, alice_achiev, charlie_achiev)
    charlie_difference = set.difference(charlie_achiev, bob_achiev,
                                        alice_achiev)

    rare = set.union(alice_difference, bob_difference, charlie_difference)
    print(f"Rare achievements (1 player): {rare}\n")


def players_stat(alice_achiev, bob_achiev):
    common_achiev = set.intersection(alice_achiev, bob_achiev)
    alice_unique = alice_achiev.difference(common_achiev)
    bob_unique = bob_achiev.difference(common_achiev)
    print(f"Alice vs Bob common: {common_achiev}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


def main():
    print("=== Achievement Tracker System ===\n")
    alice_achievements = {
        "first_kill",
        "speed_demon",
        "level_10",
        "treasure_hunter",
    }
    player_creator(alice_achievements, "alice")
    bob_achievements = {
        "boss_slayer",
        "collector",
        "first_kill",
        "level_10",
    }
    player_creator(bob_achievements, "bob")
    charlie_achievements = {
        "level_10",
        "speed_demon",
        "perfectionist",
        "treasure_hunter",
        "boss_slayer",
    }
    player_creator(charlie_achievements, "charlie")
    print("\n=== Achievement Analytics ===")
    unique_achievement(charlie_achievements,
                       alice_achievements,
                       bob_achievements)
    common_achievement(charlie_achievements,
                       alice_achievements,
                       bob_achievements)
    rare_achievements(alice_achievements,
                      bob_achievements,
                      charlie_achievements)
    players_stat(alice_achievements, bob_achievements)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
