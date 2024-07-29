from dataclasses import dataclass, asdict

@dataclass
class Game:
    date: str
    title: str
    id: int = None

    def dict(self):
        return asdict(self)
