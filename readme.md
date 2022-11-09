# SQL Automation

This is a simple tool to run a set of sql queries and generate a HTML report of the results

# How to use the tool

### Install the tool using pip

```bash
pip install auto-reports-sql
```

### Create a json file with the following schema

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "required": ["name", "query"],
    "properties": {
      "name": {
        "type": "string",
        "pattern": "^.*$"
      },
      "query": {
        "type": "array",
        "items": {
          "type": "string",
          "pattern": "^.*$"
        }
      }
    }
  }
}
```

> Example

```json
[
  {
    "name": "First 10 data",
    "query": [
      "select * from Person limit 10",
      "select * from Person order by name desc limit 10"
    ]
  }
]
```

### Run the program with the following command

```
Usage: auto-reports-sql execute [OPTIONS] QUERIES

Options:
  -t, --threads INTEGER           No. of threads used for computation
                                  [default: 10]
  -rt, --report-title TEXT        Title of the generated report.  [default: Report Title]
  -d, --db [sqlite|mysql|postgres]
                                  The database which is used.  [required]
  -dp, --db-path PATH             Sqlite database path. Only required if the
                                  database is set to 'sqlite'
  -h, --host TEXT                 host of the database. Only required if the
                                  database is not set to 'sqlite'
  -u, --username TEXT             username to access the database. Only
                                  required if the database is not set to
                                  'sqlite'
  -p, --password TEXT             password of the database. Only required if
                                  the database is not set to 'sqlite'
  -n, --db-name TEXT              name of the database. Only required if the
                                  database is not set to 'sqlite'
  --config FILE                   Read configuration from FILE.
  --help                          Show this message and exit.
```

# Report Examples

![Screenshot](https://github.com/naveeng2402/auto-reports-sql/raw/master/images/report.jpg)

# Possible Updates

- Errors in the queries are not taken into account
