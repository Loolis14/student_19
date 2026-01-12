#!/usr/bin/env python3

class PlayerError(Exception):
    """To handle error if no name is given"""
    pass


class AchivementHunter:
    """create and manage players and their achievements"""
    players = []

    def __init__(self, name):
        """Initalisation of a player"""
        if name:
            self.name = name
            self.players.append(self)
        else:
            raise PlayerError("No name given")
        self.achievements = set()

    def add_achievement(self, *args):
        """To add achievement(s) to a player"""
        self.achievements = set(args)

    def unique_by_player(self):
        """Achievement unlock juste by self"""
        others = set()
        for player in AchivementHunter.players:
            if player.name == self.name:
                continue
            others |= player.achievements
        return self.achievements - others

    def print_unique_by_player(self):
        """To print the unique achievement for the chosen player"""
        unique = AchivementHunter.unique_by_player(self)
        if unique == set():
            print(f"{self.name.capitalize()} has no unique achievement yet")
        else:
            print(f"{self.name.capitalize()} unique: {unique}")

    @classmethod
    def achivement_tracker_system(cls):
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
    def unique_achievement(cls):
        """print all unique achievements"""
        unique = set()
        for player in cls.players:
            unique = unique.union(player.achievements)
        print(f"All unique achievements: {unique}")
        print(f"Total unique achievements: {len(unique)}")

    @classmethod
    def common_achievement(cls):
        """Achievement unlock by all players"""
        common = cls.players[0].achievements
        for player in cls.players[1:]:
            common = common.intersection(player.achievements)
        print(f"Common to all players: {common}")

    @classmethod
    def rare_achievement(cls):
        """All achievements obtained by one player"""
        rare = set()
        for player in cls.players:
            rare |= player.unique_by_player()
        print(f"Rare achievements (1 player): {rare}")

    @staticmethod
    def common_compare(player1, player2):
        """To print what achievement two players has in commom"""
        common = player1.achievements & player2.achievements
        return (
            f"{player1.name.capitalize()} vs {player2.name.capitalize()} "
            f"common: {common}")


def tests():
    """to test functions built on AchivementHunter class"""
    AchivementHunter.achivement_tracker_system()
    print("\n=== Achievement Analytics ===")
    AchivementHunter.unique_achievement()
    print()
    AchivementHunter.common_achievement()
    AchivementHunter.rare_achievement()
    print()
    print(AchivementHunter.common_compare(alice, bob))
    alice.print_unique_by_player()
    bob.print_unique_by_player()
    print("\n=== End of tests ===")


if __name__ == "__main__":
    # create players
    alice = AchivementHunter("alice")
    bob = AchivementHunter("bob")
    charlie = AchivementHunter("charlie")

    # add achievements to player
    AchivementHunter.add_achievement(
        alice, 'first_kill', 'level_10',
        'treasure_hunter', 'speed_demon'
        )
    AchivementHunter.add_achievement(
        bob, 'first_kill', 'level_10',
        'boss_slayer', 'collector'
                                     )
    AchivementHunter.add_achievement(
        charlie, 'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon', 'perfectionist'
        )
    tests()
