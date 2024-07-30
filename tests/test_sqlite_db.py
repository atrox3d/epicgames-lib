from db.sqlitedb import SqliteDb
from pathlib import Path
import pytest

from models.game import Game

SQLITE_DB_PATH = 'test.db'

@pytest.fixture
def sqlite_db_path() -> str:
    return SQLITE_DB_PATH

@pytest.fixture
def db(sqlite_db_path) -> SqliteDb:
    return SqliteDb(sqlite_db_path)

@pytest.fixture
def empty_db(sqlite_db_path) -> SqliteDb:
    return SqliteDb(sqlite_db_path, clear=True)

@pytest.fixture
def date() -> str:
    return '2024/08/01'

@pytest.fixture
def title() -> str:
    return 'geforce now'

@pytest.fixture
def game(date, title) -> Game:
    return Game(date, title)

@pytest.fixture
def records(game) -> list[Game]:
    return [game for _ in range(10)]



def test_can_instantiate_sqlitefb(sqlite_db_path):
    db = SqliteDb(sqlite_db_path)
    assert Path(sqlite_db_path).exists()

def test_create_empty_db(empty_db, sqlite_db_path):
    assert Path(sqlite_db_path).exists()
    assert empty_db.rows() == []

# def test_init_and_load_empty_db(db):
#     assert db.data == []

def test_load_empty_db(empty_db):
    records = empty_db.rows()
    print(records)
    assert records == []
#     assert db.data == []

# def test_save_empty_db(db):
#     db.save()
#     db.load()
#     assert db.data == []

def test_empty_query(empty_db):
    rows = empty_db.rows()
    assert rows == []

def test_add_title(empty_db, date, title, game):
    empty_db.add(date, title)
    game.id = 1
    assert empty_db.rows() == [game]

# def test_save_and_reload_title(db, date, title):
#     db.add(date, title)
#     db.save()
#     db.load()
#     assert db.data == [{'date': date, 'title': title}]

def test_populate_db(empty_db, records):
    empty_db.populate([(game.date, game.title) for game in records])
    expected = [Game(game.date, game.title, id) for id, game in enumerate(records, 1)]
    assert empty_db.rows() == expected

# def test_populate_save_and_load(db, records):
#     db.populate(records)
#     db.save()
#     db.load()
#     expected = [dict(date=date, title=title) for date, title in records]
#     assert db.data == expected

# def test_populate_rows(db, records):
#     db.populate(records)
#     expected = [dict(date=date, title=title) for date, title in records]
#     assert list(db.rows()) == expected

# def test_populate_save_load_rows(db, records):
#     db.populate(records)
#     db.save()
#     db.load()
#     expected = [dict(date=date, title=title) for date, title in records]
#     assert list(db.rows()) == expected

# def test_titles(db):
#     db.add('20000101', 'Doom')
#     db.add('20000101', 'Quake')
#     print(db.titles())
#     assert db.titles() == ['Doom', 'Quake']

# def test_find_title(db):
#     db.add('20000101', 'Doom')
#     db.add('20000101', 'Quake')
#     assert db.find_title('doom') == 'Doom'

# def test_title_like(db):
#     db.add('20000101', 'id Doom')
#     db.add('20000101', 'id Quake')
#     assert db.title_like('id') == ['id Doom', 'id Quake']




