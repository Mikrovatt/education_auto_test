from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    fields_input = browser.find_elements_by_css_selector('input[type="text"]')
    for field in fields_input:
        field.send_keys("Ivan")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(20)
