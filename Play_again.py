from Gamefunctions import *
from AIvsAI import ai_vs_ai_game


def play_again(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    switch_active_player()
    game.status = False
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    if game.gamemode == 1:
        return
    elif game.gamemode == 2:
        if game.activeplayer.name == game.ai.name:
            game.ai.setsignrandom(btns)
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
        else:
            pass
    elif game.gamemode == 3:
        ai_vs_ai_game(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo)
