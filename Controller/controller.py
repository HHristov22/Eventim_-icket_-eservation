import sys
sys.path.append('..')
from Database.database_manager import Database
from data_types import Preference
from data_types import EventimEvent
from EventExtractor.eventExtractor import Extractor

#those should be deleted
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DATABASE_FILE_PATH = "eventim.db"

class Controler :
    
    def __init__(self) -> None :
        self.db = Database(DATABASE_FILE_PATH)

    def setPreference(self, pref : Preference) :
        self.db.setPreference(pref)

    def getEvents(self) -> list :
        extractor = Extractor(self.db)
        extractor.saveEvenetsOfPrefferedTypes()
        return self.db.getAllEventimEvent()

def main():
    
    ctrl = Controler()

    #UI MAGIC
    ctrl.setPreference(Preference("concert", "София", "12.06.2023", "evening", 0))
    events = ctrl.getEvents()

    #UI MAGIC
    chosenEvent = (EventimEvent)(events[0]).link
    print(events[0])

    # call to reservation engine to open the link



if __name__ == "__main__":
    main()  
