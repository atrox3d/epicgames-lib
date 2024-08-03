from pathlib import Path
from .db import Db
from .jsondb import JsonDb
from .sqlitedb import SqliteDb


def get_db(filepath:str|Path) -> Db:
    ext = Path(filepath).suffix.lower()

    if ext == '.db':
        return SqliteDb(filepath)
    elif ext == '.json':
        return JsonDb(filepath)
    else:
        raise NotImplementedError

