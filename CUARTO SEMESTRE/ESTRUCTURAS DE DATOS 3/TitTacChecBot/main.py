from round_robin import RoundRobin
from player_random import TTCPlayerRandom
from player2 import TTCPlayer
import random

player1 = TTCPlayerRandom("juan")
player2 = TTCPlayer("Nacho el Demolidor")
#player3 = TTCPlayer("juan3")
#player4 = TTCPlayer("juan4")

if __name__ == '__main__':
    tournament = RoundRobin([player1, player2], 30, 5, 150)
    tournament.start()