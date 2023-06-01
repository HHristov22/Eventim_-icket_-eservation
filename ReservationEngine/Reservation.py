from booking import Booking

'''
Reservation class calls Booking`s method to make the reservation 
The formatingLocation method does format the location. Put them '-'
The checkEvent method checks if event is preffered by preferences of user

'''

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
            
    def formattingLocation(self, rowLocation):
        formattedSentence = "-".join(rowLocation.split())
        return formattedSentence

    def reservation(self, city, eventsList, numberOfEvents, prefferedDateAndTime):
        for i in range(numberOfEvents):
            try:
                if self.checkEvent(eventsList[i]):
                    self.savePreferredEventToFile(eventsList[i])
                    eventName = eventsList[i][1]
                    formatedEventLocation = self.formattingLocation(eventsList[i][2])
                    book = Booking()
                    book.booking(city, eventName, formatedEventLocation, prefferedDateAndTime)
            except Exception as e:
                print("Error occurred during the reservation process: ", str(e))


