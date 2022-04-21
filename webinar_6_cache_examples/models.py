from dataclasses import asdict, dataclass


@dataclass
class Person:
    id: int
    last_name: str
    first_name: str
    age: int
    city: str

    def as_dict(self) -> dict:
        return asdict(self)