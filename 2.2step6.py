from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()