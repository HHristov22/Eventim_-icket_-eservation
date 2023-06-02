from data_types import User
from data_types import EventimEvent
from data_types import Preference
from database_manager_interface import DatabaseInterface
from query_creator import QueryCreator
from query_executor import QueryExecutor
import database_constants as dbc

class Database(DatabaseInterface) :

    def __init__(self, databaseFilePath : str) -> None:
        self.executor = QueryExecutor(databaseFilePath)
        self._createUsersTableIfNotPresent()
        self._createEventimEventTableIfNotPresent()
        self._createPreferenceTableIfNotPresent()

    def _createUsersTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_EMAIL_COLUMN, dbc.USER_TABLE_EMAIL_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_PASSWORD_COLUMN, dbc.USER_TABLE_PASSWORD_COLUMN_DEFINITION))
        query = QueryCreator.createTable(dbc.USER_TABLE, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def setUser(self, user : User) :
        self.deleteUser()
        columnValuePairs = list()
        columnValuePairs.append((dbc.USER_TABLE_EMAIL_COLUMN, user.email))
        columnValuePairs.append((dbc.USER_TABLE_PASSWORD_COLUMN, user.password))
        query = QueryCreator.insertInto(dbc.USER_TABLE, columnValuePairs)
        self.executor.execute(query)

    def getUser(self) -> User :
        query = QueryCreator.select(dbc.USER_TABLE, ['*'], "")
        result = self.executor.execute(query).fetch()
        if result == None :
            return None
        return User(result[0], result[1])
    
    def deleteUser(self) :
        query = QueryCreator.delete(dbc.USER_TABLE, "")
        self.executor.execute(query)

    def _createEventimEventTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_NAME_COLUMN, dbc.EVENT_TABLE_NAME_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_TYPE_COLUMN, dbc.EVENT_TABLE_TYPE_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_LOCATION_COLUMN, dbc.EVENT_TABLE_LOCATION_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_DATE_COLUMN, dbc.EVENT_TABLE_DATE_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_TIME_COLUMN, dbc.EVENT_TABLE_TIME_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_PRICE_COLUMN, dbc.EVENT_TABLE_PRICE_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.EVENT_TABLE_AVAILABILITY_COLUMN, dbc.EVENT_TABLE_AVAILABILITY_COLUMN_DEFINITION))
        query = QueryCreator.createTable(dbc.EVENT_TABLE, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def insertEventimEvent(self, eventimEvent : EventimEvent) :
        columnValuePairs = list()
        columnValuePairs.append((dbc.EVENT_TABLE_NAME_COLUMN, eventimEvent.name))
        columnValuePairs.append((dbc.EVENT_TABLE_TYPE_COLUMN, eventimEvent.type))
        columnValuePairs.append((dbc.EVENT_TABLE_LOCATION_COLUMN, eventimEvent.location))
        columnValuePairs.append((dbc.EVENT_TABLE_DATE_COLUMN, eventimEvent.date))
        columnValuePairs.append((dbc.EVENT_TABLE_TIME_COLUMN, eventimEvent.time))
        columnValuePairs.append((dbc.EVENT_TABLE_PRICE_COLUMN, eventimEvent.price))
        columnValuePairs.append((dbc.EVENT_TABLE_AVAILABILITY_COLUMN, eventimEvent.availability))
        query = QueryCreator.insertInto(dbc.EVENT_TABLE, columnValuePairs)
        self.executor.execute(query)
    
    def getAllEventimEvent(self) -> list :
        eventimEvents = list()
        query = QueryCreator.select(dbc.EVENT_TABLE, ['*','ROWID'])
        eventsFromDatabase = self.executor.execute(query).fetchall()

        for eventFromDatabase in eventsFromDatabase :
            newEvent = EventimEvent(eventFromDatabase[0], eventFromDatabase[1], eventFromDatabase[2],
                                    eventFromDatabase[3], eventFromDatabase[4], int(eventFromDatabase[5]), int(eventFromDatabase[6]))
            eventimEvents.append(newEvent)
        
        return eventimEvents
    
    def deleteAllEventimEvents(self) :
        query = QueryCreator.delete(dbc.EVENT_TABLE, "")
        self.executor.execute(query)

    def _createPreferenceTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_TYPES_COLUMN, dbc.PREFERENCE_TABLE_TYPES_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_DATES_COLUMN, dbc.PREFERENCE_TABLE_DATES_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_HOURS_COLUMN, dbc.PREFERENCE_TABLE_HOURS_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_TICKET_COUNT_COLUMN, dbc.PREFERENCE_TABLE_TICKET_COUNT_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_MIN_PRICE_COLUMN, dbc.PREFERENCE_TABLE_MIN_PRICE_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.PREFERENCE_TABLE_MAX_PRICE_COLUMN, dbc.PREFERENCE_TABLE_MAX_PRICE_COLUMN_DEFINITION))
        query = QueryCreator.createTable(dbc.PREFERENCE_TABLE, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def setPreference(self, pref : Preference) :
        self.deletePreference()
        columnValuePairs = list()
        columnValuePairs.append((dbc.PREFERENCE_TABLE_TYPES_COLUMN, ";".join(pref.types)))
        columnValuePairs.append((dbc.PREFERENCE_TABLE_DATES_COLUMN, ";".join(pref.dates)))
        columnValuePairs.append((dbc.PREFERENCE_TABLE_HOURS_COLUMN, ";".join(pref.hours)))
        columnValuePairs.append((dbc.PREFERENCE_TABLE_TICKET_COUNT_COLUMN, pref.ticketCount))
        columnValuePairs.append((dbc.PREFERENCE_TABLE_MIN_PRICE_COLUMN, pref.minPrice))
        columnValuePairs.append((dbc.PREFERENCE_TABLE_MAX_PRICE_COLUMN, pref.maxPrice))
        query = QueryCreator.insertInto(dbc.PREFERENCE_TABLE, columnValuePairs)
        self.executor.execute(query)

    def getPreference(self) :
        query = QueryCreator.select(dbc.PREFERENCE_TABLE, ['*'], "")
        result = self.executor.execute(query).fetch()
        if result == None :
            return None
        return Preference(result[0].split(";"), result[1].split(";"), result[2].split(";"), int(result[3]), int(result[4]), int(result[5]))
    
    def deletePreference(self) :
        query = QueryCreator.delete(dbc.PREFERENCE_TABLE, "")
        self.executor.execute(query)