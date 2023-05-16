import sqlite3

class DatabaseConnecting:
    def __init__(self, databaseName):
        self.databaseName = databaseName;
        
    def openDataBase(self):
        conn = sqlite3.connect(self.databaseName)
        cursor = conn.execute("SELECT type, name, location, date, time, price, availability from EVENT")
        return cursor

    def getEventList(self):
        cursor = self.openDataBase()
        eventList = cursor.fetchall()
        return eventList

    def getNumberOfEvents(self):
        eventList = self.getEventList()
        return len(eventList)

class Preferences:
    
    def __init__(self, filename):
        self.filename = filename    
        
    def createUserPreferencesList(self):
        fileWithUserPrefs = open(self.filename, "r", encoding = 'utf-8-sig')
        lines = fileWithUserPrefs.readlines()
        fileWithUserPrefs.close()
        
        tempList = []
        for line in lines:
            line = line.split(',')
            line = [i.strip() for i in line]
            tempList.append(line);
            
        return tempList
        # (tempList[0] = types, tempList[1] = dates, tempList[2] = times, tempList[3] = numberOfTickets, tempList[4] = priceRange) 

class Reservation:
    def __init__(self, preferencesList):
        self.preferencesList = preferencesList
        
    def checkEvent(self, event):
        return  event[0] in self.preferencesList[0] and \
                event[3] in self.preferencesList[1] and \
                event[4] in self.preferencesList[2] and \
                event[5] > int(self.preferencesList[4][0]) and event[5] < int(self.preferencesList[4][1]) and \
                event[6] > int(max(self.preferencesList[3]))
    
    def savePreferredEventToFile (self, event):
        f = open("preferredEvents.txt", "a")
        for i in range(len(event)):
            f.write(str(event[i]) + ' ')
            
        f.write("\n")
        f.close()
    
    def reservation(self, eventsList, numberOfEvents):
        for i in range(numberOfEvents):
            if(self.checkEvent(eventsList[i])):
                self.savePreferredEventToFile(eventsList[i])
                print("Reservation...")
                
                
pref = Preferences ("userPref.txt")
userPreferencesList = pref.createUserPreferencesList()

database = DatabaseConnecting("eventDatabase.db")
eventsList = database.getEventList()
numberOfEvents = database.getNumberOfEvents()

res = Reservation(userPreferencesList)
res.reservation(eventsList, numberOfEvents)

