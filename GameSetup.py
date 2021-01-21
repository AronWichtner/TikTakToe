from Player import *
from AI import *
import random


class Game:
    player1 = Player
    player2 = Player
    ai = AI
    activeplayer = ActivePlayer
    winner = Winner
    win_count_pl1 = int
    win_count_pl2 = int
    draw_count = int
    gamemode = int  # 1:player vs player, 2:player vs AI, 3:AI vs AI

    def choose_who_starts_first(self, gamemode):
        choice = [1, 2]
        pick = random.choice(choice)
        if gamemode == 1:
            self.gamemode = 1
            if pick == 1:
                self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)
            else:
                self.activeplayer = ActivePlayer(self.player2.sign, self.player2.name)
        elif gamemode == 2:
            self.gamemode = 2
            if pick == 1:
                self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name)
            else:
                self.activeplayer = ActivePlayer(self.ai.sign, self.ai.name)
        elif gamemode == 3:
            self.gamemode = 3
            return None  # set beginner in ki vs ki mode

    def set_game_for_plvspl(self):
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.choose_who_starts_first(1)
        self.winner = Winner(False)
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0

    def set_game_for_aivspl(self):
        self.player1 = Player("X", "PlayerX")
        self.ai = AI("O", "AI")
        self.choose_who_starts_first(2)
        self.winner = Winner(False)
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0


game = Game()
