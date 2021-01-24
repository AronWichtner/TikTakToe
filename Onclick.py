from Gamefunctions import *


def onclick(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if game.gamemode == 1:
        onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn)
    elif game.gamemode == 2:
        onclick_for_plvai(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn)
    elif game.gamemode == 3:
        return None


def onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        game_over = check_for_game_status(btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
        if not game_over:
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
            return None
    else:
        lbltwo["text"] = "There is already a sign."
        return False


def onclick_for_plvai(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        game_over = check_for_game_status(btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
        if not game_over:
            disablebuttons(btns)
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
            game.ai.setsignrandom(btns)
            game_over = check_for_game_status(btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
            if not game_over:
                switch_active_player()
                enablebuttons(btns)
                return None
    else:
        lbltwo["text"] = "There is already a sign."
        return False











