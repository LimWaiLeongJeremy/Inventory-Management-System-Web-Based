from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class User:
    username: str
    password: str
    full_name: str
    is_active: bool
    create_at: datetime
    role: str
    must_change_password: bool

    def to_dict(self):
        return asdict(self)