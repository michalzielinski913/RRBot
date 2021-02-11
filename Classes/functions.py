from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
import datetime
import warnings
def scrolllock(self, browser):
    action = webdriver.ActionChains(browser)
    element = browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div[2]/div[2]/div")
    action.move_to_element(element).click_and_hold()
    action.move_to_element(element).click_and_hold()
    action.move_by_offset(0, 50).perform()
    action.release().perform()