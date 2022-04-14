from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    num1 = int(browser.find_element(by=By.ID, value="num1").text)
    num2 = int(browser.find_element(by=By.ID, value="num2").text)

    select = Select(browser.find_element(by=By.TAG_NAME, value="select"))
    select.select_by_value(str(num1 + num2))

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(5)
