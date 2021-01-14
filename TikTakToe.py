from Game import *
from tkinter import *


game = Game()
game.set_players()


def onclick(button, lblone, lbltwo, btns):
    if isvalidornot(button):
        button["text"] = game.activeplayer.sign
        win = check_for_winner_status(lblone, lbltwo)
        if win:
            disablebuttons(btns)
        else:
            switch_active_player()
            lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
    else:
        lbltwo["text"] = "There is already a sign."


def isvalidornot(button):
    if button["text"] == "-":
        return True
    else:
        return False


def create_playboard():
    playboard = [[buttons[0][0]["text"], buttons[0][1]["text"], buttons[0][2]["text"]],
                 [buttons[1][0]["text"], buttons[1][1]["text"], buttons[1][2]["text"]],
                 [buttons[2][0]["text"], buttons[2][1]["text"], buttons[2][2]["text"]]]
    return playboard


def check_for_winner_status(lblone, lbltwo):
    playboard = create_playboard()
    if verticalwin(playboard):
        lblone["text"] = "{} wins!".format(game.activeplayer.name)
        lbltwo["text"] = "{} wins!".format(game.activeplayer.name)
        return True
    elif horizontalwin(playboard):
        lblone["text"] = "{} wins!".format(game.activeplayer.name)
        lbltwo["text"] = "{} wins!".format(game.activeplayer.name)
        return True
    elif diagonalwin(playboard):
        lblone["text"] = "{} wins!".format(game.activeplayer.name)
        lbltwo["text"] = "{} wins!".format(game.activeplayer.name)
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


window = Tk()


window.title("TicTacToe")


f1 = Frame(window)
f1.grid(column=0, row=1)

buttons = [[], [], []]
for y in range(3):
    for x in range(3):
        btn = Button(f1, text="-", height=7, width=15)
        buttons[y].append(btn)
        btn.configure(command=lambda b=btn: onclick(b, lbl1, lbl2, buttons))
        btn.grid(column=x, row=y)
        #disable button


lbl1 = Label(window, text="{}, but your sign!".format(game.activeplayer.name))
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="-")
lbl2.grid(column=0, row=2)


f2 = Frame(window)
f2.grid(column=1, row=1)

new_game_btn = Button(f2, text="Play again", height=5, width=15)
new_game_btn.grid(column=0, row=0)
#reset playboard, enable playboard
pl_vs_pl_btn = Button(f2, text="Player vs Player", height=5, width=15)
pl_vs_pl_btn.grid(column=1, row=0)

pl_vs_ai_btn = Button(f2, text="Player vs AI", height=5, width=15)
pl_vs_ai_btn.grid(column=0, row=1)

ai_vs_ai_btn = Button(f2, text="AI vs AI", height=5, width=15)
ai_vs_ai_btn.grid(column=1, row=1)

window.mainloop()










