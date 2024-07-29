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

def test_create_game_dict(date, title):
    game = Game(date, title)
    assert game.dict() == dict(date=date, title=title, id=None)

