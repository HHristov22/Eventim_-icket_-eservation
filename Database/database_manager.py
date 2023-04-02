import sqlite3 as sql
from user_data import UserData

class Database :

    def __init__(self) -> None:
        pass

    def initialize(self, databaseFilePath : str) :
        self._connectToDatabase(databaseFilePath)
        self._createUsersTableIfNotPresent()

    def _connectToDatabase(self, databaseFilePath : str) :
        self.connection = sql.connect(databaseFilePath)
        self.cursor = self.connection.cursor()

    def _createUsersTableIfNotPresent(self) :
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            eventimEmail TEXT NOT NULL UNIQUE,
            eventimPassword TEXT
        );
        """)
    
    def getAllTableNames(self) :
        tableNames = self.cursor.execute("""
            SELECT name FROM sqlite_schema
            WHERE type='table';
        """).fetchone()
        if(tableNames is None) :
            tableNames = list()
        return tableNames
    
    def removeTable(self, tableName : str) :
        self.cursor.execute("""
            DROP TABLE IF EXISTS '{}';
        """.format(tableName))

    def insertUser(self, user : UserData) :
        self.cursor.execute("""
        INSERT INTO users ('username', 'password', 'eventimEmail', 'eventimPassword')
        VALUES ('{}', '{}', '{}', '{}');
        """.format(user.username, user.password, user.eventimEmail, user.eventimPassword))

    def getAllUsers(self) -> list :
        users = list()
        usersFromDatabase = self.cursor.execute("""
        SELECT *,ROWID FROM users;
        """).fetchall()

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
        self.cursor.execute("""
        DELETE FROM users
        WHERE username='{}';
        """.format(username))

    def updateUser(self, username : str, updatedData : UserData) :
        self.cursor.execute("""
        UPDATE users
        SET username='{}', password='{}', eventimEmail='{}', eventimPassword='{}'
        WHERE username='{}';
        """.format(
            updatedData.username,
            updatedData.password,
            updatedData.eventimEmail,
            updatedData.eventimPassword,
            username
        ))
    
    def commitAndCloseConnection(self) :
        self.connection.commit()
        self.connection.close()