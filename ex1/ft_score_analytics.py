#!/usr/bin/env python3
import sys


class Stats:
    def __init__(self, scores: list[int]) -> None:
        self._scores = scores
        self._total_players = len(scores)
        self._total_score = sum(scores)
        self._average_score = self._total_score / self._total_players
        self._high_score = max(scores)
        self._low_score = min(scores)
        self._score_range = self._high_score - self._low_score

    def __str__(self) -> str:
        return (
            f"Scores processed: {self._scores}\n"
            f"Total players: {self._total_players}\n"
            f"Total score: {self._total_score}\n"
            f"Average score: {self._average_score:.1f}\n"
            f"High score: {self._high_score}\n"
            f"Low score: {self._low_score}\n"
            f"Score range: {self._score_range}"
        )


def main() -> None:
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    scores = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: python3",
            sys.argv[0],
            "<score1> <score2> ...",
        )
    else:
        print(Stats(scores))


if __name__ == "__main__":
    main()
