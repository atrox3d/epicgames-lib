from pathlib import Path
import sqlite3
from .db import Db
from contextlib import closing
from contextlib import contextmanager

class SafeCursor:
    def __init__(self, connection):
        self.con = connection

    def __enter__(self):
        self.cursor = self.con.cursor()
        return self.cursor

    def __exit__(self, typ, value, traceback):
        self.cursor.close()
# You'll then call your class like this:

# with SafeCursor(conn) as c:
#     c.execute(...)

@contextmanager
def db_ops(db_name):
    conn = sqlite3.connect(db_name)
    try:
        cur = conn.cursor()
        yield cur
    except Exception as e:
        # do something with exception
        conn.rollback()
        raise e
    else:
        conn.commit()
    finally:
        conn.close()
# with db_ops('dbpath') as cur:
    # cur.

def x():
    with closing(sqlite3.connect("aquarium.db")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            print(rows)

class SqliteDb(Db):
    
    def __init__(self, filepath:str) -> None:
        self.filepath = Path(filepath)
        self.db = sqlite3.connect(self.filepath)

    def_

    def create(self):

if False:
    cur = sqlite3.connect('epicgames-lib.db').cursor()
    sql = "CREATE TABLE IF NOT EXISTS games (" \
            "id INTEGER PRIMARY KEY," \
            "title VARCHAR(250) NOT NULL UNIQUE," \
            ")"


    new_rows = [
        ('100.100.100.100', 'a.b.c', 100),
        ('200.200.200.200', 'd.e.f', 200),
    ]

    cur.executemany(
        'INSERT into ips VALUES(?, ?, ?)',
        new_rows
    )
    cur.connection.commit()
