from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

def sum(x, y):
    return str(x + y)
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    z = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
