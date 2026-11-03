from dataclasses import dataclass, asdict

@dataclass
class Location:
    id: int
    code: str
    name: str
    is_active: bool

    def to_dict(self):
        return asdict(self)