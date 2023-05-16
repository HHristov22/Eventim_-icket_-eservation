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
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    
    def openHalls(self, pageName, driver):  
        driver.get(pageName)
        driver.maximize_window()

        linksForCookies = driver.find_elements("xpath", "//div[contains(@class, 'cookie-policy-action')]")

        for link in linksForCookies:
            if "Приемам" in link.get_attribute("innerHTML"):
                link.click()
                break
            
        mainLinks = driver.find_elements("xpath", "//a[@href]")
        for link in mainLinks:
            if "Зали" in link.get_attribute("innerHTML"):
                link.click()
                break
            
    def openWantedHall(self, driver, wantedHall):    
        hallsLinks = driver.find_elements("xpath", "//a[@href]")
        for link in hallsLinks:
            if wantedHall in link.get_attribute("innerHTML"):
                link.click()
                break         
            
    def goToEvent(self, driver, eventName):
        allEventInHallLinks = driver.find_elements("xpath", "//div[contains(@class, 'a-tabPanel')]")
        for event_link in allEventInHallLinks:
            links = event_link.find_elements("xpath", "//a[@href]")
            for link in links:
                if eventName in link.get_attribute("href"):
                    link.click()
                    break
                # else  
                
                
booking = Booking()

driver = booking.driverConnect()
pageName = "https://www.eventim.bg/bg/"
booking.openHalls(pageName, driver)
wantedHall = "София"
booking.openWantedHall(driver, wantedHall)
# href="/bg/bileti/koncert-gregorianski-pesnopeniya-sofiya-siti-mark-art-centr-595194/event.html" как ще построим този линк от името на събитието?
eventName = "/bg/bileti/cska-balkan-sofiya-basketbolna-zala-594635/event.html"
booking.goToEvent(driver, eventName)

# date and time format: 2023-05-15T19:00:00+03:00

    