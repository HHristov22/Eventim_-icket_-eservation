import unittest
import sys
sys.path.append('..')
sys.path.append('../..')
from database_manager import Database
from data_types import EventimEvent
from data_types import Preference
import data_types

import database_constants as dbc
import os

DATABASE_FILEPATH = "test_database.db"

class TestDatabase(unittest.TestCase) :

    def test_eventIntegration(self) : 
        db = Database(DATABASE_FILEPATH)

        testEvent0 = EventimEvent("In Hell with Jesus - Мюзикъл", "Комедия", "Държавен куклен театър Пловдив", "Четвъртък, 15.06.2023 г. в 19:00 ч.", "18,00 лв. - 25,00 лв.", "https1")
        testEvent1 = EventimEvent("ВСИЧКИ ОБИЧАТ ГАРИ", "Comedy", "Културен дом НХК", "03.29.2020 от 11:00", "1,00 лв. - 2,00 лв.", "https2")
        testEvent2 = EventimEvent("NO MORE MANY MORE & HANGAR 42", "Music", "Клуб Строежа", "02.04.2023 от 15:00", "1,50 лв. - 2,50 лв.", "https3")
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
            ['Sofia', 'Plovdiv'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            [data_types.DAY_PART_MORNING, data_types.DAY_PART_EVENING],
            13)
        
        db.setPreference(testPref)
        pref = db.getPreference()
        print(testPref)
        print(pref)
        self.assertEqual(testPref, testPref, "Set preference not found")

        testPref = Preference(
            ['Music', 'sport'],
            ['Sofia'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            [data_types.DAY_PART_MORNING, data_types.DAY_PART_MID_DAY],
            45)
        db.setPreference(testPref)
        pref = db.getPreference()
        self.assertEqual(pref, testPref, "New set preference not found")

        db.deletePreference()
        pref = db.getPreference()
        self.assertEqual(pref, None, "Deleted preference found")

        
def removeDatabaseFile() :
    if os.path.exists(DATABASE_FILEPATH) :
            os.remove(DATABASE_FILEPATH)

if __name__ == '__main__':
    removeDatabaseFile()
    unittest.main()
    removeDatabaseFile()