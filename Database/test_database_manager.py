import unittest
import sqlite3
import os
from database_manager import Database
from user_data import UserData

gDatabaseFilePath = "test_database.db"

def removeDatabaseFile() :
    if os.path.exists(gDatabaseFilePath) :
            os.remove(gDatabaseFilePath)

class TestDatabase(unittest.TestCase) :

    def test_initialize(self) :
        removeDatabaseFile()
        db = Database()

        db.initialize(gDatabaseFilePath)

        self.assertIsInstance(db.connection, sqlite3.Connection, "Did not create connection")
        self.assertIsInstance(db.cursor, sqlite3.Cursor, "Did not create cursor")

        tableNames = db.getAllTableNames()
        self.assertIn("users", tableNames, "Did not create users table")

        db.commitAndCloseConnection()

    def test_removeTable(self) :
        removeDatabaseFile()
        db = Database()
        db.initialize(gDatabaseFilePath)

        db.removeTable("users")

        tableNames = db.getAllTableNames()
        self.assertNotIn("users", tableNames, "Did not drop table")

        db.commitAndCloseConnection()

    def test_insertUser(self) :
        removeDatabaseFile()
        db = Database()
        db.initialize(gDatabaseFilePath)
        testUser = UserData("testUser", "testPassword", "testEventimEmail", "testEventimPassword")
        
        db.insertUser(testUser)

        users = db.getAllUsers()
        self.assertIn(testUser, users, "Did not insert user")
        
        db.commitAndCloseConnection()
         

    def test_DeleteUser(self) :
        removeDatabaseFile()
        db = Database()
        db.initialize(gDatabaseFilePath)
        testUser = UserData("testUser", "testPassword", "testEventimEmail", "testEventimPassword")
        db.insertUser(testUser)

        db.deleteUser(testUser.username)

        users = db.getAllUsers()
        self.assertNotIn(testUser, users, "Did not delete user")
        
        db.commitAndCloseConnection()

    def test_updateUser(self) :
        removeDatabaseFile()
        db = Database()
        db.initialize(gDatabaseFilePath)
        testUser = UserData("testUser", "testPassword", "testEventimEmail", "testEventimPassword")
        testUpdatedUser = UserData("testUpdatedUser", "testUpdatedPassword", "testUpdatedEventimEmail", "testUpdatedEventimPassword")
        db.insertUser(testUser)

        db.updateUser(testUser.username, testUpdatedUser)

        users = db.getAllUsers()
        self.assertIn(testUpdatedUser, users, "Did not update user")

        db.commitAndCloseConnection()
    

if __name__ == '__main__':
    unittest.main()