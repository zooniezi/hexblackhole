from game import Game

NUM_SET = 1001


def match_player(player1, player2):
    player1_wins = 0
    tiebreaker = 1

    for i in range(NUM_SET):
        scrim = Game(player1, player2, tiebreaker)
        result = scrim.play()
        if result == 1:
            player1_wins += 1
        tiebreaker = 3 - tiebreaker
    win_rate = player1_wins / NUM_SET

    return win_rate
