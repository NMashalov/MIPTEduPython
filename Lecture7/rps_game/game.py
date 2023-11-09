from db import DatabaseConnection 
from utils import validate_choice_rps, PLAYER_CHOICE
from dataclass import (
    convert_to_choice,
    GameChoice,
    WinSide,
    convert_choice_to_str
)
from engine import random_choice, result

def auth(db_conn: DatabaseConnection):
    print('Hello!')
    name = input('What is your name? ') # Валидация имени

    return db_conn.create_new_player(name)

# не зависит от работы с базой данных
def round() -> WinSide:
    print('Input your choice.')
    choice = input('Rock[R], Paper[P], Scissors[S]')
    # запрашиваем у пользователя выбор
    while not validate_choice_rps(choice):
        print(f'Input should be in {PLAYER_CHOICE}')
        choice = input('Rock[R], Paper[P], Scissors[S]')
    # переводим ввод пользователя в единый интерфейс
    user_choice: GameChoice = convert_to_choice(choice)

    # сервер принимает решение
    server_choice: GameChoice = random_choice()

    print(convert_choice_to_str(server_choice))

    return result(server_choice,user_choice)


def game(player_id,db_conn: DatabaseConnection):
    result = round()

    if result == WinSide.player:
        print('You win :)')
        db_conn.update_score(player_id,1)
    elif result == WinSide.draw:
        print('Draw ()')
        db_conn.update_score(player_id,0)
    else:
        print('You lose :(')
        db_conn.update_score(player_id,0)

 
def main():
    db_conn = DatabaseConnection('game.db')

    player_id = auth(db_conn)

    for i in range(3):
        game(player_id,db_conn)
    
    print(db_conn.print_scoreboard())

if __name__ == '__main__':
    main()

