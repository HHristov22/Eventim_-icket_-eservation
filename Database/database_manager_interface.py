from data_types import EventimEvent
from data_types import Preference
import abc

class DatabaseInterface(metaclass=abc.ABCMeta) :
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return (hasattr(subclass, 'insertEventimEvent') and
                callable(subclass.insertEventimEvent) and
                hasattr(subclass, 'getAllEventimEvent') and
                callable(subclass.getAllEventimEvent) and
                hasattr(subclass, 'deleteAllEventimEvents') and
                callable(subclass.deleteAllEventimEvents) and
                hasattr(subclass, 'setPreference') and
                callable(subclass.setPreference) and
                hasattr(subclass, 'getPreference') and
                callable(subclass.getPreference) and
                hasattr(subclass, 'deletePreference') and
                callable(subclass.deletePreference))
    
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