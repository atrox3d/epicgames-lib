import sqlite3

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
