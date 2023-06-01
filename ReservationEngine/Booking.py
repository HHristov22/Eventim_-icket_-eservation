from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from booking_constants import PAGE_NAME, ACCEPT, HALLS

'''
The Booking class books a ticket through the website.
'''

class Booking:
    
    def __init__(self, driver):
        self.driver = driver
        
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
        
        
    def __openHallsMenu(self):
        self.driver.get(PAGE_NAME)
        self.driver.maximize_window()
        self.__acceptCookies()

        try:
            link = self.driver.find_element("xpath", "//a[contains(text(), '{}')]".format(HALLS))
            link.click()
        except NoSuchElementException:
            print("Halls link not found")
            return None
            
            
    def __chooseCityHall(self, cityHall):
        try:
            link = self.driver.find_element("xpath", "//a[contains(text(), '{}')]".format(cityHall))
            link.click()
        except NoSuchElementException:
            print("City hall not found:", cityHall)
        except Exception as e:
            print("Error opening the wanted hall:", str(e))   
            
            
    def __goToEvent(self, eventName, eventLocation):
        try:
            event_link = self.driver.find_element("xpath", "//div[contains(@class, 'a-tabPanel')]//a[contains(@href, '{}')\
                                                and contains(@href, '{}')]".format(eventName, eventLocation))
            event_link.click()
        except NoSuchElementException:
            print("Event not found:", eventName, "in", eventLocation)
        except Exception as e:
            print("Error navigating to the event:", str(e))

    
    def __findPrefferedDateAndTime(self, formatedDateAndTime):
        try:
            meta_tag = self.driver.find_element("xpath", "//div[@class='o-eventList']//meta[contains(@content, '{}')]".format(formatedDateAndTime))
            content = meta_tag.get_attribute("content")
            element = self.driver.find_element("xpath", "//a[@class='m-eventListItem']")
            href = element.get_attribute('href')
            element.click()
            return
        except NoSuchElementException:
            pass
    
    def booking(self, city,  eventName, eventLocation, prefferedDateAndTime):
        print("Driver object returned successfully!")
        self.__openHallsMenu()
        self.__chooseCityHall(city)
        self.__goToEvent(eventName, eventLocation)
        self.__findPrefferedDateAndTime(prefferedDateAndTime )
        self.driver.close()
        print("Driver closed successfully!")
        

def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  

    book = Booking(driver)
    eventName = "svobodno-padashchi-istorii"
    eventLocation = "theatro-otsam-kanala"
    prefferedDateAndTime = "2023-06-04T20:00:00+03:00"
    book.booking("София" , eventName, eventLocation, prefferedDateAndTime)
    
if __name__ == "__main__":
    main()