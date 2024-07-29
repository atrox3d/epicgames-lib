from dataclasses import dataclass, asdict

@dataclass
class Game:
    date: str
    title: str
    id: int = None

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, game_dict):
        return cls(**game_dict)

