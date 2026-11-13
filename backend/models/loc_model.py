from dataclasses import dataclass, asdict

@dataclass
class Location:
    id: int
    location_code: str
    name: str
    is_active: bool
    description: str
    address: str
    zone_count: int
    bin_count: int


    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))
        
    def to_dict(self):
        return asdict(self)



@dataclass
class Zone:
    zone: str
    location: str


    # Method to set data from db to model
    @classmethod
    def from_row(cls, columns, row):
        return cls(**dict(zip(columns, row)))
        
    def to_dict(self):
        return asdict(self)