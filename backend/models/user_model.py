from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class User:
    id: int
    username: str
    password_hash: str
    full_name: str
    is_active: bool
    created_at: datetime
    role: str
    must_change_password: bool

    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))

    def to_safe_dict(self):
        data = asdict(self)
        data.pop("password_hash", None)
        return data