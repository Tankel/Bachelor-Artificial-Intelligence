from round_robin import RoundRobin

from player_random import TTCPlayer as RandomTTCPlayer
from player import TTCPlayer as NormalTTCPlayer
from player2 import TTCPlayer as Normal2TTCPlayer
from player3 import TTCPlayer as Normal3TTCPlayer
from playerNacho import TTCPlayer as Normal4TTCPlayer
from player5 import TTCPlayer

player1 = RandomTTCPlayer("brandon")
player2 = Normal4TTCPlayer("Nacho")
#player3 = Normal4TTCPlayer("Octopus")
#player3 = Normal2TTCPlayer("Nacho")
player4 = Normal3TTCPlayer("kevin")
#player5 = TTCPlayer("Kevin")


if __name__ == '__main__':
    tournament = RoundRobin([player1, player2], 20, 5, 70)
    tournament.start()
