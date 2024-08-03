from abc import ABC, abstractmethod
from pathlib import Path

class Db(ABC):

    @abstractmethod
    def create(self): pass

    # @abstractmethod
    # def load(self): pass

    # @abstractmethod
    # def save(self): pass

    @abstractmethod
    def add(self, date, title): pass

    @abstractmethod
    def populate(self, data): pass

    @abstractmethod
    def rows(self): pass

    @abstractmethod
    def titles(self): pass

    @abstractmethod
    def find_title(self, title): pass

    @abstractmethod
    def find_titles_like(self, contains): pass
