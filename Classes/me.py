import numpy as np
import time
from Classes.User import User
from selenium.webdriver.common.action_chains import ActionChains
import warnings
import datetime
class Me(User):
    def __init__(self, connector):
        self.id = connector.getController().execute_script("return id")
        User.__init__(self, connector, self.id)
        self.money = self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/span[1]/span").text


    def getMoney(self):
        return self.money

    def getResources(self):
        self.browser.get('https://rivalregions.com/#work')
        self.browser.refresh();
        self.oil=self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[1]").text
        self.ore=self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[2]").text
        self.gold=self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[3]").text
        self.uranium=self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[4]").text
        self.diamond=self.browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[5]").text
        return np.array([self.oil, self.ore, self.gold, self.uranium, self.diamond], np.float)

    def checkAvailableResources(self):
        #Go to work tab
        self.browser.get('http://rivalregions.com/#work')
        self.browser.refresh();
        time.sleep(1)
        results = np.array([], dtype=bool)
        self.xgold = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[3]"
        self.xmineral = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[2]"
        self.xoil = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[1]"
        self.xdiamond = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[5]"
        self.xuranium = "/html/body/div[6]/div[1]/div[4]/div[1]/h1/span[4]"
        self.resources=np.array([self.xgold, self.xoil, self.xmineral, self.xuranium, self.xdiamond])
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

    def moveToRegion(self, ID):

        try:
            self.browser.get('https://rivalregions.com/#map/details/' + str(ID))
            self.browser.refresh();
            action = ActionChains(self.browser)
            element = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div[1]")
            if (element.text == "Request residency"):
                warnings.warn("You cant move to the region where you are currently in!")
                return
            action.move_to_element(element).click().perform()
            time.sleep(1)
            requiredMoney = self.browser.find_element_by_id("move_here")
            requiredMoneyI = (int(''.join(c for c in requiredMoney.text if c.isdigit())))
            moneyI = (int(''.join(c for c in self.money if c.isdigit())))
            if (moneyI >= requiredMoneyI):

                action.move_to_element(requiredMoney).click().perform()
                time.sleep(1)
                timeS = (self.browser.execute_script(
                    "return document.querySelector(\"#map_region_det_data > div > div.float_left.map_d_1.no_pointer > div > span\").innerText"))
                L = timeS.split(':')
                if len(L) == 1:
                    sec = L[0]
                elif len(L) == 2:
                    datee = datetime.datetime.strptime(timeS, "%M:%S")
                    sec = datee.minute * 60 + datee.second
                elif len(L) == 3:
                    datee = datetime.datetime.strptime(timeS, "%H:%M:%S")
                    sec = datee.hour * 3600 + datee.minute * 60 + datee.second
                self.browser.execute_script("document.getElementById(\"move_here_ok\").click()")
                print("Moving to given region, It will take " + str(sec) + " seconds")

            else:
                print("Not enough money")
        except:
            print("Couldn't move to defined region")