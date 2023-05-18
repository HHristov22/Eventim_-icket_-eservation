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
    city = "София" # todo
    prefferedDateAndTime = "2023-05-19T19:00:00+03:00" # todo
    res.reservation(city, eventsList, numberOfEvents, prefferedDateAndTime)

if __name__ == "__main__":
    main()