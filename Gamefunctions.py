from GameSetup import game
from tkinter import END, DISABLED, ACTIVE


def isvalidornot(button):
    if button["text"] == "-":
        return True
    else:
        return False


def end_game(game_over, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn):
    if game_over:
        disablebuttons(btns)
        switch_active_player_to_winner()
        countwin(pl1txt, pl2txt)
        lblone["text"] = "{} wins!".format(game.winner.name)
        lbltwo["text"] = "{} wins!".format(game.winner.name)
        new_game_btn["state"] = ACTIVE
    elif game_over is None:
        disablebuttons(btns)
        game.draw_count = game.draw_count + 1
        drawtxt.delete(1.0, END)
        drawtxt.insert(1.0, game.draw_count)
        lblone["text"] = "Draw"
        lbltwo["text"] = "Draw"
        new_game_btn["state"] = ACTIVE


def check_for_game_status(btns):
    check_for_winner_status(btns)
    if game.winner.status:
        return True
    elif game.winner.status is None:
        return None
    else:
        return False


def check_for_winner_status(btns):
    playboard = create_playboard(btns)
    if verticalwin(playboard):
        game.winner.status = True
    elif horizontalwin(playboard):
        game.winner.status = True
    elif diagonalwin(playboard):
        game.winner.status = True
    elif draw(playboard):
        game.winner.status = None
    else:
        return False


def horizontalwin(playboard):
    column1 = [playboard[0][0], playboard[1][0], playboard[2][0]]
    column2 = [playboard[0][1], playboard[1][1], playboard[2][1]]
    column3 = [playboard[0][2], playboard[1][2], playboard[2][2]]
    statuscolumn1 = all(sign == game.activeplayer.sign for sign in column1)
    statuscolumn2 = all(sign == game.activeplayer.sign for sign in column2)
    statuscolumn3 = all(sign == game.activeplayer.sign for sign in column3)
    if statuscolumn1:
        return True
    elif statuscolumn2:
        return True
    elif statuscolumn3:
        return True


def verticalwin(playboard):
    statusrow0 = all(sign == game.activeplayer.sign for sign in playboard[0])
    statusrow1 = all(sign == game.activeplayer.sign for sign in playboard[1])
    statusrow2 = all(sign == game.activeplayer.sign for sign in playboard[2])
    if statusrow0:
        return True
    elif statusrow1:
        return True
    elif statusrow2:
        return True


def diagonalwin(playboard):
    diag_left_to_right = [playboard[0][0], playboard[1][1], playboard[2][2]]
    diag_right_to_left = [playboard[2][0], playboard[1][1], playboard[0][2]]
    statusdiag_left_to_right = all(sign == game.activeplayer.sign for sign in diag_left_to_right)
    statusdiag_right_to_left = all(sign == game.activeplayer.sign for sign in diag_right_to_left)
    if statusdiag_left_to_right:
        return True
    elif statusdiag_right_to_left:
        return True


def draw(playboard):
    if game.gamemode == 1:
        statusrow0 = all(sign == game.player1.sign or sign == game.player2.sign for sign in playboard[0])
        statusrow1 = all(sign == game.player1.sign or sign == game.player2.sign for sign in playboard[1])
        statusrow2 = all(sign == game.player1.sign or sign == game.player2.sign for sign in playboard[2])
        status = [statusrow0, statusrow1, statusrow2]
        if all(status):
            return True
    elif game.gamemode == 2:
        statusrow0 = all(sign == game.player1.sign or sign == game.ai.sign for sign in playboard[0])
        statusrow1 = all(sign == game.player1.sign or sign == game.ai.sign for sign in playboard[1])
        statusrow2 = all(sign == game.player1.sign or sign == game.ai.sign for sign in playboard[2])
        status = [statusrow0, statusrow1, statusrow2]
        if all(status):
            return True
    elif game.gamemode == 3:
        statusrow0 = all(sign == game.ai1.sign or sign == game.ai2.sign for sign in playboard[0])
        statusrow1 = all(sign == game.ai1.sign or sign == game.ai2.sign for sign in playboard[1])
        statusrow2 = all(sign == game.ai1.sign or sign == game.ai2.sign for sign in playboard[2])
        status = [statusrow0, statusrow1, statusrow2]
        if all(status):
            return True


def countwin(pl1txt, pl2txt):
    if game.winner.sign == "X":
        game.win_count_pl1 = game.win_count_pl1 + 1
        pl1txt.delete(1.0, END)
        pl1txt.insert(1.0, game.win_count_pl1)
    elif game.winner.sign == "O":
        game.win_count_pl2 = game.win_count_pl2 + 1
        pl2txt.delete(1.0, END)
        pl2txt.insert(1.0, game.win_count_pl2)


def switch_active_player():
    if game.gamemode == 1:
        if game.activeplayer.sign == "X":
            game.activeplayer.sign = game.player2.sign
            game.activeplayer.name = game.player2.name
        else:
            game.activeplayer.sign = game.player1.sign
            game.activeplayer.name = game.player1.name
    elif game.gamemode == 2:
        if game.activeplayer.sign == "X":
            game.activeplayer.sign = game.ai.sign
            game.activeplayer.name = game.ai.name
        else:
            game.activeplayer.sign = game.player1.sign
            game.activeplayer.name = game.player1.name
    elif game.gamemode == 3:
        if game.activeplayer.sign == "X":
            game.activeplayer.sign = game.ai2.sign
            game.activeplayer.name = game.ai2.name
        else:
            game.activeplayer.sign = game.ai1.sign
            game.activeplayer.name = game.ai1.name


def switch_active_player_to_winner():
    game.winner.sign = game.activeplayer.sign
    game.winner.name = game.activeplayer.name


def create_playboard(btns):
    playboard = [[btns[0][0]["text"], btns[0][1]["text"], btns[0][2]["text"]],
                 [btns[1][0]["text"], btns[1][1]["text"], btns[1][2]["text"]],
                 [btns[2][0]["text"], btns[2][1]["text"], btns[2][2]["text"]]]
    return playboard


def reset_playboard(btns, lblone, lbltwo):
    lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
    lbltwo["text"] = "-"
    for buttonlist in btns:
        for button in buttonlist:
            button["text"] = "-"


def reset_score(pl1txt, drawtxt, pl2txt):
    pl1txt.delete(0.0, END)
    pl1txt.insert(1.0, game.win_count_pl1)
    drawtxt.delete(0.0, END)
    drawtxt.insert(1.0, game.draw_count)
    pl2txt.delete(0.0, END)
    pl2txt.insert(1.0, game.win_count_pl2)


def enablebuttons(btns):
    for buttonlist in btns:
        for button in buttonlist:
            button["state"] = ACTIVE


def disablebuttons(btns):
    for buttonlist in btns:
        for button in buttonlist:
            button["state"] = DISABLED