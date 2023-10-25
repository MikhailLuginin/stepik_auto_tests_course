from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

from selenium.webdriver.remote.webelement import WebElement


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x_elements = x_element.get_attribute("valuex")
    x = x_elements
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option1.click()
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
