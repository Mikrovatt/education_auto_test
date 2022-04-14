from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

data = {
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "city": "Moscow",
    "country": "Russia",
}

with webdriver.Chrome() as browser:
    browser.get(link)
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys(data["first_name"])
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys(data["last_name"])
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys(data["city"])
    country = browser.find_element(By.ID, "country")
    country.send_keys(data["country"])

    submit_button = browser.find_element_by_xpath("//button[text()='Submit']")
    submit_button.click()
    time.sleep(15)
