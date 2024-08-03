from pathlib import Path
import sqlite3
from .db import Db
from contextlib import closing
from contextlib import contextmanager

from models.game import Game

class AutoClose:
    def __init__(self, dbpath):
        self.dbpath = dbpath

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbpath)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, typ, value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

# You'll then call your class like this:

# with SafeCursor(conn) as c:
#     c.execute(...)

# @contextmanager
# def db_ops(db_name):
#     conn = sqlite3.connect(db_name)
#     try:
#         cur = conn.cursor()
#         yield cur
#     except Exception as e:
#         # do something with exception
#         conn.rollback()
#         raise e
#     else:
#         conn.commit()
#     finally:
#         conn.close()
# with db_ops('dbpath') as cur:
    # cur.

# def x():
#     with closing(sqlite3.connect("aquarium.db")) as connection:
#         with closing(connection.cursor()) as cursor:
#             rows = cursor.execute("SELECT 1").fetchall()
#             print(rows)

# def dec(meth):
#     def wrap(*args, **kwargs):
#         print(f'method: {args}, {kwargs}')
#         meth(*args, **kwargs)
#     return wrap

class SqliteDb(Db):
    
    def __init__(self, filepath:str, clear=False) -> None:
        self.filepath = Path(filepath)
        self.create(clear=clear)
        # self.db = sqlite3.connect(self.filepath)

    def clear(self):
        sql = "DELETE FROM games"
        with AutoClose(self.filepath) as cur:
            return cur.execute(sql).fetchall()

    def create(self, clear=False):
        sql = "CREATE TABLE IF NOT EXISTS games (" \
                "id INTEGER PRIMARY KEY," \
                "date VARCHAR(8) NOT NULL," \
                "title VARCHAR(250) NOT NULL" \
                ")"
        with AutoClose(self.filepath) as cur:
            cur.execute(sql)
        if clear:
            self.clear()

    def add(self, date, title):
        sql = 'INSERT INTO games (date, title) VALUES (:date, :title)'
        with AutoClose(self.filepath) as cur:
            cur.execute(sql, dict(date=date, title=title))
    
    def populate(self, data):
        sql = 'INSERT INTO games (date, title) VALUES (?, ?)'
        with AutoClose(self.filepath) as cur:
            cur.executemany(
                sql,
                data
            )
    
    def rows(self):
        with AutoClose(self.filepath) as cur:
            sql = "SELECT * FROM games"
            return [Game(date, title, id) for id, date, title in cur.execute(sql).fetchall()]
    
    def titles(self):
        # with AutoClose(self.filepath) as cur:
            # sql = "SELECT * FROM games"
            # return [title for title in cur.execute(sql).fetchall()]
        return [game.title for game in self.rows()]
    
    def find_title(self, title):
        with AutoClose(self.filepath) as cur:
            sql = "SELECT title FROM games WHERE title = ?"
            res =  cur.execute(sql, (title, )).fetchone()
            return res[0] if res is not None else None

    def find_titles_like(self, contains):
        with AutoClose(self.filepath) as cur:
            sql = "SELECT title FROM games WHERE title like ?"
            res =  cur.execute(sql, (f'%{contains}%', )).fetchall()
            # return res[0] if res is not None else None
            titles = [result[0] for result in res]
            return titles

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
