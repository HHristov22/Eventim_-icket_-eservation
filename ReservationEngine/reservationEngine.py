import sqlite3

def openDataBase(database):
    conn = sqlite3.connect(database)
    return conn

def createCursor(database):
    conn = openDataBase(database)
    cursor = conn.execute("SELECT type, name, location, date, time, price, availability from EVENT")
    return cursor

def getEventList(database):
    cursor = createCursor(database)
    eventsList = cursor.fetchall()
    return eventsList

def getNumberOfEvents(database):
    cursor = createCursor(database)
    eventsList = cursor.fetchall()
    return len(eventsList)

class Preferences:

    def __init__(self, types, dates, times, numberOfTickets, priceRange):
        self.types = types
        self.dates = dates
        self.times = times
        self.numberOfTickets = numberOfTickets
        self.priceRange = priceRange
    
def initUserPreferences():
    fileWithUserPrefs = open("userPref.txt", "r", encoding = 'utf-8-sig')
    lines = fileWithUserPrefs.readlines()
    fileWithUserPrefs.close()

    preferencesDict = {}
    my_list = []
    for line in lines:
        line = line.split(',')
        line = [i.strip() for i in line]
        my_list.append(line);

    return Preferences(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4]) 

def savePreferredEventToFile (event):
    f = open("preferredEvents.txt", "a")
    for i in range(len(event)):
        f.write(str(event[i]) + ' ')
        
    f.write("\n")
    f.close()

def reservation(numberOfEvents, eventsList, userPreferences):
    for i in range(numberOfEvents):
        if  eventsList[i][0] in userPreferences.types and \
            eventsList[i][3] in userPreferences.dates and \
            eventsList[i][4] in userPreferences.times and \
            eventsList[i][5] > int(userPreferences.priceRange[0]) and eventsList[i][5] < int(userPreferences.priceRange[1]) and\
            eventsList[i][6] > int(max(userPreferences.numberOfTickets)):
            savePreferredEventToFile(eventsList[i])
            print("Reservation...")
        
numberOfEvents = getNumberOfEvents('eventDatabase.db')
eventsList = getEventList('eventDatabase.db')
userPreferences = initUserPreferences()
reservation(numberOfEvents, eventsList, userPreferences)
