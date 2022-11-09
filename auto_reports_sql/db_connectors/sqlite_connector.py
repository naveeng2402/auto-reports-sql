import sqlite3


class SqliteConnector:
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return (self.connection, self.cursor)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
