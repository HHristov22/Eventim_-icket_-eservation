import unittest
import sys
sys.path.append('..')
sys.path.append('../..')
from database_manager import Database
from data_types import User
from data_types import EventimEvent
from data_types import Preference
import database_constants as dbc
import os

DATABASE_FILEPATH = "test_database.db"

class TestDatabase(unittest.TestCase) :

    def test_userIntegration(self) :
        db = Database(DATABASE_FILEPATH)
        
        testUser = User("testEventimEmail", "testEventimPassword")
        db.setUser(testUser)

        user = db.getUser()
        self.assertEqual(user, testUser, "Set user not found")

        otherUser = User("testOtherEventimEmail", "testOtherEventimPassword")
        db.setUser(otherUser)

        user = db.getUser()
        self.assertEqual(user, otherUser, "New set user not found")

        db.deleteUser()
        user = db.getUser()
        self.assertEqual(user, None, "User not deleted")

    def test_eventIntegration(self) : 
        db = Database(DATABASE_FILEPATH)

        testEvent0 = EventimEvent("testName0", "testType0", "Pirotska 5", "02.01.2024", "09:00", 12, 3)
        testEvent1 = EventimEvent("ВСИЧКИ ОБИЧАТ ГАРИ", "Comedy", "Културен дом НХК", "03.29.2020", "11:00", 35, 4)
        testEvent2 = EventimEvent("NO MORE MANY MORE & HANGAR 42", "Music", "Клуб Строежа", "02.04.2023", "15:00", 68, 5)
        db.insertEventimEvent(testEvent0)
        db.insertEventimEvent(testEvent1)
        db.insertEventimEvent(testEvent2)
        
        testEventList = db.getAllEventimEvent()
        self.assertEqual(testEvent0, testEventList[0], "Eventim event 0 not found")
        self.assertEqual(testEvent1, testEventList[1], "Eventim event 1 not found")
        self.assertEqual(testEvent2, testEventList[2], "Eventim event 2 not found")

        db.deleteAllEventimEvents()

        testEventList = db.getAllEventimEvent()
        self.assertEqual(len(testEventList), 0, "Eventim event deleting not working")

    def test_preferenceIntegration(self) :
        db = Database(DATABASE_FILEPATH)

        testPref = Preference(
            ['Concert', 'sport'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            ['10:00', '11:00', '15:00'],
            1, 10, 100)
        
        db.setPreference(testPref)
        pref = db.getPreference()
        self.assertEqual(testPref, pref, "Set preference not found")

        testPref = Preference(
            ['Music', 'sport'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            ['10:00', '12:00', '15:00'],
            1, 10, 100)
        db.setPreference(testPref)
        pref = db.getPreference()
        self.assertEqual(pref, testPref, "New set preference not found")

        db.deletePreference()
        pref = db.getPreference()
        self.assertEqual(pref, None, "New set preference not found")

        
def removeDatabaseFile() :
    if os.path.exists(DATABASE_FILEPATH) :
            os.remove(DATABASE_FILEPATH)

if __name__ == '__main__':
    removeDatabaseFile()
    unittest.main()
    removeDatabaseFile()