from Player import *
from AI import *
import random


class Game:
    player1 = Player
    player2 = Player
    ai = AI
    activeplayer = ActivePlayer
    status = False
    winner = Winner
    tempwinsign = str
    win_count_pl1 = int
    win_count_pl2 = int
    draw_count = int
    gamemode = int  # 1:player vs player, 2:player vs AI, 3:AI vs AI
    run_ai_vs_ai = False  #### stop gamemode3-loop when clicking on other gamemode
                                # or stopping the game while gamemode 3 is running###

    def choose_who_starts_first(self, gamemode):
        choice = [1, 2]
        pick = random.choice(choice)
        if gamemode == 1:
            self.gamemode = 1
            if pick == 1:
                self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name, self.player2.sign)
            else:
                self.activeplayer = ActivePlayer(self.player2.sign, self.player2.name, self.player1.sign)
        elif gamemode == 2:
            self.gamemode = 2
            if pick == 1:
                self.activeplayer = ActivePlayer(self.player1.sign, self.player1.name, self.ai.sign)
            else:
                self.activeplayer = ActivePlayer(self.ai.sign, self.ai.name, self.player1.sign)
        elif gamemode == 3:
            self.gamemode = 3
            if pick == 1:
                self.activeplayer = ActivePlayer(self.ai1.sign, self.ai1.name, self.ai2.sign)
            else:
                self.activeplayer = ActivePlayer(self.ai2.sign, self.ai2.name, self.ai1.sign)

    def set_game_for_plvspl(self):
        self.status = False
        self.player1 = Player("X", "PlayerX")
        self.player2 = Player("O", "PlayerO")
        self.choose_who_starts_first(1)
        self.winner = Winner()
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0

    def set_game_for_aivspl(self):
        self.status = False
        self.player1 = Player("X", "PlayerX")
        self.ai = AI("O", "AI")
        self.choose_who_starts_first(2)
        self.winner = Winner()
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0

    def set_game_for_aivai(self):
        self.status = False
        self.ai1 = AI("X", "PlayerX")
        self.ai2 = AI("O", "PlayerO")
        self.choose_who_starts_first(3)
        self.winner = Winner()
        self.win_count_pl1 = 0
        self.win_count_pl2 = 0
        self.draw_count = 0
        self.run_ai_vs_ai = True


game = Game()
