from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #print(text)
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    x_input = browser.find_element(by=By.ID, value="input_value")
    x = x_input.text

    fields_input = browser.find_element(by=By.ID, value="answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", fields_input)
    fields_input.send_keys(calc(int(x)))

    button = browser.find_element(By.ID, "solve")
    button.click()
    time.sleep(10)
    #message = browser.find_element_by_id("verify_message")

    #assert "successful" in message.text
