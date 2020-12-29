from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# Initiate the browser
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
class Connect:

    def __init__(self, headless):

        self.xgold = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[3]"
        self.xmineral = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[2]"
        self.xoil = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[1]"
        self.xdiamond = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[5]"
        self.xuranium = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[4]"
        self.resources=np.array([self.xgold, self.xoil, self.xmineral, self.xuranium, self.xdiamond])
        print("Starting up selenium")
        chrome_options = Options()
        if(headless):
            chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1920,1080')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.browser.implicitly_wait(100)

        # Open the Website
        self.browser.get('http://rivalregions.com/')

    def connectFacebook(self, login, password):
        element =  self.browser.find_element_by_class_name('sa_link')
        self.browser.get(element.get_attribute('href'))
        self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click();
        self.browser.find_element_by_name("email").send_keys(login)
        self.browser.find_element_by_name("pass").send_keys(password)
        # # Click Log In
        self.browser.find_element_by_id('loginbutton').click();
        print("Logged in, waiting for server response. It will take 10 seconds")
        time.sleep(10)


    def getMoney(self):
        money = self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/span[1]/span").text
        time.sleep(1)
        return money

    def checkRegionresource(self, id):
        self.browser.get('http://rivalregions.com/#map/details/'+str(id))
        self.browser.refresh();
        action=webdriver.ActionChains(self.browser)
        element=self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[2]/div[2]/div")
        action.move_to_element(element).click_and_hold()
        action.move_by_offset(0, 50).perform()
        action.release().perform()
        gold = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[18]/div[2]/span[1]").text
        oil = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[19]/div[2]/span[1]").text
        mineral = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[20]/div[2]/span[1]").text
        uranium = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[21]/div[2]/span[1]").text
        diamond = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[22]/div[2]/span[1]").text
        results = np.array([gold, oil, mineral, uranium, diamond])

        self.browser.get('http://rivalregions.com/#overview')
        self.browser.refresh();
        time.sleep(1)
        return results

    def checkCurrentUserID(self):
        url = self.browser.execute_script("return id")
        time.sleep(1)
        return url

    def checkUserStats(self, id):
        self.browser.get('http://rivalregions.com/#slide/profile/'+str(id))
        self.browser.refresh();
        strength = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[3]/table/tbody/tr[2]/td[2]/span[1]").text
        education = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[3]/table/tbody/tr[2]/td[2]/span[2]").text
        endurance = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[3]/table/tbody/tr[2]/td[2]/span[3]").text
        results = np.array([strength, education, endurance])
        self.browser.find_element_by_xpath("/html/body/div[3]/div/div[1]").click()
        self.browser.get('http://rivalregions.com/#overview')
        self.browser.refresh();
        time.sleep(1)
        return results

    def getMoney(self):
        time.sleep(1)
        return self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/span[1]/span").text

    def CheckAvailableResources(self):
        #Go to work tab
        self.browser.get('http://rivalregions.com/#work')
        self.browser.refresh();
        time.sleep(1)
        results = np.array([], dtype=bool)
        for x in self.resources:
            r = self.browser.find_element_by_xpath(x)
            hover=ActionChains(self.browser).move_to_element(r)
            hover.perform()
            tests=self.browser.find_element_by_xpath("/html/body/div[8]/div[2]")
            data=[pos for pos, char in enumerate(tests.text) if char == '/']
            if(data[0]==1 and (tests.text)[0]=='0'):
                if(tests.text[(data[1]+1):]==tests.text[(data[1]-len(tests.text[(data[1]+1):])):data[1]]):
                    results=np.append(results, [False])
            else:
                results=np.append(results, [True])

            time.sleep(1)
        #[True, True, True, True, True]
        self.browser.get('http://rivalregions.com/#overview')
        self.browser.refresh();
        time.sleep(1)
        return results

    def CheckUserResidency(self, id):
        self.browser.get('http://rivalregions.com/#slide/profile/' + str(id))
        self.browser.refresh();

        residencyTag = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[3]/table/tbody/tr[8]/td[2]/div")
        result=(int(''.join(c for c in residencyTag.get_attribute("action") if c.isdigit())))
        self.browser.get('http://rivalregions.com/#overview')
        self.browser.refresh();
        time.sleep(1)
        return result

