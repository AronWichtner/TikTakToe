import Gamefunctions
import GameSetup


#def minimax(playboard, depth, isMaximizing):  # isMaximizing(bool) -> Max=True, Min=False
   #check for win draw or maxdepth reached (maxdepth = 0)
   #if true assign sore
       #win:1, draw:0, loss(minimzing player won):-1 maxdepth: return best_score
       #return score
   #else:
        # set best score for is Maximizing(True) best_score_formax = -2
        # set best score for is Maximizing(False) best_score_formin = 2
        #for every possible move:
           #make move in playboard
           #switch isMaximizing
           #score = minimax(playboard, depth -1, isMaximizing)
           #reset move
           #if isMaximizing:
               #if score > best_score
                   #best_score = score
           #elif is not isMaximzing:
               #if score < best_score:
                   #best_score = score
       #return best_score


def swich_isMaxmizing(m):
    if m is True:
        m = False
        return m
    else:
        m = True
        return m


def evaluate_game_status(game_status, depth):
    if game_status == 1:  # win
        if GameSetup.game.tempwinsign == GameSetup.game.activeplayer.sign:
            score = 1  # if self won
            GameSetup.game.status = False
        else:
            score = -1
            GameSetup.game.status = False
        return score
    elif game_status == 0:  # draw
        score = 0
        GameSetup.game.status = False
        return score
    elif depth == 0:  # max-depth reached
        # return best score until yet
        print("max depth reached")
        score = 0
        return score


def minimax(playboard, depth, ismaximizing):
    game_status = Gamefunctions.check_for_game_status(playboard)
    if GameSetup.game.status is True or GameSetup.game.status is None:
        return evaluate_game_status(game_status, depth)
    else:
        if ismaximizing:
            temporary_activeplayer_sign = GameSetup.game.activeplayer.sign
            best_score = -2
        else:
            temporary_activeplayer_sign = GameSetup.game.activeplayer.contrary_sign
            best_score = 2

        rowcoordinate = -1
        for row in playboard:
            rowcoordinate += 1
            spotcoordinate = -1
            for spot in row:
                spotcoordinate += 1
                if spot == "-":
                    playboard[rowcoordinate][spotcoordinate] = temporary_activeplayer_sign
                    ismaximizing = swich_isMaxmizing(ismaximizing)
                    score = minimax(playboard, depth-1, ismaximizing)
                    playboard[rowcoordinate][spotcoordinate] = "-"
                    ismaximizing = swich_isMaxmizing(ismaximizing)
                    if ismaximizing is True:
                        if score > best_score:
                            best_score = score
                    elif ismaximizing is False:
                        if score < best_score:
                            best_score = score
                else:
                    continue
        return best_score












