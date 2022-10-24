import os
from time import sleep
from typing import Optional

from utils import SqliteOpen


def execute_sql(
    name: str, query: Optional[str] = None
) -> tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]]:
    print(f"INFO: Executing {name}")
    sleep(0.25)  # Emulating db connection latency

    with SqliteOpen(os.getenv("DB_PATH")) as sql:
        conn, csr = sql
        csr.execute(query)
        return (name, tuple([i[0] for i in csr.description]), tuple(csr.fetchall()))
