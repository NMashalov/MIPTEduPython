import random
from dataclass import GameChoice

COMPUTER_CHOICE = (
    GameChoice.rock,
    GameChoice.paper,
    GameChoice.scissors
)

def random_choice():
    '''
        Computer uniformly choice rock, paper or scissors
    '''
    return random.choice(COMPUTER_CHOICE)

def win_choice(user_choice: GameChoice):
    '''
        Computer choose only win variant 

        For making choice we use logic of rps
    '''
    if user_choice == GameChoice.rock:
        return GameChoice.paper
    elif user_choice == GameChoice.paper:
        return GameChoice.scissors
    elif user_choice == GameChoice.scissors:
        return GameChoice.rock
