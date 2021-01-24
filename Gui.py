from tkinter import *
from Onclick import *
from PlayerVsPlayer import *
from AIvsPl import *
from Play_again import *


def create_window():

    window = Tk()
    window.title("TicTacToe")

    f1 = Frame(window)
    f1.grid(column=0, row=1)

    buttons = [[], [], []]

    for y in range(3):
        for x in range(3):
            btn = Button(f1, text="-", height=7, width=15)
            btn.configure(command=lambda b=btn: onclick(b, lbl1, lbl2, buttons, pl1txt, drawtxt, pl2txt, new_game_btn))
            btn.grid(column=x, row=y)
            btn["state"] = DISABLED
            buttons[y].append(btn)

    lbl1 = Label(window, text="-")
    lbl1.grid(column=0, row=0)

    lbl2 = Label(window, text="-")
    lbl2.grid(column=0, row=2)

    f2 = Frame(window)
    f2.grid(column=1, row=1)

    l3 = Label(f2, text="Choose your gamemode:")
    l3.grid(column=0, row=0)

    new_game_btn = Button(f2, text="Play again", height=5, width=15, state=DISABLED)
    new_game_btn.grid(column=0, row=1)
    new_game_btn.configure(command=lambda: play_again(buttons, new_game_btn, lbl1, lbl2))

    pl_vs_pl_btn = Button(f2, text="Player vs Player", height=5, width=15)
    pl_vs_pl_btn.configure(
        command=lambda: reset_game_to_plvpl(buttons, pl1txt, drawtxt, pl2txt, new_game_btn, lbl1, lbl2))
    pl_vs_pl_btn.grid(column=1, row=1)

    pl_vs_ai_btn = Button(f2, text="Player vs AI", height=5, width=15)
    pl_vs_ai_btn.configure(
        command=lambda: reset_game_to_aivspl(buttons, pl1txt, drawtxt, pl2txt, new_game_btn, lbl1, lbl2))
    pl_vs_ai_btn.grid(column=0, row=2)

    ai_vs_ai_btn = Button(f2, text="AI vs AI", height=5, width=15)
    ai_vs_ai_btn.grid(column=1, row=2)

    f3 = Frame(window)
    f3.grid(column=2, row=1)

    pl1lbl = Label(f3, text="PlayerX")
    pl1lbl.grid(column=0, row=0)
    pl1txt = Text(f3, height=3, width=5)
    pl1txt.grid(column=0, row=1)

    drawlbl = Label(f3, text="Draw")
    drawlbl.grid(column=1, row=0)
    drawtxt = Text(f3, height=3, width=5)
    drawtxt.grid(column=1, row=1)

    pl2lbl = Label(f3, text="PlayerO")
    pl2lbl.grid(column=2, row=0)
    pl2txt = Text(f3, height=3, width=5)
    pl2txt.grid(column=2, row=1)

    def exit_game():
        window.destroy()

    exitbtn = Button(f2, text="exit game", height=4, width=10, command=exit_game)
    exitbtn.grid(column=0, row=3)

    window.mainloop()
