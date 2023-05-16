class Reservation:
    def __init__(self, preferencesList):
        self.preferencesList = preferencesList
        
    def checkEvent(self, event):
        try:
            return (
                event[0] in self.preferencesList[0] and
                event[3] in self.preferencesList[1] and
                event[4] in self.preferencesList[2] and
                event[5] > int(self.preferencesList[4][0]) and event[5] < int(self.preferencesList[4][1]) and
                event[6] > int(max(self.preferencesList[3]))
            )
        except IndexError as e:
            print("Error checking the event:", str(e))
            return False

    def savePreferredEventToFile(self, event):
        try:
            f = open("preferredEvents.txt", "a")
            for i in range(len(event)):
                f.write(str(event[i]) + ' ')
                
            f.write("\n")
            f.close()
        except IOError as e:
            print("Error saving the preferred event to file:", str(e))

    def reservation(self, eventsList, numberOfEvents):
        for i in range(numberOfEvents):
            if self.checkEvent(eventsList[i]):
                self.savePreferredEventToFile(eventsList[i])
                print("Reservation...")
