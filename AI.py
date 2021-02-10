import random
import time
from MiniMax import minimax


class AI:
    sign: str
    name: str

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name

    def check_for_valid_spots(self, btns):
        possible_buttons = []
        for buttonlist in btns:
            for button in buttonlist:
                if button["text"] == "-":
                    possible_buttons.append(button)
        return possible_buttons

    def setsignrandom(self, buttonlist):
        time.sleep(0.5)
        possible_buttons = self.check_for_valid_spots(buttonlist)
        button = random.choice(possible_buttons)
        button["text"] = self.sign

    def check_if_Playboard_empty(self, playboard):
        spots = []
        for row in playboard:
            for spot in row:
                spots.append(spot)
        if all(spot == "-" for spot in spots):
            return True
        else:
            return False

    def makeBestMove(self, bestmove, btns):
        time.sleep(0.5)
        row = bestmove[1]
        spot = bestmove[2]
        button = btns[row][spot]
        button["text"] = self.sign

    def find_best_move(self, playboard):
        emptyplayboard = self.check_if_Playboard_empty(playboard)
        if emptyplayboard:
            firstmove = [True, 0, 0]
            return firstmove
        else:
            ismaximizing = False
            possible_moves = []
            bestscore = -2
            rowcoordinate = -1
            for row in playboard:
                rowcoordinate += 1
                spotcoordinate = -1
                for spot in row:
                    spotcoordinate += 1
                    if spot == "-":
                        playboard[rowcoordinate][spotcoordinate] = self.sign
                        score = minimax(playboard, 100, ismaximizing)
                        playboard[rowcoordinate][spotcoordinate] = "-"
                        move = [bestscore, rowcoordinate, spotcoordinate]
                        if score > bestscore:
                            bestscore = score
                            possible_moves.clear()
                            possible_moves.append(move)
                        elif score == bestscore:
                            possible_moves.append(move)
                        else:
                            continue
                    else:
                        continue
            bestmove = random.choice(possible_moves)
            return bestmove  #returns a list ->[score,row,spot]


