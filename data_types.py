'''
EventimEvent: 
These are used for informing the user about the event: 
name - Name of the event the way it is shown in the site
    examples(In Hell with Jesus - Мюзикъл/Нощните Рицари - по драматургични текстове на Яна Борисова)
type - Type/genre of the event
    examples(Джаз/Комедия/Футбол)
location - Location of the event (the whole location not just the city)
    examples (Държавен куклен театър Пловдив, Пловдив/Нов театър НДК, София)
dateAndTime - Date and time of the event similar to the way they are displayed in the site
    examples (Четвъртък, 15.06.2023 г. в 19:00 ч./Събота, 10.06.2023 г. в 10:30 ч.)
priceRange - The smallest and biggest price for a ticket fot the event similar to the way they are displayed in the site
    examples - (18,00 лв. - 25,00 лв./55,00 лв. - 75,00 лв.)

This is for accessing the event from the reservation logic
link - Link to the page of the event
    examples(https://www.eventim.bg/bg/bileti/pinto-picasso-with-simon-danila-in-bulgaria-sofiya-sofia-live-club-1345480/performance.html)
    examples(https://www.eventim.bg/bg/bileti/malkata-rusalka-song-of-the-mermaid-plovdiv-ancient-theatre-1342298/performance.html)
'''

class EventimEvent :

    def __init__(self, name = "", type = "", location = "", dateAndTime = "", priceRange = "", link = "") -> None :
        self.name = name
        self.type = type
        self.location = location
        self.dateAndTime = dateAndTime
        self.priceRange = priceRange
        self.link = link
    
    def __repr__(self) -> str :
        return self.__str__()
    
    def __str__(self) -> str :
        return "\nEvent:\n\tName: {}\n\tType: {}\n\tLocation: {}\n\tDate and time: {}\n\tPrice range: {}\n\tLink: {}".format(
            self.name,
            self.type,
            self.location,
            self.dateAndTime,
            self.priceRange,
            self.link
        )
    
    def __eq__(self, __value : object) -> bool :
        result = self.name == __value.name
        result = result and self.type == __value.type
        result = result and self.location == __value.location
        result = result and self.dateAndTime == __value.dateAndTime
        result = result and self.priceRange == __value.priceRange
        result = result and self.link == __value.link
        return result

    def __getitem__(self, index) :
        match index :
            case 0 : return self.name
            case 1 : return self.type
            case 2 : return self.location
            case 3 : return self.dateAndTime
            case 4 : return self.priceRange
            case 5 : return self.link
        return self.name

    def __setitem__(self, index, value) :
        match index :
            case 0 : self.name = value
            case 1 : self.type = value
            case 2 : self.location = value
            case 3 : self.dateAndTime = value
            case 4 : self.priceRange = value
            case 5 : self.link = value

'''
Preference: 
types - List of types/genres of events
    example(["Комедия", "Метъл", "Театър"]) // These should be taken from the site's "Събития" menu
locations - List of cities
    example(["Sofia", "София", "Пловдив"]) // Best add both Latin alphabet and Cyrillic alphabet variations for the names of the cities
dates - List of dates
    example(["15.06.2023", "21.05.2022", "03.12.2023"])
dayParts - List of parts of the day - each part can be one of [DAY_PART_MORNING, DAY_PART_MID_DAY, DAY_PART_AFTERNOON, DAY_PART_EVENING]
    example([MORNING, MID_DAY]) - this is from 06.00 to 16.00
    example([MID_DAY, EVENING]) - this is from 06.00 to 12.00 and from 18.00 to 24.00 
maxPrice - The biggest price that the user is willing to pay
'''

DAY_PART_MORNING = "morning" # 06.00 - 12.00
DAY_PART_MID_DAY = "midday" # 11.00 - 16.00
DAY_PART_AFTERNOON = "afternoon" # 15.00 - 19.00
DAY_PART_EVENING = "evening" # 18.00 - 24.00

class Preference :

    def __init__(self, types : list, locations : list, dates : list, dayParts : list, maxPrice : int) -> None :
        self.types = types
        self.locations = locations
        self.dates = dates
        self.dayParts = dayParts
        self.maxPrice = maxPrice
    
    def __repr__(self) -> str :
        return self.__str__()
    
    def __str__(self) -> str :
        return "\nPreference:\n\tTypes: {}\n\tLocations: {}\n\tDates: {}\n\tParts of the day: {}\n\tMaximal price: {}".format(
            "; ".join(self.types),
            "; ".join(self.locations),
            "; ".join(self.dates),
            "; ".join(self.dayParts),
            self.maxPrice
        )
    
    def __eq__(self, __value : object) -> bool :
        result = True
        for element in self.types :
            result = result and element in __value.types
        for element in __value.types :
            result = result and element in self.types
        
        for element in self.locations :
            result = result and element in __value.locations
        for element in __value.locations :
            result = result and element in self.locations


        for element in self.dates :
            result = result and element in __value.dates
        for element in __value.dates :
            result = result and element in self.dates

        for element in self.dayParts :
            result = result and (element in __value.dayParts)
        for element in __value.dayParts :
            result = result and element in self.dayParts

        result = result and self.maxPrice == __value.maxPrice

        return result
    
    def __getitem__(self, index) :
        match index :
            case 0 : return self.types
            case 1 : return self.locations
            case 2 : return self.dates
            case 3 : return self.dayParts
            case 4 : return self.maxPrice
        return self.name

    def __setitem__(self, index, value) :
        match index :
            case 0 : self.types = value
            case 1 : self.locations = value
            case 2 : self.dates = value
            case 3 : self.dayParts = value
            case 4 : self.maxPrice = value