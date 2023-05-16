from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
        
        
    def openHalls(self, pageName, driver):
        driver.get(pageName)
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
            
            
    def goToEvent(self, driver, eventName):
        try:
            allEventInHallLinks = driver.find_elements("xpath", "//div[contains(@class, 'a-tabPanel')]")
            for event_link in allEventInHallLinks:
                links = event_link.find_elements("xpath", "//a[@href]")
                for link in links:
                    if eventName in link.get_attribute("href"):
                        link.click()
                        return  
            print("Event not found:", eventName)
        except Exception as e:
            print("Error navigating to the event:", str(e))


booking = Booking()

driver = booking.driverConnect()
print("Driver object returned successfully!")
pageName = "https://www.eventim.bg/bg/"
booking.openHalls(pageName, driver)
wantedHall = "София"
booking.openWantedHall(driver, wantedHall)
# href="/bg/bileti/koncert-gregorianski-pesnopeniya-sofiya-siti-mark-art-centr-595194/event.html" как ще построим този линк от името на събитието?
eventName = "/bg/bileti/cska-balkan-sofiya-basketbolna-zala-594635/event.html"
booking.goToEvent(driver, eventName)

# date and time format: 2023-05-15T19:00:00+03:00