from Gamefunctions import *


def onclick(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if game.gamemode == 1:
        onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn)
    elif game.gamemode == 2:
        onclick_for_plvai(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn)
    elif game.gamemode == 3:
        # no onclick because no user input
        return None


def onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        playboard = create_playboard(btns)
        game_status = check_for_game_status(playboard)
        if game.status is True or game.status is None:
            return end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
        if not game.status:
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
    else:
        lbltwo["text"] = "There is already a sign."
        return False


def onclick_for_plvai(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        playboard = create_playboard(btns)
        game_status = check_for_game_status(playboard)
        if game.status is True or game.status is None:
            return end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
        if not game.status:
            disablebuttons(btns)
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
            playboard = create_playboard(btns)
            bestmove = game.ai.find_best_move(playboard)
            game.ai.makeBestMove(bestmove, btns)
            playboard = create_playboard(btns)
            game_status = check_for_game_status(playboard)
            if game.status is True or game.status is None:
                return end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
            if not game.status:
                switch_active_player()
                lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
                lbltwo["text"] = "-"
                enablebuttons(btns)
    else:
        lbltwo["text"] = "There is already a sign."
        return False
