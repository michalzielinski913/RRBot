from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
import datetime
import warnings
class rrbot:

    def __init__(self, headless):
        print("Starting up selenium")
        chrome_options = Options()
        if (headless):
            chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1920,1080')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.browser.implicitly_wait(100)
        self.browser.get('http://rivalregions.com/')

    def __loginFacebook(self, username, password):
        element = self.browser.find_element_by_class_name('sa_link')
        self.browser.get(element.get_attribute('href'))
        self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
        self.browser.find_element_by_name("email").send_keys(username)
        self.browser.find_element_by_name("pass").send_keys(password)
        # # Click Log In
        self.browser.find_element_by_id('loginbutton').click();
        print("Logged in, waiting for server response.")
        while True:
            if (self.browser.current_url != "http://rivalregions.com/#overview"):
                while (True):
                    try:
                        url = self.browser.execute_script("return id")
                        if (not (url is None)):
                            break
                    except:
                        time.sleep(1)
                print("Response received")
                break
            else:
                time.sleep(0.1)

    def login(self, username, password, method):
        print("Starting up")
        print("Establishing connection")
        if method=='f':
            print("Choosen login method: facebook")
            self.__loginFacebook(username, password)
        else:
            print("nope")

    def getController(self):
        return self.browser