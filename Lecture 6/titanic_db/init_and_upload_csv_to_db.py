import sqlite3
import csv

def init_db():
    conn = sqlite3.connect('titanic.db')
    c = conn.cursor()

    with open("titanic.csv","r") as f:
        headers = next(csv.reader(f))

    c.execute("CREATE TABLE IF NOT EXISTS  titanic (" + ",".join([f'{column} TEXT' for  column in headers]) + ")")


def upload_rows_to_db():
    conn = sqlite3.connect('titanic.db')
    c = conn.cursor()

    with open("titanic.csv","r") as f:
        reader = csv.reader(f)
        _ = next(reader)
        for row in reader:
            c.execute(f"INSERT INTO titanic VALUES ({','.join(['?']*len(row))})", tuple(row))
    conn.commit()
        

upload_rows_to_db()




