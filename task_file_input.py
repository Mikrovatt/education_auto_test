from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
# Инициализируем драйвер браузера
with webdriver.Chrome() as browser:
    browser.get(link) # перходим к тестирумеому приложению
    first_name = browser.find_element(by=By.NAME, value="firstname") # Получаю елемент для ввода данных
    first_name.send_keys("firstname") # Ввожу данные
    last_name = browser.find_element(by=By.NAME, value="lastname")
    last_name.send_keys("lastname")
    email = browser.find_element(by=By.NAME, value="email")
    email.send_keys("email@email.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # Получаю текущую дерриктоию программы
    file_path = os.path.join(current_dir, 'file.txt') # Создаю путь к загружаемому файлу
    file = browser.find_element(by=By.ID, value="file") # Ищу поле дляподгрузки файла
    file.send_keys(file_path) # Загружаю файл

    button = browser.find_element(by=By.TAG_NAME, value="button") # Ищу кнопку ввода
    button.click() # нажимаю кнопку
    time.sleep(10)
