from Gamefunctions import *


def reset_game_to_aivsai(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.set_game_for_aivai()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)  # cant be pressed -> just for better look
    ai_vs_ai_game(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo)


def ai_vs_ai_game(window, btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    moves = 9
    for i in range(moves):
        if game.run_ai_vs_ai:
            if game.activeplayer.name == game.ai1.name:
                playboard = create_playboard(btns)
                bestmove = game.ai1.find_best_move(playboard)
                game.ai1.makeBestMove(bestmove, btns)
                playboard = create_playboard(btns)
                game_status = check_for_game_status(playboard)
                if game.status is True or game.status is None:
                    return end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
                if not game.status:
                    switch_active_player()
                    lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
                    lbltwo["text"] = "-"
                window.update()
            elif game.activeplayer.name == game.ai2.name:
                playboard = create_playboard(btns)
                bestmove = game.ai2.find_best_move(playboard)
                game.ai2.makeBestMove(bestmove, btns)
                playboard = create_playboard(btns)
                game_status = check_for_game_status(playboard)
                if game.status is True or game.status is None:
                    return end_game(game_status, btns, pl1txt, drawtxt, pl2txt, lblone, lbltwo, new_game_btn)
                if not game.status:
                    switch_active_player()
                    lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
                    lbltwo["text"] = "-"
                window.update()
        else:
            return None



