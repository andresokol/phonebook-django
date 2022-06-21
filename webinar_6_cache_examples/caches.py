import time
from typing import List, Dict, Tuple

from db import DatabaseConnection
from models import Person


class PersonsCache:
    TTL = 10  # seconds

    def __init__(self) -> None:
        self._data: List[Person] = []
        self._last_updated: int = 0

    def get(self) -> List[Person]:
        with DatabaseConnection() as connection:
            connection.execute("SELECT * FROM phonebook_app_person")
            data = connection.fetchall()

        return [Person(*values) for values in data]

    def get_cached(self) -> List[Person]:
        cache_age = time.time() - self._last_updated
        print(f"Cache age: {cache_age} seconds")

        if self.TTL < cache_age:
            self._data = self.get()
            self._last_updated = time.time()
            print("Cache updated")

        return self._data


persons_cache = PersonsCache()


class ByCityCache:
    TTL = 10  # seconds
    KeyT = Tuple[str, int]
    ValueT = Tuple[int, List[Person]]

    def __init__(self) -> None:
        self._data: Dict[self.KeyT, self.ValueT] = {}

    def get(self, city: str, age: int) -> List[Person]:
        with DatabaseConnection() as connection:
            connection.execute(
                "SELECT * FROM phonebook_app_person WHERE city = ? AND age = ?",
                (city, age,)
            )
            data = connection.fetchall()

        return [Person(*values) for values in data]

    def get_cached(self, city: str, age: int) -> List[Person]:
        key = f"{city}${age}"

        updated_at, data = self._data[key] if city in self._data else (0, [])

        cache_age = time.time() - updated_at
        print(f"Cache age: {cache_age} seconds")

        if self.TTL < cache_age:
            data = self.get(city, age)
            self._data[city, age] = (time.time(), data)
            print("Cache updated")

        return data


by_city_cache = ByCityCache()
