import sqlite3

class DatabaseConnecting:
    def __init__(self, databaseName):
        self.databaseName = databaseName
        
    def openDataBase(self):
        try:
            conn = sqlite3.connect(self.databaseName)
            cursor = conn.execute("SELECT type, name, location, date, time, price, availability from EVENT")
            return cursor
        except sqlite3.Error as e:
            print("Error opening the database:", str(e))
            return None

    def getEventList(self):
        cursor = self.openDataBase()
        if cursor:
            eventList = cursor.fetchall()
            return eventList
        else:
            return []

    def getNumberOfEvents(self):
        eventList = self.getEventList()
        return len(eventList)