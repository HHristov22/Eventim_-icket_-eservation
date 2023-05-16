import unittest
from query_creator import QueryCreator

class QueryCreatorUnitTests(unittest.TestCase) :

    def testCreateTable(self) :
        columnNameAndDefinitionPairs = list()
        columnNameAndDefinitionPairs.append(("column1", "TEXT NOT NULL"))
        columnNameAndDefinitionPairs.append(("column2", "INT PRIMARY KEY"))
        columnNameAndDefinitionPairs.append(("column3", "DATE UNIQUE"))
        createdQuery = QueryCreator.createTable("someTable", columnNameAndDefinitionPairs)
        testQuery = "CREATE TABLE IF NOT EXISTS someTable (column1 TEXT NOT NULL, column2 INT PRIMARY KEY, column3 DATE UNIQUE);"
        self.assertEqual(createdQuery, testQuery)

    def testDropTable(self) :
        createdQuery = QueryCreator.dropTable("someTable")
        testQuery = "DROP TABLE IF EXISTS 'someTable';"
        self.assertEqual(createdQuery, testQuery)

    def testInsertInto(self) :
        columnValuePairs = list()
        columnValuePairs.append(("column1", "value1"))
        columnValuePairs.append(("column2", "value2"))
        columnValuePairs.append(("column3", "value3"))
        createdQuery = QueryCreator.insertInto("someTable", columnValuePairs)
        testQuery = "INSERT INTO 'someTable' ('column1', 'column2', 'column3') VALUES ('value1', 'value2', 'value3');"
        self.assertEqual(createdQuery, testQuery)
    
    def testSelect(self) :
        createdQuery = QueryCreator.select("someTable", ['someColumn','*','ROWID'])
        testQuery = "SELECT 'someColumn', *, 'ROWID' FROM 'someTable';"
        self.assertEqual(createdQuery, testQuery)

    def testSelectWithCondition(self) :
        sqlCondition = "'someOtherColumn'='someOtherValue'"
        createdQuery = QueryCreator.select("someTable", ['someColumn','*','ROWID'], sqlCondition)
        testQuery = "SELECT 'someColumn', *, 'ROWID' FROM 'someTable' WHERE 'someOtherColumn'='someOtherValue';"
        self.assertEqual(createdQuery, testQuery)

    def testDelete(self) :
        createdQuery = QueryCreator.delete('someTable', "'someColumn'='someValue'")
        testQuery = "DELETE FROM 'someTable' WHERE 'someColumn'='someValue';"
        self.assertEqual(createdQuery, testQuery)
    
    def testUpdate(self) :
        columnValuePairs = list()
        columnValuePairs.append(("column1", "value1"))
        columnValuePairs.append(("column2", "value2"))
        columnValuePairs.append(("column3", "value3"))
        createdQuery = QueryCreator.update("someTable", columnValuePairs, "'column3'='someValue'")
        testQuery = "UPDATE 'someTable' SET 'column1'='value1', 'column2'='value2', 'column3'='value3' WHERE 'column3'='someValue';"
        self.assertEqual(createdQuery, testQuery)

if __name__ == '__main__':
    unittest.main()