import os
from time import sleep
from concurrent.futures import ThreadPoolExecutor

from utils import SqliteOpen


def execute_single_query(
    query: str,
) -> tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]]:
    print(f"INFO: Executing {query}")
    sleep(0.25)  # Emulating db connection latency

    with SqliteOpen(os.getenv("DB_PATH")) as sql:
        conn, csr = sql
        csr.execute(query)
        return (query, tuple([i[0] for i in csr.description]), tuple(csr.fetchall()))


def execute_sql(
    max_workers: int, name: str, query: list[str]
) -> tuple[str, tuple[tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]], ...]]:
    with ThreadPoolExecutor(max_workers=max_workers) as exe:
        res = exe.map(execute_single_query, query)

    """For testing performance"""
    # res = []
    # for q in query:
    #     res.append(execute_single_query(q))

    return (name, tuple(res))
