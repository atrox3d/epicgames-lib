import json
from pathlib import Path
from .db import Db

class JsonDb(Db):
    
    def __init__(self, filepath:str, load=False) -> None:
        self.filepath = Path(filepath)
        if load:
            self.load()
        else:
            self.data = []

    def create(self):
        # self.filepath.touch(exist_ok=True)
        self.data = []
        self.save()

    def load(self):
        with open(self.filepath) as fp:
            self.data = json.load(fp)

    def save(self):
        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)

    def add(self, date:str, title:str):
        self.data.append(dict(date=date, title=title))

    def populate(self, data):
        for date, title in data:
            self.add(date, title)
    
    def rows(self) -> list[list[str]]:
        return (row for row in self.data)
    
    def titles(self) -> list[str]:
        return [row['title'] for row in self.rows()]
        
    def find_title(self, title:str) -> str:
        found = [_title for _title in self.titles()
                if _title.lower() == title.lower()]
        return found[0] if found else None
    
    def title_like(self, contains:str) -> list[str]:
        return [title for title in self.titles()
                if contains.lower() in title.lower()]
    
