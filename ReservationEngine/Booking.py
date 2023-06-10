from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

'''
The Booking class opens the link to the chosen event.
'''

class Booking:
    
    def __init__(self) :
        self.__createWebDriver()
    
    def openLink(self, link) :
        self.driver.get(link)
        self.driver.maximize_window()

    def __createWebDriver(self) :
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(3)