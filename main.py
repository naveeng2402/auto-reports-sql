import os
import sys
from concurrent.futures import ThreadPoolExecutor

import dotenv

import utils


def main(queries: tuple[dict[str, str]], report_title: str):
    try:
        MAX_WORKERS = int(os.getenv("MAX_THREADS"))
    except:
        MAX_WORKERS = 5

    res = []
    print(f"using {MAX_WORKERS} threads")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
        res = exe.map(lambda args: utils.execute_sql(**args), queries)

    """For testing performance"""
    # for query in queries:
    #     res.append(utils.execute_sql(**query))

    utils.generate_report(report_title, res)


if __name__ == "__main__":
    if not os.path.exists(".env.local"):
        print("ERR: '.env.local' is missing.\nPlease look in the documentation")
        sys.exit(1)
    dotenv.load_dotenv(".env.local")

    if len(sys.argv) < 2:
        print("ERR: Please provide a query.json file with the following schema:")
        print(utils.get_schema())
        sys.exit(1)

    if len(sys.argv) > 3:
        print(
            "ERR: Expected one required argument and one optional argument but got more than two arguments"
        )
        sys.exit(1)

    report_title = sys.argv[2] if len(sys.argv) == 3 else "Report"

    if not os.path.exists(sys.argv[1]):
        print(f"ERR: '{sys.argv[1]}' file not found.")
        sys.exit(1)

    is_valid, res = utils.validate_json(sys.argv[1])
    if not is_valid:
        print(f"ERR: {res}")
        sys.exit(1)

    main(res, report_title)
