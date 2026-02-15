from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    tournament = TournamentPlatform()
    print("Registering Tournament Cards...\n")
    dragon = TournamentCard("Fire Dragon",
                            5, Rarity.LEGENDARY, 10, 7, 5, "dragon_001", 1200)
    print(tournament.register_card(dragon))

    wizard = TournamentCard("Ice Wizard",
                            3, Rarity.LEGENDARY, 5, 9, 4, "wizard_001", 1150)
    print(tournament.register_card(wizard))

    print("Creating tournament match...")
    print(f'Match result: {tournament.create_match(dragon.id, wizard.id)}')

    leaderboard = tournament.get_leaderboard()
    print("\nTournament Leaderboard:")
    i = 1
    for stats in leaderboard:
        name, rating, win, lose = stats
        print(f'{i}. {name} - Rating: {rating} '
              f'({win}-{lose})')
        i += 1

"""
Creating tournament match...
Match result: {'winner': 'dragon_001'
,
'loser': 'wizard_001'
,
'winner_rating': 1216,'loser_rating': 1134}

Platform Report:
{'total_cards': 2,'matches_played': 1,
'avg_rating': 1175,'platform_status': 'active'}
=== Tournament Platform Successfully Deployed! ===
All abstract patterns working together harmoniously!
"""
