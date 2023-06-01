from user_data import UserData
from database_manager_interface import DatabaseInterface
from query_creator import QueryCreator
from query_executor import QueryExecutor
import database_constants as dbc

class Database(DatabaseInterface) :

    def __init__(self, databaseFilePath : str) -> None:
        self.executor = QueryExecutor(databaseFilePath)
        self._createUsersTableIfNotPresent()

    def _createUsersTableIfNotPresent(self) :
        columnNamesAndDefinitionPairs = list()
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_USERNAME_COLUMN, dbc.USER_TABLE_USERNAME_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_PASSWORD_COLUMN, dbc.USER_TABLE_PASSWORD_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_EVENTIM_EMAIL_COLUMN, dbc.USER_TABLE_EVENTIM_EMAIL_COLUMN_DEFINITION))
        columnNamesAndDefinitionPairs.append((dbc.USER_TABLE_EVENTIM_PASSWORD_COLUMN, dbc.USER_TABLE_EVENTIM_PASSWORD_COLUMN_DEFINITION))
        query = QueryCreator.createTable(dbc.USER_TABLE, columnNamesAndDefinitionPairs)
        self.executor.execute(query)

    def insertUser(self, user : UserData) :
        columnValuePairs = list()
        columnValuePairs.append((dbc.USER_TABLE_USERNAME_COLUMN, user.username))
        columnValuePairs.append((dbc.USER_TABLE_PASSWORD_COLUMN, user.password))
        columnValuePairs.append((dbc.USER_TABLE_EVENTIM_EMAIL_COLUMN, user.eventimEmail))
        columnValuePairs.append((dbc.USER_TABLE_EVENTIM_PASSWORD_COLUMN, user.eventimPassword))
        query = QueryCreator.insertInto(dbc.USER_TABLE,columnValuePairs)
        self.executor.execute(query)

    def getUser(self, username: str) -> UserData:
        sqlCondition = "{}='{}'".format(dbc.USER_TABLE_USERNAME_COLUMN, username)
        query = QueryCreator.select(dbc.USER_TABLE, ['*'], sqlCondition)
        result = self.executor.execute(query).fetch()
        searchedUser = UserData(result[0], result[1], result[2], result[3])
        return searchedUser

    def getAllUsers(self) -> list :
        users = list()
        query = QueryCreator.select(dbc.USER_TABLE, ['*','ROWID'])
        usersFromDatabase = self.executor.execute(query).fetchall()

        for userFromDatabase in usersFromDatabase :
            newUser = UserData(
                userFromDatabase[0],
                userFromDatabase[1],
                userFromDatabase[2],
                userFromDatabase[3]
            )
            users.append(newUser)
        
        return users
    
    def deleteUser(self, username : str) :
        query = QueryCreator.delete(dbc.USER_TABLE, "{}='{}'".format(dbc.USER_TABLE_USERNAME_COLUMN, username))
        self.executor.execute(query)

    def updateUser(self, username : str, updatedData : UserData) :
        columnValuePairs = list()
        columnValuePairs.append((dbc.USER_TABLE_USERNAME_COLUMN, updatedData.username))
        columnValuePairs.append((dbc.USER_TABLE_PASSWORD_COLUMN, updatedData.password))
        columnValuePairs.append((dbc.USER_TABLE_EVENTIM_EMAIL_COLUMN, updatedData.eventimEmail))
        columnValuePairs.append((dbc.USER_TABLE_EVENTIM_PASSWORD_COLUMN, updatedData.eventimPassword))
        condition = "{}='{}'".format(dbc.USER_TABLE_USERNAME_COLUMN, username)
        query = QueryCreator.update(dbc.USER_TABLE, columnValuePairs, condition)
        self.executor.execute(query)