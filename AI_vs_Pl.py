from Gamefunctions import *


def reset_game_to_aivspl(btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.set_game_for_aivspl()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    if game.activeplayer.name == game.ai.name:
        game.ai.setsign(btns)
    else:
        print("Activeplayer?")




