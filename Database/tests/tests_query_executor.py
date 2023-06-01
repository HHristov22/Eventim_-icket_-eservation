import unittest
import sys
sys.path.append('..')
from query_executor import QueryExecutor
import os
import sqlite3

DATABASE_FILEPATH = "test_database.db"

class QueryExecutorUnitTests(unittest.TestCase) :

    def test__init__(self) :
        removeDatabaseFile()
        executor = QueryExecutor(DATABASE_FILEPATH)

        self.assertIsInstance(executor.connection, sqlite3.Connection, "Did not create connection")
        self.assertIsInstance(executor.cursor, sqlite3.Cursor, "Did not create cursor")

    def testExecuteAndFetch(self) :
        removeDatabaseFile()
        executor = QueryExecutor(DATABASE_FILEPATH)
        executor.execute("CREATE TABLE table1 (column1 TEXT)")
        executor.execute("SELECT name FROM sqlite_master")
        result = executor.fetch()
        self.assertIn("table1", result)

    def testFetchall(self) :
        removeDatabaseFile()
        executor = QueryExecutor(DATABASE_FILEPATH)
        executor.execute("CREATE TABLE table1 (column1 TEXT);")
        executor.execute("INSERT INTO table1 ('column1') VALUES ('value1');")
        executor.execute("INSERT INTO table1 ('column1') VALUES ('value2');")
        executor.execute("INSERT INTO table1 ('column1') VALUES ('value3');")
        executor.execute("SELECT * FROM table1")
        result = executor.fetchall()
        expectedResult = [('value1',), ('value2',), ('value3',)]
        self.assertEqual(result, expectedResult)
         

    def test__del__(self) :
        removeDatabaseFile()
        executor = QueryExecutor(DATABASE_FILEPATH)
        executor.execute("CREATE TABLE table1 (column1 TEXT)")

        executor = QueryExecutor(DATABASE_FILEPATH)
        executor.execute("SELECT name FROM sqlite_master")
        result = executor.fetch()
        self.assertIn("table1", result)

def removeDatabaseFile() :
    if os.path.exists(DATABASE_FILEPATH) :
            os.remove(DATABASE_FILEPATH)

if __name__ == '__main__':
    unittest.main()
    removeDatabaseFile()