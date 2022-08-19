import time
import secret
import os
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("window-size=1920,1080");
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument('--disable-dev-shm-usage')    
options.add_argument("--disable-gpu")
options.add_argument('--disable-software-rasterizer')
options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
options.add_argument("--disable-notifications")

options.add_experimental_option("prefs", {
    "download.default_directory": "~\Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
    }
)


#Defining functions to navigate browser

class Browser:
    browser, service = None, None
    
    def __init__(self,driver:str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service,options=options)

    def open_page(self,url:str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()
    
    def add_input(self,by:By,value:str, text:str):
        field = self.browser.find_element(by=by,value=value)
        field.send_keys(text)
        time.sleep(1)
        
    def click_button(self,by: By,value:str):
        button = self.browser.find_element(by=by,value=value)
        button.click()
        time.sleep(1)

#login function
    def login_digihero(self,username: str, password: str):
        self.add_input(by=By.ID,value='username',text=username)
        self.add_input(by=By.ID,value='password',text=password)
        self.click_button(by=By.XPATH,value="//button[contains(text(),'Inloggen')]")

#add date parameters and download 
    def add_date(self,startDate:str,endDate:str):
        self.add_input(by=By.NAME,value='startDate',text=startDate)
        self.add_input(by=By.NAME,value='endDate',text=endDate)
        self.click_button(by=By.XPATH,value="//button[contains(text(),'Exporteer')]")


if __name__== '__main__':
    browser= Browser('/home/mihnea/Documents/DigiHeroDownload/chromedriver')
    browser.open_page('https://www.digihero.nl/control-panel/login')
    time.sleep(3)

    browser.login_digihero(secret.email,secret.password) 
    time.sleep(5)

    browser.open_page('https://www.digihero.nl/control-panel/centrale/extensies/extensie/?extensie=0596*0999')
    time.sleep(5)

    browser.add_date(secret.date_from,secret.date_to)
    print ("Download button clicked and date added")

    time.sleep(5)
