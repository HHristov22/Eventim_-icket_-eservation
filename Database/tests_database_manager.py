import unittest
from database_manager import Database
from user_data import UserData
import database_constants as dbc
import os

DATABASE_FILEPATH = "test_database.db"

class TestDatabase(unittest.TestCase) :

    def test_integration(self) :
        db = Database(DATABASE_FILEPATH)
        
        testUser = UserData("testUser", "testPassword", "testEventimEmail", "testEventimPassword")
        db.insertUser(testUser)

        user = db.getUser("testUser")
        self.assertEqual(user, testUser, "Inserted user not found")

        users = db.getAllUsers()
        self.assertIn(testUser, users, "Get all user doesn't work")

        testUpdatedUser = UserData("testUpdatedUser", "testUpdatedPassword", "testUpdatedEventimEmail", "testUpdatedEventimPassword")
        db.updateUser(testUser.username, testUpdatedUser)

        users = db.getAllUsers()
        self.assertIn(testUpdatedUser, users, "Did not update user")

        db.deleteUser(testUpdatedUser.username)

        users = db.getAllUsers()
        self.assertNotIn(testUser, users, "Did not delete user")
        
def removeDatabaseFile() :
    if os.path.exists(DATABASE_FILEPATH) :
            os.remove(DATABASE_FILEPATH)

if __name__ == '__main__':
    removeDatabaseFile()
    unittest.main()
    removeDatabaseFile()