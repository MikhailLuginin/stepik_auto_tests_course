from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestUtest(unittest.TestCase):

    def test_Utest1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[required]')
        input1.send_keys('Olesya')
        input2 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[required]')
        input2.send_keys('Ovchinnikova')
        input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.third[required]')
        input3.send_keys('Good')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_Utest2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[required]')
        input1.send_keys('Olesya')
        input2 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[required]')
        input2.send_keys('Ovchinnikova')
        input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.third[required]')
        input3.send_keys('Good')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        # находим элемент, содержащий текст
        welcome_text_elt1 = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text1 = welcome_text_elt1.text
        self.assertEqual(welcome_text1, "Congratulations! You have successfully registered!")

    if __name__ == "__main__":
        unittest.main()
