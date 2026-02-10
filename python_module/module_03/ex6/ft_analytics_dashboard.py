#!/usr/bin/env python3

from typing import List, Dict, Set


class Player:
    score_categorie: Dict = {
        "novice": 0,
        "expert": 0,
        "démoniaque": 0
    }
    players: List = []

    def __init__(self, name, region):
        self.name = name
        self.achievements = []
        self.region = region
        self.score = 0
        self.score_categorie: str = "novice"
        Player.score_categorie[self.score_categorie] += 1
        Player.players.append(self)

    def add_achievements(self, achievements):
        self.achievements += achievements

    def add_score(self, n):
        self.score += n
        if 10 < self.score < 30:
            Player.score_categorie["novice"] -= 1
            Player.score_categorie["expert"] += 1
        elif 39 < self.score:
            Player.score_categorie["novice"] -= 1
            Player.score_categorie["démoniaque"] += 1


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    diana = Player("Diana", "europe")
    bob = Player("Bob", "europe")
    alice = Player("Alice", "US")
    charlie = Player("Charlie", "US")

    diana.add_score(5)
    bob.add_score(22)
    alice.add_score(40)
    charlie.add_score(2)

    diana.add_achievements(['first kill', 'fishing'])
    bob.add_achievements(['boss slayer', 'level 10'])
    alice.add_achievements(['level 10'])
    charlie.add_achievements(['fishing'])

    print("\n=== List Comprehension Examples ===")
    high_scorers: List = []
    doubled: List = []
    active_players: List = []
    for player in Player.players:
        doubled.append(player.score * 2)
        active_players.append(player.name)
        if player.score > 39:
            high_scorers.append(player.name)
    print(f"High scorers (>39): {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    players_score: Dict = {}
    count_achievements: Dict = {}
    for player in Player.players:
        players_score[player.name] = player.score
        count_achievements[player.name] = len(player.achievements)
    print(f"Player scores: {players_score}")
    print(f"Score categories: {Player.score_categorie}")
    print(f"Achievement counts: {count_achievements}")

    print("\n=== Set Comprehension Examples ===")
    unique_player: Set = set()
    unique_achievements: Set = {ach
                                for player in Player.players
                                for ach in player.achievements}
    active_regions: Set = {player.region
                           for player in Player.players}
    for player in Player.players:
        unique_player.add(player.name)
    print(f'Unique players: {unique_player}')
    print(f'Unique achievements: {unique_achievements}')
    print(f'Active regions: {active_regions}')

    print("\n=== Combined Analysis ===")
    print(f'Total players: {len(Player.players)}')
    print(f'Total unique achievements: {len(unique_achievements)}')
    print(f'Average score: '
          f'{sum(players_score.values()) / len(players_score): .2f}')
    max_ = max(players_score.values())
    for player in Player.players:
        if player.score == max_:
            print(f'Top performer: {player.name} '
                  f'({player.score} points, '
                  f'{len(player.achievements)} achievements)')
