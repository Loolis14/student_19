#!/usr/bin/env python3

from typing import List, Tuple


class PlayerError(Exception):
    """To handle error if no name is given"""
    pass


class AchievementHunter:
    """create and manage players and their achievements"""
    players: List["AchievementHunter"] = []

    def __init__(self, name: str) -> None:
        """Initalisation of a player"""
        if not name:
            raise PlayerError("No name given")
        self.name: str = name
        self.players.append(self)
        self.achievements: Tuple[str] = set()

    def add_achievement(self, *args: List[str]) -> None:
        """To add achievement(s) to a player"""
        self.achievements.update(args)

    def unique_by_player(self) -> Tuple[str]:
        """Achievement unlock juste by self"""
        others: Tuple[str] = set()
        for player in AchievementHunter.players:
            if player.name == self.name:
                continue
            others |= player.achievements
        return self.achievements - others

    def print_unique_by_player(self) -> None:
        """To print the unique achievement for the chosen player"""
        unique: Tuple[str] = self.unique_by_player()
        if unique == set():
            print(f"{self.name.capitalize()} has no unique achievement yet")
        else:
            print(f"{self.name.capitalize()} unique: {unique}")

    @classmethod
    def achivement_tracker_system(cls) -> None:
        """To print all achievements every player has"""
        print("=== Achievement Tracker System ===\n")
        for player in cls.players:
            if not player.achievements:
                print(f"Player {player.name} has no achievements yet.")
            else:
                print(
                    f"Player {player.name} "
                    f"achievements: {player.achievements}")

    @classmethod
    def unique_achievement(cls) -> None:
        """print all unique achievements"""
        unique: Tuple[str] = set()
        for player in cls.players:
            unique = unique.union(player.achievements)
        print(f"All unique achievements: {unique}")
        print(f"Total unique achievements: {len(unique)}")

    @classmethod
    def common_achievement(cls) -> None:
        """Achievement unlock by all players"""
        common: Tuple[str] = cls.players[0].achievements
        for player in cls.players[1:]:
            common = common.intersection(player.achievements)
        print(f"Common to all players: {common}")

    @classmethod
    def rare_achievement(cls) -> None:
        """All achievements obtained by one player"""
        rare: Tuple[str] = set()
        for player in cls.players:
            rare |= player.unique_by_player()
        print(f"Rare achievements (1 player): {rare}")

    @staticmethod
    def common_compare(player1: "AchievementHunter",
                       player2: "AchievementHunter") -> str:
        """To print what achievement two players has in commom"""
        common: Tuple[str] = player1.achievements & player2.achievements
        return (
            f"{player1.name.capitalize()} vs {player2.name.capitalize()} "
            f"common: {common}")


def tests():
    """to test functions built on AchievementHunter class"""
    AchievementHunter.achivement_tracker_system()
    print("\n=== Achievement Analytics ===")
    AchievementHunter.unique_achievement()
    print()
    AchievementHunter.common_achievement()
    AchievementHunter.rare_achievement()
    print()
    print(AchievementHunter.common_compare(alice, bob))
    alice.print_unique_by_player()
    bob.print_unique_by_player()
    print("\n=== End of tests ===")


if __name__ == "__main__":
    # create players
    alice = AchievementHunter("alice")
    bob = AchievementHunter("bob")
    charlie = AchievementHunter("charlie")

    # add achievements to player
    alice.add_achievement('first_kill', 'level_10',
                          'treasure_hunter', 'speed_demon')
    bob.add_achievement('first_kill', 'level_10',
                        'boss_slayer', 'collector')
    charlie.add_achievement('level_10', 'treasure_hunter',
                            'boss_slayer', 'speed_demon', 'perfectionist')
    tests()
