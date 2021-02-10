from GameSetup import game
from tkinter import END, DISABLED, ACTIVE


def isvalidornot(button):
    if button["text"] == "-":
        return True
    else:
        return False


def end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn):
    if game_status == 1:
        disablebuttons(btns)
        switch_active_player_to_winner()
        countwin(pl1txt, pl2txt)
        lblone["text"] = "{} wins!".format(game.winner.name)
        lbltwo["text"] = "{} wins!".format(game.winner.name)
        new_game_btn["state"] = ACTIVE
    elif game_status == 0:
        disablebuttons(btns)
        game.draw_count = game.draw_count + 1
        drawtxt.delete(1.0, END)
        drawtxt.insert(1.0, game.draw_count)
        lblone["text"] = "Draw"
        lbltwo["text"] = "Draw"
        new_game_btn["state"] = ACTIVE


def check_for_game_status(playboard):
    if verticalwin(playboard):
        game.status = True
        return 1
    elif horizontalwin(playboard):
        game.status = True
        return 1
    elif diagonalwin(playboard):
        game.status = True
        return 1
    elif draw(playboard):
        game.status = None
        return 0
    else:
        game.status = False
        return -1


def verticalwin(playboard):
    column1 = [playboard[0][0], playboard[1][0], playboard[2][0]]
    column2 = [playboard[0][1], playboard[1][1], playboard[2][1]]
    column3 = [playboard[0][2], playboard[1][2], playboard[2][2]]
    statuscolumn1x = all(sign == "X" for sign in column1)
    statuscolumn1o = all(sign == "O" for sign in column1)
    statuscolumn2x = all(sign == "X" for sign in column2)
    statuscolumn2o = all(sign == "O" for sign in column2)
    statuscolumn3x = all(sign == "X" for sign in column3)
    statuscolumn3o = all(sign == "O" for sign in column3)
    if statuscolumn1x:
        game.tempwinsign = column1[0]
        return True
    elif statuscolumn1o:
        game.tempwinsign = column1[0]
        return True
    elif statuscolumn2x:
        game.tempwinsign = column2[0]
        return True
    elif statuscolumn2o:
        game.tempwinsign = column2[0]
        return True
    elif statuscolumn3x:
        game.tempwinsign = column3[0]
        return True
    elif statuscolumn3o:
        game.tempwinsign = column3[0]
        return True


def horizontalwin(playboard):
    statusrow0x = all(sign == "X" for sign in playboard[0])
    statusrow0o = all(sign == "O" for sign in playboard[0])
    statusrow1x = all(sign == "X" for sign in playboard[1])
    statusrow1o = all(sign == "O" for sign in playboard[1])
    statusrow2x = all(sign == "X" for sign in playboard[2])
    statusrow2o = all(sign == "O" for sign in playboard[2])
    if statusrow0x:
        game.tempwinsign = playboard[0][0]
        return True
    elif statusrow0o:
        game.tempwinsign = playboard[0][0]
        return True
    elif statusrow1x:
        game.tempwinsign = playboard[1][0]
        return True
    elif statusrow1o:
        game.tempwinsign = playboard[1][0]
        return True
    elif statusrow2x:
        game.tempwinsign = playboard[2][0]
        return True
    elif statusrow2o:
        game.tempwinsign = playboard[2][0]
        return True


def diagonalwin(playboard):
    diag_left_to_right = [playboard[0][0], playboard[1][1], playboard[2][2]]
    diag_right_to_left = [playboard[2][0], playboard[1][1], playboard[0][2]]
    statusdiag_left_to_rightx = all(sign == "X" for sign in diag_left_to_right)
    statusdiag_left_to_righto = all(sign == "O" for sign in diag_left_to_right)
    statusdiag_right_to_leftx = all(sign == "X" for sign in diag_right_to_left)
    statusdiag_right_to_lefto = all(sign == "O" for sign in diag_right_to_left)
    if statusdiag_left_to_rightx:
        game.tempwinsign = diag_left_to_right[0]
        return True
    elif statusdiag_left_to_righto:
        game.tempwinsign = diag_left_to_right[0]
        return True
    elif statusdiag_right_to_leftx:
        game.tempwinsign = diag_right_to_left[0]
        return True
    elif statusdiag_right_to_lefto:
        game.tempwinsign = diag_right_to_left[0]
        return True
    else:
        return False


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
            game.activeplayer.contrary_sign = game.player1.sign
        else:
            game.activeplayer.sign = game.player1.sign
            game.activeplayer.name = game.player1.name
            game.activeplayer.contrary_sign = game.player2.sign
    elif game.gamemode == 2:
        if game.activeplayer.sign == "X":
            game.activeplayer.sign = game.ai.sign
            game.activeplayer.name = game.ai.name
            game.activeplayer.contrary_sign = game.player1.sign
        else:
            game.activeplayer.sign = game.player1.sign
            game.activeplayer.name = game.player1.name
            game.activeplayer.contrary_sign = game.ai.sign
    elif game.gamemode == 3:
        if game.activeplayer.sign == "X":
            game.activeplayer.sign = game.ai2.sign
            game.activeplayer.name = game.ai2.name
            game.activeplayer.contrary_sign = game.ai1.sign
        else:
            game.activeplayer.sign = game.ai1.sign
            game.activeplayer.name = game.ai1.name
            game.activeplayer.contrary_sign = game.ai2.sign


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