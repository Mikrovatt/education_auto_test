from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

# Инициализируем браузер
with webdriver.Chrome() as browser:
    browser.get(link) # Загружаем приложение
    # Активация кнопки
    button_main = browser.find_element(by=By.TAG_NAME, value="button")
    button_main.click()
    # time.sleep(1)
    # Таргет окно confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    # time.sleep(1)
    # получаю число со страницы
    num = int(browser.find_element(by=By.ID, value="input_value").text)
    # Ищу поле ввода ответа
    field_input = browser.find_element(by=By.ID, value="answer")
    # Ввожу ответ
    field_input.send_keys(calc(num))

    # Поиск кнопки для ввода формы
    button = browser.find_element(by=By.TAG_NAME, value="button")
    button.click()

    time.sleep(10)
