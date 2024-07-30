from json import JSONDecodeError
from db.jsondb import JsonDb
from pathlib import Path
import pytest

from models.game import Game

JSON_DB_PATH = 'test.json'

@pytest.fixture
def json_db_path():
    return JSON_DB_PATH

@pytest.fixture
def db(json_db_path):
    return JsonDb(json_db_path)

@pytest.fixture
def date():
    return '2024/08/01'

@pytest.fixture
def title():
    return 'geforce now'

@pytest.fixture
def records():
    return [['2024/08/01', 'geforce now'] for _ in range(10)]


def teardown_function():
    print(f'TEARDOWN_FUNCTION | deleting {JSON_DB_PATH}')
    Path(JSON_DB_PATH).unlink(missing_ok=True)


def test_can_instantiate_jsondb(json_db_path):
    db = JsonDb(json_db_path)

def test_create_empty_db(db, json_db_path):
    db.create([])
    assert Path(json_db_path).exists()
    assert db.data == []

def test_create_db_from_data(db, json_db_path, records):
    db.create(records)
    assert Path(json_db_path).exists()

def test_init_and_load_empty_db(db):
    assert db.data == []

def test_load_empty_db(db):
    db.load()
    assert db.data == []

def test_save_empty_db(db):
    db.save()
    db.load()
    assert db.data == []

def test_add_title(db, date, title):
    db.add(date, title)
    assert db.data == [Game(date, title)]

def test_save_and_reload_title(db, date, title):
    db.add(date, title)
    db.save()
    db.load()
    assert db.data == [Game(date, title)]

def test_populate_db(db, records):
    db.populate(records)
    expected = [Game(date=date, title=title) for date, title in records]
    assert db.data == expected

def test_populate_save_and_load(db, records):
    db.populate(records)
    db.save()
    db.load()
    expected = [Game(date=date, title=title) for date, title in records]
    assert db.data == expected

def test_populate_rows(db, records):
    db.populate(records)
    expected = [Game(date=date, title=title) for date, title in records]
    assert db.rows() == expected

def test_populate_save_load_rows(db, records):
    db.populate(records)
    db.save()
    db.load()
    expected = [Game(date=date, title=title) for date, title in records]
    assert db.rows() == expected

def test_titles(db):
    db.add('20000101', 'Doom')
    db.add('20000101', 'Quake')
    print(db.titles())
    assert db.titles() == ['Doom', 'Quake']

def test_find_title(db):
    db.add('20000101', 'Doom')
    db.add('20000101', 'Quake')
    assert db.find_title('doom') == 'Doom'

def test_title_like(db):
    db.add('20000101', 'id Doom')
    db.add('20000101', 'id Quake')
    assert db.title_like('id') == ['id Doom', 'id Quake']




