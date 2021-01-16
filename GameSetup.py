from Player import *


class Game:
    player1 = Player
    player2 = Player
    activeplayer = ActivePlayer
    winner = Winner

    def set_players(self):
        #asign letters random for fair start
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)
        self.winner = Winner(False)





