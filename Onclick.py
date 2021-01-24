from Gamefunctions import *


def onclick(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if game.gamemode == 1:
        onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn)
    elif game.gamemode == 2:
        onclick_for_plvai(button, lbltwo)
    elif game.gamemode == 3:
        return None


def onclick_forplvpl(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt, new_game_btn):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        check_for_winner_status(btns)
        if game.winner.status:
            disablebuttons(btns)
            switch_active_player_to_winner()
            countwin(pl1txt, pl2txt)
            lblone["text"] = "{} wins!".format(game.winner.name)
            lbltwo["text"] = "{} wins!".format(game.winner.name)
            new_game_btn["state"] = ACTIVE
            return True
        elif game.winner.status is None:
            disablebuttons(btns)
            game.draw_count = game.draw_count + 1
            drawtxt.delete(1.0, END)
            drawtxt.insert(1.0, game.draw_count)
            lblone["text"] = "Draw"
            lbltwo["text"] = "Draw"
            new_game_btn["state"] = ACTIVE
            return None
        else:
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            lbltwo["text"] = "-"
            return False
    else:
        lbltwo["text"] = "There is already a sign."
        return False


def onclick_for_plvai(button, lbltwo):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        # check for winner
        # either True (win) None(draw) False(none of them)
    else:
        lbltwo["text"] = "There is already a sign."
        return False





