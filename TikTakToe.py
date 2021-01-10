from tkinter import *
from Player import *


player1 = Player("X", "PlayerX")
player2 = Player("O", "PlayerO")
activeplayer = ActivePlayer(player1.sign, player1.name)


def onclick(button, lbl):
    if isvalidornot(button):
        button["text"] = activeplayer.sign
        check_for_winner_status(lbl)
        switch_active_player()
        #if no win -->lbl["text"] = "-"
        #set lbl 1 to active player put your sign
    else:
        lbl["text"] = "There is already a sign."


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


def check_for_winner_status(lbl):
    if verticalwin(lbl):
        lbl["text"] = "{} wins!".format(activeplayer.name)
        return None
    elif horizontalwin(lbl):
        return None


def verticalwin(lbl):
    playboard = create_playboard()
    statusrow0 = all(sign == activeplayer.sign for sign in playboard[0])
    statusrowe1 = all(sign == activeplayer.sign for sign in playboard[1])
    statusrowe2 = all(sign == activeplayer.sign for sign in playboard[2])
    if statusrow0:
        return True
        #disable all buttons from buttons
    elif statusrowe1:
        return True
        # disable all buttons from buttons
    elif statusrowe2:
        return True


def horizontalwin(lbl):
    playboard = create_playboard()


def switch_active_player():
    if activeplayer.sign == "X":
        activeplayer.sign = player2.sign
        activeplayer.name = player2.name
    else:
        activeplayer.sign = player1.sign
        activeplayer.name = player1.name


#start Gui
window = Tk()


window.title("TicTacToe")

lbl1 = Label(window, text="{}, but your sign!".format(activeplayer.name))
lbl1.grid(column=0, row=0)

f1 = Frame(window)
f1.grid(column=0, row=1)

buttons = [[], [], []]
for y in range(3):
    for x in range(3):
        btn = Button(f1, text="-", height=7, width=15)
        buttons[y].append(btn)
        btn.configure(command=lambda b=btn: onclick(b, lbl2))
        btn.grid(column=x, row=y)


lbl2 = Label(window, text="-")
lbl2.grid(column=0, row=2)

window.mainloop()
#end Gui








