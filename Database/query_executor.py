import sqlite3 as sql

class QueryExecutor :

    def __init__(self, databaseFilePath) -> None :
        self.connection = sql.connect(databaseFilePath)
        self.cursor = self.connection.cursor()
        self.result = None

    def __del__(self) -> None :
        self.connection.commit()
        self.connection.close()

    def execute(self, query : str) :
        self.result = self.cursor.execute(query)
        return self

    def fetch(self) :
        return self.result.fetchone()


    def fetchall(self) :
        return self.result.fetchall()