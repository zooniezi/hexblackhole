from player import RandomPlayer
from arena import match_player

player1 = RandomPlayer()
player2 = RandomPlayer()

my_game = match_player(player1, player2)

print(my_game)
