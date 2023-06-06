from data_types import EventimEvent
from data_types import Preference
from Database.database_manager_interface import DatabaseInterface
from  Database.query_creator import QueryCreator
from  Database.query_executor import QueryExecutor
import  Database.database_constants as dbc

class Database(DatabaseInterface) :

    def __init__(self, databaseFilePath : str) -> None:
        self.executor = QueryExecutor(databaseFilePath)
        self._createEventimEventTableIfNotPresent()
        self._createPreferenceTableIfNotPresent()

    def _createEventimEventTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        for columnName in dbc.EVENT_TABLE_COLUMN_NAMES :
            columnNamesAndDefinitionPairs.append((columnName, "TEXT"))
        query = QueryCreator.createTable(dbc.EVENT_TABLE_NAME, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def insertEventimEvent(self, eventimEvent : EventimEvent) :
        columnValuePairs = list()
        for index in range(0, len(dbc.EVENT_TABLE_COLUMN_NAMES))  :
            columnValuePairs.append((dbc.EVENT_TABLE_COLUMN_NAMES[index], eventimEvent[index]))
        query = QueryCreator.insertInto(dbc.EVENT_TABLE_NAME, columnValuePairs)
        self.executor.execute(query)
    
    def getAllEventimEvent(self) -> list :
        eventimEvents = list()
        query = QueryCreator.select(dbc.EVENT_TABLE_NAME, ['*','ROWID'])
        eventsFromDatabase = self.executor.execute(query).fetchall()

        for eventFromDatabase in eventsFromDatabase :
            newEvent = EventimEvent()
            for index in range(0, len(eventFromDatabase)) :
                newEvent[index] = eventFromDatabase[index]
            eventimEvents.append(newEvent)
        
        return eventimEvents
    
    def deleteAllEventimEvents(self) :
        query = QueryCreator.delete(dbc.EVENT_TABLE_NAME, "")
        self.executor.execute(query)

    def _createPreferenceTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        for columnName in dbc.PREFERENCE_TABLE_COLUMN_NAMES :
            columnNamesAndDefinitionPairs.append((columnName, "TEXT"))
        query = QueryCreator.createTable(dbc.PREFERENCE_TABLE_NAME, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def setPreference(self, pref : Preference) :
        self.deletePreference()
        columnValuePairs = list()
        for index in range(0, len(dbc.PREFERENCE_TABLE_COLUMN_NAMES)) :
            value = ""
            if isinstance(pref[index], list) :
                value = ";".join(pref[index])
            else :
                value = pref[index] 
            columnValuePairs.append((dbc.PREFERENCE_TABLE_COLUMN_NAMES[index], value))
        query = QueryCreator.insertInto(dbc.PREFERENCE_TABLE_NAME, columnValuePairs)
        self.executor.execute(query)

    def getPreference(self) :
        query = QueryCreator.select(dbc.PREFERENCE_TABLE_NAME, ['*'], "")
        result = self.executor.execute(query).fetch()
        if result == None :
            return None
        return Preference(result[0].split(";"), result[1].split(";"), result[2].split(";"), result[3].split(";"), int(result[4]))
    
    def deletePreference(self) :
        query = QueryCreator.delete(dbc.PREFERENCE_TABLE_NAME, "")
        self.executor.execute(query)