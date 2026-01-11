#!/usr/bin/env python3

import sys


def create_score(args):
    """create an int list of scores"""
    score = []
    for arg in args:
        try:
            int(arg)
        except ValueError:
            return f"Oops, you typed '{arg}' instead of a number, monkey!"
        else:
            score.append(int(arg))
    return score


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        score = create_score(sys.argv[1:])
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score) / len(score)}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
