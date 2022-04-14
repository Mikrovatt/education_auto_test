from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x_input = browser.find_element(by=By.ID, value="treasure")
    x = x_input.get_attribute("valuex")
    print(x)

    fields_input = browser.find_element(by=By.ID, value="answer")
    fields_input.send_keys(calc(int(x)))

    ch_box = browser.find_element(by=By.ID, value="robotCheckbox")
    ch_box.click()

    ch_box = browser.find_element(by=By.ID, value="robotsRule")
    ch_box.click()

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(5)
