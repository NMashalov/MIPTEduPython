import sqlite3
# база создаётся автоматически 
conn = sqlite3.connect("student.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    grade INTEGER
)
"""          
)

values = ('NIKITA',10)
c.execute("INSERT INTO student(name,grade) VALUES(?,?)",values)
# подтверждаем внесенные изменения 
conn.commit()
conn.close()
