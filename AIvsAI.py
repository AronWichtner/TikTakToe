from Gamefunctions import *


def reset_game_to_aivsai(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.set_game_for_aivai()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    ai_vs_ai_game(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo)


def ai_vs_ai_game(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    moves = 9
    for i in range(moves):
        if game.run_ai_vs_ai:
            if game.activeplayer.name == game.ai1.name:
                game.ai1.setsignrandom(btns)
                game_over = check_for_game_status(btns)
                if game_over is True or game_over is None:
                    return end_game(game_over, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
                if not game_over:
                    switch_active_player()
                    lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
                    lbltwo["text"] = "-"
                window.update()
            elif game.activeplayer.name == game.ai2.name:
                game.ai2.setsignrandom(btns)
                game_over = check_for_game_status(btns)
                if game_over:
                    return end_game(game_over, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
                if not game_over:
                    switch_active_player()
                    lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
                    lbltwo["text"] = "-"
                window.update()
        else:
            return None



