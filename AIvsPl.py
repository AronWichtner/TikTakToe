from Gamefunctions import *


def reset_game_to_aivsplminimax(btns, pl1txt, drawtxt, pl2txt, new_game_btn, lblone, lbltwo):
    game.run_ai_vs_ai = False
    game.set_game_for_aivspl()
    reset_score(pl1txt, drawtxt, pl2txt)
    new_game_btn["state"] = DISABLED
    reset_playboard(btns, lblone, lbltwo)
    enablebuttons(btns)
    if game.activeplayer.name == game.ai.name:
        playboard = create_playboard(btns)
        bestmove = game.ai.find_best_move(playboard)
        game.ai.makeBestMove(bestmove, btns)
        switch_active_player()
        lblone["text"] = "{}, put your sign!".format(game.activeplayer.name)
        lbltwo["text"] = "-"
    else:
        return None  # Player has to make move


