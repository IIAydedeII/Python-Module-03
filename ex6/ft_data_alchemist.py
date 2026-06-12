#!/usr/bin/env python3
import random

PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print("")

    players_capitalized = [player.capitalize() for player in PLAYERS]
    capitalized_players = [
        player for player in PLAYERS if player.capitalize() == player
    ]

    print("Initial list of players:", PLAYERS)
    print("New list with all names capitalized:", players_capitalized)
    print("New list of capitalized names only:", capitalized_players)
    print("")

    scores = {player: random.randrange(999) for player in players_capitalized}
    average = round(sum(scores.values()) / len(scores), 2)
    high_scores = {
        player: score for player, score in scores.items() if score > average
    }

    print("Score dict:", scores)
    print("Score average is", average)
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
