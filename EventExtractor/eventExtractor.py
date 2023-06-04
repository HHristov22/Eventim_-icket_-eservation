from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from booking_constants import PAGE_NAME, ACCEPT, EVENTS, LIST_OF_LINKS

class Extractor:
    def __init__(self, driver):
        self.driver = driver

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
        
    def __extractAllLinksForConcerts(self) -> list:
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
    
    def __extractAllLinksForCulture(self) -> list:
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
    
    def __extractAllLinksForSport(self) -> list:
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
    
    def __extractAllLinksForFamily(self) -> list:
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
    
    def __extractAllLinksForOther(self) -> list:
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
    
    def __getNameOfEvent(self):
        name = self.driver.find_element("xpath", "/html/body/div[3]/div[3]/main/div/div[2]/div/div/article/div[2]/div/a[1]/div[2]/h3".format("name"))
        return name.text
        
    def saveConcertEvents(self):
        links = self.__extractAllLinksForConcerts()
        concert_events_links = [] 
        for concertLink in links:
            self.driver.get(concertLink)
            anchor_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            for tag in anchor_tags:
                link = tag.get_attribute("href")
                if link and 'event' in link and 'bileti' in  link:
                    concert_events_links.append(link)   
                        
    
    def saveCultureEvents(self):
        links = self.__extractAllLinksForCulture()
        culture_events_links = [] 
        for concertLink in links:
            self.driver.get(concertLink)
            anchor_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            for tag in anchor_tags:
                link = tag.get_attribute("href")
                if link and 'event' in link and 'bileti' in  link:
                    culture_events_links.append(link)   
                    
        
    def saveSportEvents(self):
        links = self.__extractAllLinksForSport()
        sport_events_links = [] 
        for concertLink in links:
            self.driver.get(concertLink)
            anchor_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            for tag in anchor_tags:
                link = tag.get_attribute("href")
                if link and 'event' in link and 'bileti' in  link:
                    sport_events_links.append(link)   
                    
    
    def saveFamilyEvents(self):
        links = self.__extractAllLinksForFamily()
        family_events_links = [] 
        for concertLink in links:
            self.driver.get(concertLink)
            anchor_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            for tag in anchor_tags:
                link = tag.get_attribute("href")
                if link and 'event' in link and 'bileti' in  link:
                    family_events_links.append(link)   
                    
        
    def saveOtherEvents(self):
        links = self.__extractAllLinksForOther()
        other_events_links = [] 
        for concertLink in links:
            self.driver.get(concertLink)
            anchor_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            for tag in anchor_tags:
                link = tag.get_attribute("href")
                if link and 'event' in link and 'bileti' in  link:
                    other_events_links.append(link)   
                    
    
    
    
def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  

    extractor = Extractor (driver)
    extractor.saveConcertEvents()


    driver.close()

if __name__ == "__main__":
    main()  