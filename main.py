from player import RandomPlayer, HumanPlayer
from arena import match_player

print("Do you want to play the game yourself?")
print("Enter 1 if you want to play, otherwise it will be an AI match.")
a = input()
if a == '1':
    player1 = HumanPlayer()
    player2 = HumanPlayer()
else:
    player1 = RandomPlayer()
    player2 = RandomPlayer()


my_game = match_player(player1, player2, True)

print(my_game)
