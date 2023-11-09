PLAYER_CHOICE = (
    'r', 
    'p',
    's',
    'rock',
    'paper',
    'scissors'
)

def validate_choice_rps(choice: str) -> bool:
    '''
        Input of game rock paper scissors should be either R,P,S.
        It's ok to use letter in lower register.
        r,p,s - is ok.
        rp - is not ok.

    '''
    if choice.lower() in PLAYER_CHOICE:
        return True
    else:
        return False
        


if __name__ == '__main__':
    assert validate_choice_rps('r') == True, 'r is valid input'
    assert validate_choice_rps('rp') == False, 'rp is not valid input'

    assert validate_choice_rps('Rock') == True, 'Rock is valid input'

    print('OK!')

