from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from booking_constants import PAGE_NAME, ACCEPT, HALLS
from selenium.webdriver.common.by import By
import time
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
    
    
    def __increasingAmount(self, numberOfTickets):
        try:
            stepper = self.driver.find_elements(By.CSS_SELECTOR, '[data-qa="stepper-increase"]')
            for i in range(numberOfTickets):
                stepper[0].click()
                time.sleep(1) 
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
    
    def __reservationTickets(self):
        try:
            element = self.driver.find_element_by_class_name('a-ticketModeOption__indicatorCircle')
            element.click()
            button = self.driver.find_element(By.CSS_SELECTOR, 'button.a-button.-active.-fullWidth.-submit')
            button.click()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def booking(self, link, numberOfTickets):
        self.driver.get('https://www.eventim.bg/bg/bileti/svetlio-the-legends-sofiya-stroeja-open-air-music-bar-1352917/performance.html')
        self.driver.maximize_window()
        self.__acceptCookies()
        element = self.driver.find_element_by_class_name('a-Stepper__amount')

        number = element.text
        self.__increasingAmount(numberOfTickets - int(number))
        self.__reservationTickets()
        
        # print("Driver object returned successfully!")
        # self.__openHallsMenu()
        # self.__chooseCityHall(city)
        # self.__goToEvent(eventName, eventLocation)
        # self.__findPrefferedDateAndTime(prefferedDateAndTime )
        # self.__increasingAmount(numberOfTickets)
        # self.__reservationTickets()
        # time.sleep(10)
        # self.driver.close()
        # print("Driver closed successfully!")
        
        
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
    numberOfTickets = 5
    book.booking('https://www.eventim.bg/bg/bileti/svetlio-the-legends-sofiya-stroeja-open-air-music-bar-1352917/performance.html', numberOfTickets)
    
if __name__ == "__main__":
    main()  