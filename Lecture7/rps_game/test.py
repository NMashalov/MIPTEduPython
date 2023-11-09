import db
from engine import random_choice, COMPUTER_CHOICE, result
from dataclass import GameChoice, WinSide

def test_db():
    db_conn = db.DatabaseConnection('local1.db')
    id = db_conn.create_new_player('Pasha')
    db_conn.update_score(id,0)
    db_conn.update_score(id,1)

    db_conn.delete_player(id-1)
    db_conn.print_scoreboard()

def test_decision():
    assert random_choice() in COMPUTER_CHOICE, f'Random choice should be in {COMPUTER_CHOICE}'

def test_result():
    assert result(GameChoice.paper,GameChoice.paper) == WinSide.draw, 'Result of paper vs paper should be draw'
    assert result(GameChoice.rock,GameChoice.paper) == WinSide.player, 'Result of rock vs paper should be player'

test_result()




