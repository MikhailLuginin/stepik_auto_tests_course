from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
