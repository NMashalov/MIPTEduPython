import random


num_wins = 0
num_losses = 0
num_ties = 0

def run_game():
  choices = ['paper', 'scissors', 'rock']
  user_move = input("Please choice scissors, paper or rock: ")
    while user_move not in choices:
      user_move = input("Please choice scissors, paper or rock: ")
  comp_move = random.choice(choices)

  if user_move == comp_move:
    num_ties += 1
    print(f"BOTH with {user_move} - TIE")
  elif choices[(choices.index(user) + 1) % len(choices)] == comp_move:
    num_losses += 1
    print(f"COMPUTER with {comp_move} - WIN!")
  else:
    num_wins += 1
    print(f"USER with {user_move} - WIN!")

def print_results():
  print("You win %d times!" % num_wins)
  print("You lose %d times!" % num_losses)
  print("You tie %d times!" % num_ties)

if __name__ == "main":
  continue = 'y'
  while continue.lower() == 'y':
    run_game()
    continue = input('Enter "y"/"Y" to continue')
  print_results()



def player_choice(self) -> Choice:
    prompt = ("\nChoices are 'rock', 'paper', or 'scissors'.\n"
              "Which do you choose? ")
    while True:
        try:
            return Choice.from_str(input(prompt))
        except ValueError:
            print("Invalid input, try again!")