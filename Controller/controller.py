import sys
sys.path.append('..')
from Database.database_manager import Database
from data_types import Preference
from data_types import EventimEvent

DATABASE_FILE_PATH = "eventim.db"

HOME_PAGE = 0
PREF_PAGE = 1
EVENT_PAGE = 2
EXIT_LOOP = -1

class Controler :
    
    def __init__(self) -> None :
        self.db = Database(DATABASE_FILE_PATH)
        self.currentPage = 0
        self.mainLoop()


    def __mainLoop(self) -> None :
        
        while self.currentPage != EXIT_LOOP :
            if self.currentPage == HOME_PAGE :
                self.__launchHomePage()
            elif self.currentPage == PREF_PAGE :
                self.__launchPrefPage()
            elif self.currentPage == EVENT_PAGE :
                self.__launchEventPage()

    def __launchHomePage(self) :
        prefs = self.db.getPreference()
        # launch home page from GUI
        # arguments (Preference) - (current preference)
        # returns nextPage - which is the next page chosen by the user

        homePageResponse = gui.launchHomePage(prefs)
        self.currentPage = homePageResponse

    def __launchPrefPage(self) :
        prefs = self.db.getPreference()
        # launch preference page from GUI
        # arguments (Preference) - (current preference)
        # returns [bool, Preference] - [if the preferences are changed, the new preferences]

        prefPageResponse = gui.launchPrefPage(prefs)
        if prefPageResponse[0] :
            self.db.setPreference(prefPageResponse[1])
        
        self.currentPage = HOME_PAGE

    def __launchEventPage(self) :
        # calls to EventExtractor to do its thing(fill the database with events)
        eventExtractor() 

        eventList = self.db.getAllEventimEvent()
        self.db.deleteAllEventimEvents()

        # launch event page from GUI
        # arguments (list) - (list of events)
        # return string - link to the event that should be reserved(=="" if none is chosen)

        eventPageResponse = gui.launchEventPage(eventList)
        if eventPageResponse == "" :
            self.currentPage = HOME_PAGE
            return
        
        # send link to reservation engine to open the page
        self.currentPage = -1
        reservationEngine.open(eventPageResponse)

    def __getEvents(self) -> list :
        eventList = self.db.getAllEventimEvent() 
        
        return eventList
    
