from Player import *
import random


class Game:
    player1 = Player
    player2 = Player
    activeplayer = ActivePlayer
    winner = Winner
    win_count_pl1 = int
    win_count_pl2 = int
    draw_count = int

    def choose_who_starts_first(self):
        choice = [1, 2]
        pick = random.choice(choice)
        if pick == 1:
            self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)
        else:
            self.activeplayer = ActivePlayer(self.player2.sign, self.player2.name)

    def set_game_for_plvspl(self):
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.choose_who_starts_first()
        self.winner = Winner(False)
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0








