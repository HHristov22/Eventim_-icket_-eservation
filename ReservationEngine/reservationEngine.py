import sqlite3
from DatabaseConnecting import DatabaseConnecting
from Reservation import Reservation
from Preferences import Preferences

def main():
    pref = Preferences("userPref.txt")
    userPreferencesList = pref.createUserPreferencesList()

    database = DatabaseConnecting("eventDatabase.db")
    eventsList = database.getEventList()
    numberOfEvents = database.getNumberOfEvents()

    res = Reservation(userPreferencesList)
    res.reservation(eventsList, numberOfEvents)

if __name__ == "__main__":
    main()