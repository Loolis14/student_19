#!/usr/bin/env python3

"""Second Exercise."""

import sys


def get_scores(args: list[str]) -> list[int]:
    """Get scores."""
    score: list[int] = []
    for arg in args:
        try:
            score.append(int(arg))
        except ValueError:
            print(f"Oops, you typed '{arg}' instead of a number.")
    return score


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        score = get_scores(sys.argv[1:])
        if not score:
            print("No valid scores to process")
        else:
            print(f"Scores processed: {score}")
            print(f"Total players: {len(score)}")
            print(f"Total score: {sum(score)}")
            print(f"Average score: {sum(score) / len(score):.1f}")
            print(f"High score: {max(score)}")
            print(f"Low score: {min(score)}")
            print(f"Score range: {max(score) - min(score)}")
