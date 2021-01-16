from GameSetup import *
from tkinter import *

game = Game()
game.set_players()


def reset_game(btns, pl1txt, drawtxt, pl2txt):
    pl1txt.delete(0.0, END)
    drawtxt.delete(0.0, END)
    pl2txt.delete(0.0, END)
    reset_playboard(btns)
    enablebuttons(btns)


def onclick(button, lblone, lbltwo, btns, pl1txt, drawtxt, pl2txt):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        win = check_for_winner_status(btns)
        if win:
            disablebuttons(btns)
            switch_active_player_to_winner()
            lblone["text"] = "{} wins!".format(game.winner.name)
            lbltwo["text"] = "{} wins!".format(game.winner.name)
            return True
        else:
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
            return False
    else:
        lbltwo["text"] = "There is already a sign."
        return False


def isvalidornot(button):
    if button["text"] == "-":
        return True
    else:
        return False


def create_playboard(btns):
    playboard = [[btns[0][0]["text"], btns[0][1]["text"], btns[0][2]["text"]],
                 [btns[1][0]["text"], btns[1][1]["text"], btns[1][2]["text"]],
                 [btns[2][0]["text"], btns[2][1]["text"], btns[2][2]["text"]]]
    return playboard

def reset_playboard(btns):
    for buttonlist in btns:
        for button in buttonlist:
            button["text"] = "-"


def check_for_winner_status(btns):
    playboard = create_playboard(btns)
    if verticalwin(playboard):
        return True
    elif horizontalwin(playboard):
        return True
    elif diagonalwin(playboard):
        return True
    else:
        return False


def verticalwin(playboard):
    statusrow0 = all(sign == game.activeplayer.sign for sign in playboard[0])
    statusrowe1 = all(sign == game.activeplayer.sign for sign in playboard[1])
    statusrowe2 = all(sign == game.activeplayer.sign for sign in playboard[2])
    if statusrow0:
        return True
    elif statusrowe1:
        return True
    elif statusrowe2:
        return True


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


def diagonalwin(playboard):
    diag_left_to_right = [playboard[0][0], playboard[1][1], playboard[2][2]]
    diag_right_to_left = [playboard[2][0], playboard[1][1], playboard[0][2]]
    statusdiag_left_to_right = all(sign == game.activeplayer.sign for sign in diag_left_to_right)
    statusdiag_right_to_left = all(sign == game.activeplayer.sign for sign in diag_right_to_left)
    if statusdiag_left_to_right:
        return True
    elif statusdiag_right_to_left:
        return True


def enablebuttons(btns):
    for buttonlist in btns:
        for button in buttonlist:
            button["state"] = ACTIVE


def disablebuttons(btns):
    for buttonlist in btns:
        for button in buttonlist:
            button["state"] = DISABLED



def switch_active_player():
    if game.activeplayer.sign == "X":
        game.activeplayer.sign = game.player2.sign
        game.activeplayer.name = game.player2.name
    else:
        game.activeplayer.sign = game.player1.sign
        game.activeplayer.name = game.player1.name


def switch_active_player_to_winner():
    game.winner.sign = game.activeplayer.sign
    game.winner.name = game.activeplayer.name
    game.winner.status = True


def create_window():
    window = Tk()

    window.title("TicTacToe")


    f1 = Frame(window)
    f1.grid(column=0, row=1)

    buttons = [[], [], []]

    for y in range(3):
        for x in range(3):
            btn = Button(f1, text="-", height=7, width=15)
            btn.configure(command=lambda b=btn: onclick(b, lbl1, lbl2, buttons, pl1txt, drawtxt, pl2txt))
            btn.grid(column=x, row=y)
            btn["state"] = DISABLED
            buttons[y].append(btn)

    lbl1 = Label(window, text="{}, but your sign!".format(game.activeplayer.name))
    lbl1.grid(column=0, row=0)

    lbl2 = Label(window, text="-")
    lbl2.grid(column=0, row=2)


    f2 = Frame(window)
    f2.grid(column=1, row=1)

    l3 = Label(f2, text="Choose your gamemode:")
    l3.grid(column=0, row=0)

    new_game_btn = Button(f2, text="Play again", height=5, width=15)
    new_game_btn.grid(column=0, row=1)
    new_game_btn.configure(command=lambda: None)

    pl_vs_pl_btn = Button(f2, text="Player vs Player", height=5, width=15)
    pl_vs_pl_btn.configure(command=lambda: reset_game(buttons, pl1txt, drawtxt, pl2txt))
    pl_vs_pl_btn.grid(column=1, row=1)

    pl_vs_ai_btn = Button(f2, text="Player vs AI", height=5, width=15)
    pl_vs_ai_btn.grid(column=0, row=2)

    ai_vs_ai_btn = Button(f2, text="AI vs AI", height=5, width=15)
    ai_vs_ai_btn.grid(column=1, row=2)


    f3 = Frame(window)
    f3.grid(column=2, row=1)

    pl1lbl = Label(f3, text=game.player1.name)
    pl1lbl.grid(column=0, row=0)
    pl1txt = Text(f3, height=3, width=5)
    pl1txt.grid(column=0, row=1)

    drawlbl = Label(f3, text="Draw")
    drawlbl.grid(column=1, row=0)
    drawtxt = Text(f3, height=3, width=5)
    drawtxt.grid(column=1, row=1)

    pl2lbl = Label(f3, text=game.player2.name)
    pl2lbl.grid(column=2, row=0)
    pl2txt = Text(f3, height=3, width=5)
    pl2txt.grid(column=2, row=1)


    window.mainloop()




#create_window()






