from dataclass import WinSide, GameChoice

def result(server_decision: GameChoice, player_decision: GameChoice) -> WinSide:
    ''' 
        Return result of game
    ''' 

    if server_decision == player_decision:
        return WinSide.draw
    elif server_decision == GameChoice.paper and player_decision == GameChoice.rock:
        return WinSide.server
    elif server_decision == GameChoice.scissors and player_decision == GameChoice.paper:
        return WinSide.server
    elif server_decision == GameChoice.rock and player_decision == GameChoice.scissors:
        return WinSide.server
    else:
        return WinSide.player 
     