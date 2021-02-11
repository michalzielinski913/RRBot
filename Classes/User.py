import numpy as np
import time
class User:

    def __init__(self,connector, ID):
        self.browser=connector.getController()
        self.id=ID
        self.browser.get('http://rivalregions.com/#slide/profile/'+str(self.id))
        self.browser.refresh();
        time.sleep(1)
        usernames = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[4]/h1").text
        pos = 0
        for x in range(len(usernames)):
            if (usernames[x] == ":"):
                pos = x + 2
                break
        self.username=usernames[pos:]
        self.strength = self.browser.find_element_by_css_selector("[action=\"listed/perk/1\"]").text
        self.education = self.browser.find_element_by_css_selector("[action=\"listed/perk/2\"]").text
        self.endurance = self.browser.find_element_by_css_selector("[action=\"listed/perk/3\"]").text
        party = self.browser.find_element_by_css_selector("div[action^='slide/party/']")
        party_tag = party.get_attribute("action")
        result = (int(''.join(c for c in party_tag if c.isdigit())))
        self.partyID=result
        residencyTag = self.browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[5]/div[3]/table/tbody/tr[8]/td[2]/div")
        self.residency = (int(''.join(c for c in residencyTag.get_attribute("action") if c.isdigit())))

    def getStrength(self):
        return self.strength

    def getEducation(self):
        return self.education

    def getEndurance(self):
        return self.endurance

    def getParty(self):
        return self.partyID

    def getUserID(self):
        return self.id

    def getResidency(self):
        return self.residency

