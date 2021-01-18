from Player import *


class Game:
    player1 = Player
    player2 = Player
    activeplayer = ActivePlayer
    winner = Winner
    win_count_pl1 = int
    win_count_pl2 = int
    draw_count = int

    def set_game(self):
        #asign letters random for fair start
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)
        self.winner = Winner(False)
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0





