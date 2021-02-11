import numpy as np

class Country:

    def __init__(self, connector, ID):
        self.id=ID
        self.browser=connector.getController()
        self.browser.get('https://rivalregions.com/#state/details/'+str(self.id))
        self.browser.refresh(); #2307
        self.name=self.browser.find_element_by_css_selector('[href=\"http://rivalregions.com/info/regions/'+str(self.id)+'\"]').text
        self.browser.get('http://rivalregions.com/info/regions/'+str(self.id))
        self.browser.refresh();

        self.regions=int(self.browser.execute_script("return document.querySelector(\"body > table\").rows.length;"))-1

    def getName(self):
        return self.name

    def getRegionsAmount(self):
        return self.regions