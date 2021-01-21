from Gamefunctions import *


def reset_game_to_plvpl(btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.set_game_for_plvspl()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)















