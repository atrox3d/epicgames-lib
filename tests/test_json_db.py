from db.json import JsonDb
from pathlib import Path


JSON_DB_PATH = 'test.json'

def test_can_instantiate_jsondb():
    db = JsonDb(JSON_DB_PATH)

def test_create_empty_db():
    db = JsonDb(JSON_DB_PATH)
    db.create()
    assert Path(JSON_DB_PATH).exists()

def test_init_and_load_empty_db():
    db = JsonDb(JSON_DB_PATH, load=True)
    assert db.data == []

def test_load_empty_db():
    db = JsonDb(JSON_DB_PATH)
    db.load()
    assert db.data == []

def test_save_empty_db():
    db = JsonDb(JSON_DB_PATH)
    db.save()
    db.load()
    assert db.data == []

def test_add_title():
    db = JsonDb(JSON_DB_PATH)
    date = '2024/08/01'
    title = 'geforce now'
    db.add(date, title)
    assert db.data == [{'date': date, 'title': title}]

def test_save_and_reload_title():
    db = JsonDb(JSON_DB_PATH)
    date = '2024/08/01'
    title = 'geforce now'
    db.add(date, title)
    db.save()
    db.load()
    assert db.data == [{'date': date, 'title': title}]

def test_populate_db():
    db = JsonDb(JSON_DB_PATH)
    records = [['2024/08/01', 'geforce now'] for _ in range(10)]
    db.populate(records)
    expected = [dict(date=date, title=title) for date, title in records]
    assert db.data == expected

def test_populate_save_and_load():
    db = JsonDb(JSON_DB_PATH)
    records = [['2024/08/01', 'geforce now'] for _ in range(10)]
    db.populate(records)
    db.save()
    db.load()
    expected = [dict(date=date, title=title) for date, title in records]
    assert db.data == expected

def test_populate_rows():
    db = JsonDb(JSON_DB_PATH)
    records = [['2024/08/01', 'geforce now'] for _ in range(10)]
    db.populate(records)
    expected = [dict(date=date, title=title) for date, title in records]
    assert list(db.rows()) == expected

def test_populate_save_load_rows():
    db = JsonDb(JSON_DB_PATH)
    records = [['2024/08/01', 'geforce now'] for _ in range(10)]
    db.populate(records)
    db.save()
    db.load()
    expected = [dict(date=date, title=title) for date, title in records]
    assert list(db.rows()) == expected






