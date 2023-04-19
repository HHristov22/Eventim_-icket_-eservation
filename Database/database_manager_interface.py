from user_data import UserData
import abc

class DatabaseInterface(metaclass=abc.ABCMeta) :
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return (hasattr(subclass, 'insertUser') and
                callable(subclass.insertUser) and
                hasattr(subclass, 'getAllUsers') and
                callable(subclass.getAllUsers) and
                hasattr(subclass, 'deleteUser') and
                callable(subclass.deleteUser) and
                hasattr(subclass, 'updateUser') and
                callable(subclass.updateUser))
    
    @abc.abstractmethod
    def insertUser(self, user : UserData) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def getAllUsers(self) -> list :
        raise NotImplementedError
    
    @abc.abstractmethod
    def deleteUser(self, username : str) :
        raise NotImplementedError

    @abc.abstractmethod
    def updateUser(self, username : str, updatedData : UserData) :
        raise NotImplementedError