from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re
import sys
sys.path.append('..')
from data_types import EventimEvent
# from Database.database_manager import Database
from booking_constants import PAGE_NAME, ACCEPT, EVENTS, LIST_OF_LINKS

class Extractor:
    
    def __init__(self, driver):
        self.driver = driver
        # self.database = database
        
    def __connectWithWebPage(self):
        self.driver.get(PAGE_NAME)
        self.driver.maximize_window()
        self.__acceptCookies()
        
    def __acceptCookies(self):
        try:
            linksForCookies = self.driver.find_elements("xpath", "//div[contains(@class, 'cookie-policy-action')]")
            for link in linksForCookies:
                if ACCEPT in link.get_attribute("innerHTML"):
                    link.click()
                    break
        except Exception as e:
            print("Error handling cookies:", str(e))
            return None

    def __openEventsMenu(self):
        self.__connectWithWebPage()
        try:
            link = self.driver.find_element("xpath", "//a[contains(text(), '{}')]".format(EVENTS))
            link.click()
        except NoSuchElementException:
            print("events link not found")
            return None
        
    def extractAllLinksForConcerts(self) -> list:
        self.__openEventsMenu()
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.m-mainMenu__listItemSubListItem')
        
        links = []
        for li in li_elements:
            a = li.find_element(By.CSS_SELECTOR, 'a')
            link = a.get_attribute('href')
            if(link not in LIST_OF_LINKS):
                if('concerts' in link or 'muzika/narodna_muzika' in link):
                    links.append(link)
        
        return links
    
    def extractAllLinksForCulture(self) -> list:
        self.__openEventsMenu()
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.m-mainMenu__listItemSubListItem')
        
        links = []
        for li in li_elements:
            a = li.find_element(By.CSS_SELECTOR, 'a')
            link = a.get_attribute('href')
            if(link not in LIST_OF_LINKS):
                if('kultura' in link in link):
                    links.append(link)
        
        return links    
    
    def extractAllLinksForSport(self) -> list:
        self.__openEventsMenu()
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.m-mainMenu__listItemSubListItem')
        
        links = []
        for li in li_elements:
            a = li.find_element(By.CSS_SELECTOR, 'a')
            link = a.get_attribute('href')
            if(link not in LIST_OF_LINKS):
                if('sport' in link in link):
                    links.append(link)
        
        return links   
    
    def extractAllLinksForFamily(self) -> list:
        self.__openEventsMenu()
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.m-mainMenu__listItemSubListItem')
        
        links = []
        for li in li_elements:
            a = li.find_element(By.CSS_SELECTOR, 'a')
            link = a.get_attribute('href')
            if(link not in LIST_OF_LINKS):
                if('semeistvo' in link or 'zabavlenija_razni' in link or 'panair' in link or 'party' in link):
                    links.append(link)
        
        return links
    
    def extractAllLinksForOther(self) -> list:
        self.__openEventsMenu()
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'li.m-mainMenu__listItemSubListItem')
        
        links = []
        for li in li_elements:
            a = li.find_element(By.CSS_SELECTOR, 'a')
            link = a.get_attribute('href')
            if(link not in LIST_OF_LINKS):
                if('drugi' in link and not 'zabavlenija_razni' in link and not 'drugi_sportni_subitiya' in link):
                    links.append(link)
        
        return links
    
    def __maxPrice(self, event_link):
        self.driver.get(event_link)
        time.sleep(3)  # Wait for 3 seconds
        button = self.driver.find_element(By.XPATH, '//*[@id="event_page"]/div[2]/article/div/div[2]/div/div/a/div[3]/button')
        button.click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".o-singleTicketTypeSelection__options .m-priceLevel__title.-alternative")
        
        stringPrices = [element.text for element in elements]
        prices = [re.findall(r'\d+', s)[0] for s in stringPrices]

        return max(prices)            
        
    def __saveEventsOfType(self, links, event_type): # links - contanis all links for different type in one category
        events_links = [] 
        events_names = []
        events_locations = []
        events_datesAndTimes = []
        events_maxPrices = []
        
        for concertLink in links:
            self.driver.get(concertLink)
            try:
                element = self.driver.find_element(By.XPATH, "//span[contains(@class, 'a-pagination_loadMoreLabel') and contains(text(), 'Покажи още')]")
                element.click()
            except NoSuchElementException:
                print("All elements in page are loaded!")
            
            # Extract names
            h3_elements = self.driver.find_elements(By.TAG_NAME, "h3")
            events_names.extend(element.get_attribute("innerHTML") for element in h3_elements)

            # Extract locations
            elements = self.driver.find_elements(By.CLASS_NAME, "m-eventListItem__venue")
            events_locations.extend(element.text for element in elements)

            # Extract dates and times
            elements = self.driver.find_elements(By.CSS_SELECTOR, "*[itemprop='startDate']")
            events_datesAndTimes.extend(element.get_attribute("content") for element in elements)
            
            # Extract links
            elements = self.driver.find_elements(By.TAG_NAME, 'a')
            events_links.extend(tag.get_attribute("href") for tag in elements 
                                if tag.get_attribute("href") and 'event' in tag.get_attribute("href") and 'bileti' in tag.get_attribute("href"))
        
        # extract max prices
        for i in range(0, len(events_links)):
            events_maxPrices.append(0)        
        
        for name, location, dateAndTime, maxPrice, link in zip(events_names, events_locations, events_datesAndTimes, events_maxPrices, events_links):
            newEvenet = EventimEvent(name, event_type, location, dateAndTime, maxPrice, link)
            print(newEvenet)
            # Database.insertEventimEvent(newEvenet)

    def saveEvenetsOfPrefferedTypes(self):
        # prefferedType = self.database.getPreference()
        prefferedType = ['', 'concert']
        # prefferedType[1] = 'concert'
        
        if prefferedType[1]  == 'concert':
            concertLinks = self.extractAllLinksForConcerts()
            self.__saveEventsOfType(concertLinks, 'concert')
            
        elif prefferedType[1]  == 'family':
            familyLinks = self.extractAllLinksForFamily()
            self.__saveEventsOfType(familyLinks, 'family')
            
        elif prefferedType[1]  == 'culture':
            cultureLinks = self.extractAllLinksForCulture()
            self.__saveEventsOfType(cultureLinks, 'culture')
            
        elif prefferedType[1]  == 'sport':
            sportLinks = self.extractAllLinksForSport()
            self.__saveEventsOfType(sportLinks, 'sport')

        elif prefferedType[1]  == 'other':
            otherLinks = self.extractAllLinksForOther()
            self.__saveEventsOfType(otherLinks, 'other')





def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  

    extractor = Extractor (driver)
    extractor.saveEvenetsOfPrefferedTypes()

    driver.close()

if __name__ == "__main__":
    main()  