import time
from typing import List, Dict, Tuple

from db import DatabaseConnection
from models import Person


class PersonsCache:
    TTL = 10  # seconds

    def __init__(self) -> None:
        ...

    def get(self) -> List[Person]:
        with DatabaseConnection() as connection:
            connection.execute("SELECT * FROM phonebook_app_person")
            data = connection.fetchall()

        return [Person(*values) for values in data]

    def get_cached(self) -> List[Person]:
        cache_age = ...
        print(f"Cache age: {cache_age} seconds")

        ...


persons_cache = PersonsCache()
