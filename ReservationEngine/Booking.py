from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from BookingConstants import PAGE_NAME, ACCEPT, HALLS

class Booking:
    
    def __init__(self):
        self.attribute = 0
                

    def driverConnect(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.implicitly_wait(10)  
            return driver
        except Exception as e:
            print("Failed to connect to the driver:", str(e))
            return None
        
        
    def acceptCookies(self, driver):
        try:
            linksForCookies = driver.find_elements("xpath", "//div[contains(@class, 'cookie-policy-action')]")
            for link in linksForCookies:
                if ACCEPT in link.get_attribute("innerHTML"):
                    link.click()
                    break
        except Exception as e:
            print("Error handling cookies:", str(e))
        
        
    def openHalls(self, driver):
        driver.get(PAGE_NAME)
        driver.maximize_window()
        self.acceptCookies(driver)

        try:
            link = driver.find_element("xpath", "//a[contains(text(), '{}')]".format(HALLS))
            link.click()
        except NoSuchElementException:
            print("Halls link not found")
            
            
    def openCityHall(self, driver, cityHall):
        try:
            link = driver.find_element("xpath", "//a[contains(text(), '{}')]".format(cityHall))
            link.click()
        except NoSuchElementException:
            print("City hall not found:", cityHall)
        except Exception as e:
            print("Error opening the wanted hall:", str(e))   
            
            
    def goToEvent(self, driver, eventName, eventLocation):
        try:
            event_link = driver.find_element("xpath", "//div[contains(@class, 'a-tabPanel')]//a[contains(@href, '{}')\
                                                and contains(@href, '{}')]".format(eventName, eventLocation))
            event_link.click()
        except NoSuchElementException:
            print("Event not found:", eventName, "in", eventLocation)
        except Exception as e:
            print("Error navigating to the event:", str(e))

    
    def findPrefferedDateAndTime(self, driver, formatedDateAndTime):
        try:
            meta_tag = driver.find_element("xpath", "//div[@class='o-eventList']//meta[contains(@content, '{}')]".format(formatedDateAndTime))
            content = meta_tag.get_attribute("content")
            element = driver.find_element("xpath", "//a[@class='m-eventListItem']")
            href = element.get_attribute('href')
            element.click()
            return
        except NoSuchElementException:
            pass
    
    def booking(self, city,  eventName, eventLocation, prefferedDateAndTime):
        driver = self.driverConnect()
        print("Driver object returned successfully!")
        self.openHalls(driver)
        self.openCityHall(driver, city)
        self.goToEvent(driver, eventName, eventLocation)
        self.findPrefferedDateAndTime(driver, prefferedDateAndTime )
        driver.close()
        print("Driver closed successfully!")
        

def main():
    book = Booking()
    eventName = "cska"
    eventLocation = "balkan-sofiya-basketbolna-zala"
    prefferedDateAndTime = "2023-05-19T19:00:00+03:00"
    book.booking("София" , eventName, eventLocation, prefferedDateAndTime)
    
if __name__ == "__main__":
    main()