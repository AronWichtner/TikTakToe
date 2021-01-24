from Gamefunctions import *


def reset_game_to_aivspl(btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.set_game_for_aivspl()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    #own def ?
    if game.activeplayer.name == game.ai.name:
        game.ai.setsignrandom(btns)
        switch_active_player()
    else:
        return None




