from operator import itemgetter


def sort_player(players):
    sorted_players = sorted(players, key=itemgetter(0, 1, 2))
    print(sorted_players)


if __name__ == "__main__":
    player1 = ("Anna", 18, 70)
    player2 = ("John", 20, 80)
    player3 = ("Jony", 19, 95)
    player4 = ("Json", 23, 120)
    player_list = [player4, player3, player2, player1]

    sort_player(player_list)
