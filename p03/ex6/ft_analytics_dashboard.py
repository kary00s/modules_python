def main() -> None:
    players = ["alice", "bob", "charlie", "diana", "bob", "eve", "alice"]
    scores = [2300, 1800, 2150, 4600, 1200, 900, 2300]
    regions = ["north", "east", "central", "north", "south", "east", "north"]
    achievements = [
        ("alice", "first_kill"),
        ("alice", "level_10"),
        ("alice", "boss_slayer"),
        ("bob", "first_kill"),
        ("bob", "level_5"),
        ("charlie", "boss_slayer"),
        ("charlie", "level_10"),
        ("charlie", "first_kill"),
        ("charlie", "100_kills"),
        ("diana", "level_10"),
        ("diana", "boss_slayer"),
        ("eve", "first_kill")
    ]

    player_scores = dict(zip(players, scores))
    player_achievements = {}
    for player, ach in achievements:
        if player not in player_achievements:
            player_achievements[player] = set()
        player_achievements[player].add(ach)

    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")

    high_scorers = [p for p, s in player_scores.items() if s >= 2000]
    print("High scorers (≥2000):", sorted(high_scorers))

    doubled_scores = [score * 2 for score in scores]
    print("Scores doubled           :", doubled_scores[:5], "...")

    active_players = [p for p in players if p in player_achievements]
    print("Players with achievements:", sorted(set(active_players)))

    north_players = [p for p, r in zip(players, regions) if r == "north"]
    print("Players from north       :", sorted(set(north_players)))
    print()

    print("=== Dict Comprehension Examples ===")
    score_map = {p: s for p, s in zip(players, scores)}
    print("Player scores:", score_map)

    score_category = {
        "high":   sum(1 for s in scores if s >= 2000),
        "medium": sum(1 for s in scores if 1000 <= s < 2000),
        "low":    sum(1 for s in scores if s < 1000)
    }
    print("Score distribution:", score_category)

    ach_count = {player: len(achs) for
                 player, achs in player_achievements.items()}
    print("Achievement counts   :", ach_count)

    last_region = {p: r for p, r in zip(players, regions)}
    print("Last known region    :", last_region)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    print("Unique players          :", sorted(unique_players))

    unique_achievements = {ach for _, ach in achievements}
    print("Unique achievements     :", sorted(unique_achievements))

    unique_regions = {r for r in regions}
    print("Active regions          :", sorted(unique_regions))

    high_score_players = {p for p, s in player_scores.items() if s >= 2000}
    print("High score players set  :", sorted(high_score_players))

    print("=== Combined Analysis ===")
    total_players = len(unique_players)
    total_unique_ach = len(unique_achievements)
    avg_score = sum(scores) / len(scores)
    top_player = max(player_scores, key=player_scores.get)

    print(f"Total unique players     : {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score            : {avg_score:.1f}")
    print(f"Top performer            : {top_player} "
          f"({player_scores[top_player]} pts, "
          f"{ach_count.get(top_player, 0)} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
