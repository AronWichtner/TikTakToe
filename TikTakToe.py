from tkinter import *
from Player import *


player1 = Player("X", "PlayerX")
player2 = Player("O", "PlayerO")
activeplayer = ActivePlayer(player1.sign, player1.name)


def switch_active_player():
    if activeplayer.sign == "X":
        activeplayer.sign = player2.sign
        activeplayer.name = player2.name
    else:
        activeplayer.sign = player1.sign
        activeplayer.name = player1.name


def onclick(button, lbl):
    if isvalidornot(button):
        button["text"] = activeplayer.sign
        lbl["text"] = "-"
        switch_active_player()
    else:
        lbl["text"] = "There is already a sign."


def isvalidornot(button):
    if button["text"] == "-":
        return True
    else:
        return False


window = Tk()


window.title("TicTacToe")

lbl1 = Label(window, text="{}, but your sign!".format(activeplayer.name))
lbl1.grid(column=0, row=0)

f1 = Frame(window)
f1.grid(column=0, row=1)

for y in range(3):
    for x in range(3):
        btn = Button(f1, text="-", height=7, width=15)
        btn.configure(command=lambda b=btn: onclick(b, lbl2))
        btn.grid(column=y, row=x)

lbl2 = Label(window, text="-")
lbl2.grid(column=0, row=2)

window.mainloop()








