from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Product:
    barcode: int
    sku: str
    name: str
    category: str
    unit: str
    reorder_level: int
    quantity: int
    location: str
    zone: int
    bin: int

    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))

    def to_dict(self):
        return asdict(self)


@dataclass
class All_Product:
    barcode: int
    sku: str
    name: str
    category: str
    unit: str
    reorder_level: int
    quantity: int
    location: str
    zone: str
    bin: str
    status: str

    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))

    def to_dict(self):
         return asdict(self)


@dataclass
class Stock_Level:
    product_id: int
    location_id: str
    quantity: int
    bin_id: str

    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))

    def to_dict(self):
        return asdict(self)
