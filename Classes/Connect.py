from selenium import webdriver

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
        self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
        self.browser.find_element_by_name("email").send_keys(login)
        self.browser.find_element_by_name("pass").send_keys(password)
        # # Click Log In
        self.browser.find_element_by_id('loginbutton').click();
        print("Logged in, waiting for server response.")
        while True:
            if(self.browser.current_url!="http://rivalregions.com/#overview"):
                while(True):
                    try:
                        url = self.browser.execute_script("return id")
                        if(not(url is None)):
                            break
                    except:
                        time.sleep(1)
                print("Response received")
                break
            else:
                time.sleep(0.1)


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
        results=np.array([])
        test = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[18]/div[2]/span[1]").text
        if (test.count("km") == 1):
            y = 19
        else:
            y = 18
        for x in range(5):
            z=y+x
            resource = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div["+str(z)+"]/div[2]/span[1]").text
            results=np.append(results, [resource])
        time.sleep(1)
        return results

    def checkCurrentUserID(self):
        url = self.browser.execute_script("return id")
        time.sleep(1)
        return url

    def checkUserStats(self, id):
        self.browser.get('http://rivalregions.com/#slide/profile/'+str(id))
        self.browser.refresh();        #         By.cssSelector("[action: \"listed/perk/1\"]")
        time.sleep(1)
        strength = self.browser.find_element_by_css_selector("[action=\"listed/perk/1\"]").text
        education = self.browser.find_element_by_css_selector("[action=\"listed/perk/2\"]").text
        endurance = self.browser.find_element_by_css_selector("[action=\"listed/perk/3\"]").text
        results = np.array([strength, education, endurance])
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
            tests=self.browser.find_element_by_id("tiptip_content")
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

    def checkPartyNumbers(self, id):
        self.browser.get('http://rivalregions.com/#slide/party/' + str(id))
        self.browser.refresh();
        #/html/body/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]
        number = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]").text
        boolean=True
        while boolean:
            try:
                result=(int(''.join(c for c in number if c.isdigit())))
            except:
                number = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]").text
                continue
            boolean=False
        return result

    def scrolllock(self):
        action = webdriver.ActionChains(self.browser)
        element = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div[2]/div[2]/div")
        action.move_to_element(element).click_and_hold()
        action.move_to_element(element).click_and_hold()
        action.move_by_offset(0, 50).perform()
        action.release().perform()


    def retrievePartyMembersID(self, id):
        number=self.checkPartyNumbers(id)
        self.browser.get('http://rivalregions.com/#listed/party/' + str(id))
        self.browser.refresh()
        results=np.array([])
        time.sleep(1)
        fetched=0
        time.sleep(5)
        table = self.browser.find_element_by_xpath("//table[@id='table_list']")
        fetched=len(table.find_elements_by_xpath(".//tr"))
        while(fetched<number):
            self.browser.execute_script("document.getElementById('list_last').click();")
            time.sleep(1)
            table = self.browser.find_element_by_xpath("//table[@class='list_table tc']")
            fetched = len(table.find_elements_by_xpath(".//tr"))
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            results = np.append(results, [row.get_attribute("user")])

        return (results)





