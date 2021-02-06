import numpy as np
import time
from Classes.User import User

class Me(User):
    def __init__(self, connector):
        self.id = connector.getController().execute_script("return id")
        User.__init__(self, connector, self.id)
        self.money = self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[4]/span[1]/span").text


    def getMoney(self):
        return self.money

