from db.sqlitedb import SqliteDb
from pathlib import Path
import pytest

from models.game import Game

SQLITE_DB_PATH = 'test.db'

@pytest.fixture
def sqlite_db_path() -> str:
    return SQLITE_DB_PATH

@pytest.fixture
def empty_db(sqlite_db_path) -> SqliteDb:
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

def test_load_empty_db(empty_db):
    records = empty_db.rows()
    print(records)
    assert records == []

def test_empty_query(empty_db):
    rows = empty_db.rows()
    assert rows == []

def test_add_title(empty_db, date, title, game):
    empty_db.add(date, title)
    game.id = 1
    assert empty_db.rows() == [game]

def test_populate_db(empty_db, records):
    empty_db.populate([(game.date, game.title) for game in records])
    expected = [Game(game.date, game.title, id) for id, game in enumerate(records, 1)]
    assert empty_db.rows() == expected

def test_titles(empty_db):
    empty_db.add('20000101', 'Doom')
    empty_db.add('20000101', 'Quake')
    print(empty_db.titles())
    assert empty_db.titles() == ['Doom', 'Quake']

def test_find_title(empty_db):
    empty_db.add('20000101', 'Doom')
    empty_db.add('20000101', 'Quake')
    assert empty_db.find_title('Doom') == 'Doom'


def test_not_found_title(empty_db):
    empty_db.add('20000101', 'Doom')
    empty_db.add('20000101', 'Quake')
    assert empty_db.find_title('Zoom') is None

def test_title_like(empty_db):
    empty_db.add('20000101', 'id Doom')
    empty_db.add('20000101', 'id Quake')
    assert empty_db.find_titles_like('id') == ['id Doom', 'id Quake']




