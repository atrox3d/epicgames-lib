import json
from pathlib import Path
from .db import Db
from models.game import Game


class JsonDb(Db):
    
    def __init__(self, filepath:str, load=False) -> None:
        self.filepath = Path(filepath)
        self.filepath.touch(exist_ok=True)
        if load:
            self.load()
        else:
            self.clear()

    def create(self):
        # self.populate(data)
        self.save()

    def clear(self):
        self.data = []

    def load(self): 
        try:
            with open(self.filepath) as fp:
                self.data = [
                    Game.from_dict(game)
                    for game in
                    json.load(fp)
                ]
        except json.JSONDecodeError as jde:
            if jde.doc == '':
                self.data = []
            else:
                raise

    def save(self):
        with open(self.filepath, 'w') as fp:
            json.dump(
                [row.to_dict() for row in self.rows()], 
                fp
            )

    def add(self, date:str, title:str):
        self.data.append(Game(date, title))

    def populate(self, data):
        for date, title in data:
            self.add(date, title)
    
    def rows(self) -> list[Game]:
        return [row for row in self.data]
    
    def titles(self, natural=False) -> list[str]:
        if natural:
            return [self.natural(row.title.lower()) for row in self.rows()]
        else:
            return [row.title.lower() for row in self.rows()]
        
    def find_title(self, title:str) -> str:
        found = [_title for _title in self.titles()
                if _title.lower() == title.lower()]
        return found[0] if found else None
    
    def find_titles_like(self, contains:str) -> list[str]:
        return [title for title in self.titles()
                if contains.lower() in title.lower()]
    
