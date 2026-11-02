from dataclasses import dataclass, asdict

@dataclass
class Product:
    location: str
    barcode: str
    name: str
    category: str
    unit: str
    reorder_level: int
    quantity: int

    def to_dict(self):
        return asdict(self)