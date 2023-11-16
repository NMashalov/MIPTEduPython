def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT    
        )
    """)

def create_user(name:str,cursor,connector):
    cursor.execute("""
        INSERT INTO user(name) 
        VALUES (?)            
    """,(name,))
    connector.commit()


def select_users(cursor) -> str:
    cursor.execute("""
        SELECT * FROM user          
    """)
    return cursor.fetchall()