#!/usr/bin/env python3
import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    amount = random.randrange(1, ACHIEVEMENTS.__len__())
    return set(random.sample(ACHIEVEMENTS, k=amount))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print("")

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements: dict[str, set[str]] = {player: set() for player in players}

    for player in players:
        achievements[player] = gen_player_achievements()
        print(f"Player {player}:", achievements[player])
    print("")

    print("Common achievements:", set.intersection(*achievements.values()))
    print("")

    for player in players:
        others = (achievements[p] for p in players if p != player)
        print(
            f"Only {player} has:",
            achievements[player].difference(*others),
        )
    print("")

    total = set.union(*achievements.values())
    for player in players:
        print(
            f"{player} is missing:",
            total.difference(achievements[player]),
        )


if __name__ == "__main__":
    main()
