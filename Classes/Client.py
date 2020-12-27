
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
import time
from selenium.webdriver.chrome.options import Options

class Client:

    def __init__(self, username, password, method):
        self.username=username
        self.password=password
        self.method=method

    def login(self):
        print("Starting up")
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # Open the Website
        browser.maximize_window()
        browser.get('http://rivalregions.com/')
        print("Establishing connection")
        if self.method=='f':
            print("Choosen login method: facebook")
            element = browser.find_element_by_class_name('sa_link')
            browser.get(element.get_attribute('href'))
            time.sleep(5)
            browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click();
            time.sleep(5)
            browser.find_element_by_name("email").send_keys(self.username)
            browser.find_element_by_name("pass").send_keys(self.password)
            # # Click Log In
            browser.find_element_by_id('loginbutton').click();
            print("Logged in, waiting for server response")
            time.sleep(10)
            money= browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/span[1]/span").text
            money.replace(".", "")
            print("You have "+money+" $")
        else:
            print("nope")