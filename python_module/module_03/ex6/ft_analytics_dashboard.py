#!/usr/bin/env python3

class Player:
    score_categorie = {}
    players = []

    def __init__(self, name, region):
        self.name = name
        self.achievements = []
        self.region = region
        self.score = 0
        Player.score_categorie[name] = "débutant"
        Player.players.append(self)

    def add_achievements(self, achievements):
        self.achievements += achievements

    def add_score(self, n):
        self.score += n
        if self.score < 10:
            Player.score_categorie[self.name] = "novice"
        elif 10 < self.score < 20:
            Player.score_categorie[self.name] = "expert"
        elif 20 < self.score:
            Player.score_categorie[self.name] = "démoniaque"


if __name__ == "__main__":
    diana = Player("Diana", "europe")
    bob = Player("Bob", "europe")
    alice = Player("Alice", "US")
    charlie = Player("Charlie", "US")

    diana.add_score(5)
    bob.add_score(22)
    alice.add_score(40)
    charlie.add_score(2)
