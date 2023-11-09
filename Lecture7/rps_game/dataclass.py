class GameChoice:
    rock = 1
    paper = 2
    scissors = 3  

class WinSide:
    server = 0
    player = 1
    draw = 2

def convert_to_choice(choice: str) -> GameChoice:

    if choice.lower() in ('r','rock'):
        return GameChoice.rock
    elif choice.lower() in ('p','paper'):
        return GameChoice.paper
    elif choice.lower() in ('s','scissors'):
        return GameChoice.scissors
    
def convert_choice_to_str(choice: GameChoice) -> str:

    if choice == GameChoice.rock:
        return 'Rock 🗿'
    elif choice == GameChoice.paper:
        return 'Paper 📝'
    elif choice == GameChoice.scissors:
        return 'Scissors ✂️'
    