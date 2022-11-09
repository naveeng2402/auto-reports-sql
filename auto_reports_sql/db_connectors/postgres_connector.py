import psycopg2
    

class PostgresConnector:
    def __init__(self, host, username, password, database) -> None:
        self.host = host
        self.username= username
        self.password= password
        self.database= database

        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(host=self.host,user=self.username,password=self.password,database=self.database)
        self.cursor = self.connection.cursor()
        return (self.connection, self.cursor)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()