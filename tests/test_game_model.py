import pytest
from models.game import Game


@pytest.fixture
def date():
    return '20240101'

@pytest.fixture
def title():
    return 'Doom'

def test_create_game(date, title):
    game = Game(date, title)
    assert game.date == date
    assert game.title == title
    assert game.id is None

def test_create_game_to_dict(date, title):
    game = Game(date, title)
    assert game.to_dict() == dict(date=date, title=title, id=None)

def test_create_game_from_dict(date, title):
    game_dict = dict(date=date, title=title, id=None)
    game = Game(**game_dict)
    assert game.date == date
    assert game.title == title
    assert game.id is None

