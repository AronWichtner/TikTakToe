from Gamefunctions import *


def play_again(btns, new_game_btn, lblone, lbltwo):
    game.winner.status = False
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    if game.gamemode == 1:
        switch_active_player()
    elif game.gamemode == 2:
        switch_active_player()
        if game.activeplayer.name == game.ai.name:
            game.ai.setsignrandom(btns)
            switch_active_player()