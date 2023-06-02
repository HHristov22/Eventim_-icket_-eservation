from data_types import User
from data_types import EventimEvent
from data_types import Preference
import abc

class DatabaseInterface(metaclass=abc.ABCMeta) :
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return (hasattr(subclass, 'insertUser') and
                callable(subclass.insertUser) and
                hasattr(subclass, 'getUser') and
                callable(subclass.getUser) and
                hasattr(subclass, 'getAllUsers') and
                callable(subclass.getAllUsers) and
                hasattr(subclass, 'deleteUser') and
                callable(subclass.deleteUser) and
                hasattr(subclass, 'updateUser') and
                callable(subclass.updateUser))
    
    @abc.abstractmethod
    def setUser(self, user : User) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def getUser(self) -> User :
        raise NotImplementedError
    
    @abc.abstractmethod
    def deleteUser(self) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def insertEventimEvent(self, eventimEvent : EventimEvent) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def getAllEventimEvent(self) -> list :
        raise NotImplementedError
    
    @abc.abstractmethod
    def deleteAllEventimEvents(self) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def setPreference(self, pref : Preference) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def getPreference(self) :
        raise NotImplementedError
    
    @abc.abstractmethod
    def deletePreference(self) :
        raise NotImplementedError