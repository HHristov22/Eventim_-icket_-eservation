from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from typing import Final

PAGE_NAME: Final[str] = "https://www.eventim.bg/bg/"

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
        
        
    def openHalls(self, driver):
        driver.get(PAGE_NAME)
        driver.maximize_window()

        try:
            linksForCookies = driver.find_elements("xpath", "//div[contains(@class, 'cookie-policy-action')]")
            for link in linksForCookies:
                if "Приемам" in link.get_attribute("innerHTML"):
                    link.click()
                    break
        except Exception as e:
            print("Error handling cookies:", str(e))

        try:
            mainLinks = driver.find_elements("xpath", "//a[@href]")
            for link in mainLinks:
                if "Зали" in link.get_attribute("innerHTML"):
                    link.click()
                    break
        except Exception as e:
            print("Error opening halls:", str(e))
            
            
    def openWantedHall(self, driver, wantedHall):
        try:
            hallsLinks = driver.find_elements("xpath", "//a[@href]")
            for link in hallsLinks:
                if wantedHall in link.get_attribute("innerHTML"):
                    link.click()
                    break
        except Exception as e:
            print("Error opening the wanted hall:", str(e))    
            
            
    def goToEvent(self, driver, eventName, eventLocation):
        try:
            allEventInHallLinks = driver.find_elements("xpath", "//div[contains(@class, 'a-tabPanel')]")
            for event_link in allEventInHallLinks:
                links = event_link.find_elements("xpath", "//a[@href]")
                for link in links:
                    if eventName in link.get_attribute("href") and eventLocation in link.get_attribute("href"):
                        link.click()
                        return  
            print("Event not found:", eventName, "in", eventLocation)
        except Exception as e:
            print("Error navigating to the event:", str(e))

    def booking(self, eventName, eventLocation):
        driver = self.driverConnect()
        print("Driver object returned successfully!")
        self.openHalls(driver)
        wantedHall = "София"
        self.openWantedHall(driver, wantedHall)
        self.goToEvent(driver, eventName, eventLocation)
        driver.close()

def main():
    booking = Booking()

    driver = booking.driverConnect()
    print("Driver object returned successfully!")
    booking.openHalls(driver)
    wantedHall = "София"
    booking.openWantedHall(driver, wantedHall)
    eventName = "cska"
    eventLocation = "balkan-sofiya-basketbolna-zala"
    booking.goToEvent(driver, eventName, eventLocation)

    # date and time format: 2023-05-15T19:00:00+03:00


if __name__ == "__main__":
    main()