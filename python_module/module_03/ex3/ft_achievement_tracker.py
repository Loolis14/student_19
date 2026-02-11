#!/usr/bin/env python3

"""Fourth Exercise."""


class AchievementHunter:
    """Create and manage players and their achievements."""

    players: list["AchievementHunter"] = []

    def __init__(self, name: str) -> None:
        """Initalisation of a player."""
        self.name: str = name
        AchievementHunter.players.append(self)
        self.achievements: set[str] = set()

    def add_achievement(self, args: tuple[str]) -> None:
        """Add achievement(s) to a player."""
        self.achievements.update(args)

    def unique_by_player(self) -> set[str]:
        """Print achievement unlock juste by self."""
        others: set[str] = set()
        for player in AchievementHunter.players:
            if player.name == self.name:
                continue
            others |= player.achievements
        return self.achievements - others

    def print_unique_by_player(self) -> None:
        """Print the unique achievement for the chosen player."""
        unique: set[str] = self.unique_by_player()
        if not unique:
            print(f"{self.name.capitalize()} has no unique achievement yet")
        else:
            print(f"{self.name.capitalize()} unique: {unique}")

    @classmethod
    def achievement_tracker_system(cls) -> None:
        """Print all achievements every player has."""
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
        """Print all unique achievements."""
        unique: set[str] = set()
        for player in cls.players:
            unique = unique.union(player.achievements)
        print(f"All unique achievements: {unique}")
        print(f"Total unique achievements: {len(unique)}")

    @classmethod
    def common_achievement(cls) -> None:
        """Print achievement unlock by all players."""
        common: set[str] = cls.players[0].achievements
        for player in cls.players[1:]:
            common = common.intersection(player.achievements)
        print(f"Common to all players: {common}")

    @classmethod
    def rare_achievement(cls) -> None:
        """Print all achievements obtained by one player."""
        rare: set[str] = set()
        for player in cls.players:
            rare |= player.unique_by_player()
        print(f"Rare achievements (1 player): {rare}")

    @staticmethod
    def common_compare(player1: "AchievementHunter",
                       player2: "AchievementHunter") -> str:
        """Print what achievement two players has in commom."""
        common: set[str] = player1.achievements & player2.achievements
        return (
            f"{player1.name.capitalize()} vs {player2.name.capitalize()} "
            f"common: {common}")


def tests():
    """Test functions built on AchievementHunter class."""
    AchievementHunter.achievement_tracker_system()
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
    alice.add_achievement(('first_kill', 'level_10',
                          'treasure_hunter', 'speed_demon'))
    bob.add_achievement(('first_kill', 'level_10',
                        'boss_slayer', 'collector'))
    charlie.add_achievement(('level_10', 'treasure_hunter',
                            'boss_slayer', 'speed_demon', 'perfectionist'))
    tests()
