import os
import sqlite3


class DatabaseConnection:
    DB_PATH = os.path.join(
        os.path.dirname(__file__),
        "../phonebook_project/db.sqlite3",
    )

    def __enter__(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect(self.DB_PATH)
        return self.connection.cursor()

    def __exit__(self, *args):
        self.connection.close()
