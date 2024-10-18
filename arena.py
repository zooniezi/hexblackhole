from game import Game

NUM_SET = 1


def game_setting():
    print("Do you want to play the game yourself?")
    print("Enter 1 if you want to play, otherwise it will be an AI match.")
    a = input()

def match_player(player1, player2, verbose=False):
    player1_wins = 0
    tiebreaker = 1

    for i in range(NUM_SET):
        print("\nGame start!\n")
        scrim = Game(player1, player2, tiebreaker, verbose)
        result = scrim.play()
        if result == 1:
            player1_wins += 1
        tiebreaker = 3 - tiebreaker
    win_rate = player1_wins / NUM_SET

    return win_rate
