# Users have email and password for login in https://www.eventim.bg/bg/
class User :
    
    def __init__(self, email : str, password : str) -> None :
        self.email = email
        self.password = password

    def __repr__(self) -> str :
        return self.__str__()
    
    def __str__(self) -> str :
        return "\nUser:\n\teventimEmail: {}\n\teventimPassword: {}".format(
            self.email,
            self.password
        )
    
    def __eq__(self, __value : object) -> bool :
        return self.email == __value.email and self.password == __value.password
    

class EventimEvent :

    def __init__(self, name : str, type : str, location : str, date : str, time : str, price : int, availability : int) -> None :
        self.name = name
        self.type = type
        self.location = location
        self.date = date
        self.time = time
        self.price = price
        self.availability = availability
    
    def __repr__(self) -> str :
        return self.__str__()
    
    def __str__(self) -> str :
        return "\nEvent:\n\tName: {}\n\tType: {}\n\tLocation: {}\n\tDate: {}\n\tTime: {}\n\tPrice: {}\n\tAvailability: {}".format(
            self.name,
            self.type,
            self.location,
            self.date,
            self.time,
            self.price,
            self.availability
        )
    
    def __eq__(self, __value : object) -> bool :
        result = self.name == __value.name
        result = result and self.type == __value.type
        result = result and self.location == __value.location
        result = result and self.date == __value.date
        result = result and self.time == __value.time
        result = result and self.price == __value.price
        result = result and self.availability == __value.availability
        return result


class Preference :

    def __init__(self, types : list, dates : list, hours : list, ticketCount : int, minPrice : int, maxPrice : int) -> None :
        self.types = types
        self.dates = dates
        self.hours = hours
        self.ticketCount = ticketCount
        self.minPrice = minPrice
        self.maxPrice = maxPrice
    
    def __repr__(self) -> str :
        return self.__str__()
    
    def __str__(self) -> str :
        return "\nPreference:\n\tTypes: {}\n\tDates: {}\n\tHours: {}\n\tNumber of tickets: {}\n\tPrice range: {} - {}".format(
            ", ".join(self.types),
            ", ".join(self.dates),
            ", ".join(self.hours),
            self.ticketCount,
            self.minPrice,
            self.maxPrice
        )
    
    def __eq__(self, __value : object) -> bool :
        result = True
        for element in self.types :
            result = result and element in __value.types
        for element in __value.types :
            result = result and element in self.types
        
        for element in self.dates :
            result = result and element in __value.dates
        for element in __value.dates :
            result = result and element in self.dates

        for element in self.hours :
            result = result and element in __value.hours
        for element in __value.hours :
            result = result and element in self.hours

        result = result and self.ticketCount == __value.ticketCount
        result = result and self.minPrice == __value.minPrice
        result = result and self.maxPrice == __value.maxPrice

        return result