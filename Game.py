from Player import *

class Game:
    player1 = Player
    player2 = Player
    activeplayer = ActivePlayer

    def set_players(self):
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)





