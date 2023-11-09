import sqlite3


class DatabaseConnection:
    def __init__(self,db_name='local.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor() 
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scoreboard(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                game_suc INTEGER,
                game_cnt INTEGER      
            )
        """)

    def create_new_player(self,name: str) -> int:
        self.cursor.execute("""
            INSERT INTO scoreboard(name,game_suc,game_cnt)
            VALUES (?,0,0)
        """,(name,))

        self.conn.commit()

        return int(self.cursor.lastrowid)

    def update_score(self,player_id,result):
        """
            result:
                1 -  when player win 
                0 -  when player lose or draw
        """

        self.cursor.execute("""
            UPDATE scoreboard
            SET 
                game_suc = game_suc + (?),
                game_cnt = game_cnt + 1
            WHERE id = (?)
        """,(result,player_id,))
        self.conn.commit()

    def delete_player(self,player_id):

        self.cursor.execute("""
            DELETE FROM  scoreboard
            WHERE id = (?)
        """,(player_id,))

        self.conn.commit()

    def print_scoreboard(self):
        
        self.cursor.execute("""
            SELECT name,
                game_suc,
                game_cnt
            FROM scoreboard
        """)


        return self.cursor.fetchall() 
 
if __name__ == '__main__':
    print('')   
    




