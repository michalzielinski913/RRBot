import numpy as np
from Classes.functions import scrolllock
import time

class Party:
    def __init__(self,connector, ID):
        self.id=ID
        self.browser=connector.getController()
        partyURL = 'https://rivalregions.com/#slide/party/' + str(self.id)
        self.browser.get(partyURL)
        self.browser.refresh();
        self.party = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/h1/a").text
        number = self.browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]").text
        boolean = True
        while boolean:
            try:
                result = (int(''.join(c for c in number if c.isdigit())))
            except:
                number = self.browser.find_element_by_xpath(
                    "/html/body/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]").text
                continue
            boolean = False
        self.number=result

    def getPartyMembersID(self):

        self.browser.get('http://rivalregions.com/#listed/party/' + str(self.id))
        self.browser.refresh()
        results=np.array([])
        time.sleep(1)
        fetched=0
        time.sleep(5)
        table = self.browser.find_element_by_xpath("//table[@id='table_list']")
        fetched=len(table.find_elements_by_xpath(".//tr"))
        while(fetched<self.number):
            self.browser.execute_script("document.getElementById('list_last').click();")
            time.sleep(1)
            table = self.browser.find_element_by_xpath("//table[@class='list_table tc']")
            fetched = len(table.find_elements_by_xpath(".//tr"))
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            results = np.append(results, [row.get_attribute("user")])

        return (results)

    def getPartyName(self):
        return self.party

    def getPartyPopulation(self):
        return self.number