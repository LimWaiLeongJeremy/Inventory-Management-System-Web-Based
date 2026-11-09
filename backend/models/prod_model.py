from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Product:
    id: int
    barcode: str
    name: str
    category: str
    unit: str
    reorder_level: int
    created_at: datetime
    restock_at: datetime
    quantity: int
    location: str

    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))

    def to_dict(self):
        return asdict(self)