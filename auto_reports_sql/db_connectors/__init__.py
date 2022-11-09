from .sqlite_connector import SqliteConnector
from .postgres_connector import PostgresConnector
from .mysql_connector import MySqlConnector

import os
from typing import Union


def get_db_connector() -> Union[SqliteConnector, PostgresConnector, MySqlConnector]:
    db = os.getenv("db")
    if db == "sqlite":
        return SqliteConnector(os.getenv("db_path"))
    elif db == "mysql":
        return MySqlConnector(
            host=os.getenv("host"),
            username=os.getenv("username"),
            password=os.getenv("password"),
            database=os.getenv("db_name"),
        )
    else:
        return PostgresConnector(
            host=os.getenv("host"),
            username=os.getenv("username"),
            password=os.getenv("password"),
            database=os.getenv("db_name"),
        )
