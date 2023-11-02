import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

class TestStepik():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_autorization_stepik(click):
        click.browser.get(link)
        click.browser.implicitly_wait(5)
        click.browser.find_element(By.ID, "ember33")
        button = click.browser.find_element(By.ID, "ember33")
        button.click()

    @pytest.mark.parametrize('login', ["rabotaluginin@gmail.com"])
    def test_autorization_stepik1(self, login):
        self.browser.find_element(By.ID, "id_login_email")
        input1 = self.browser.find_element(By.ID, "id_login_email")
        input1.send_keys({login})

    @pytest.mark.parametrize('password', ["Mihail221090"])
    def test_autorization_stepik2(self, password):
        self.browser.find_element(By.ID, "id_login_password")
        input2 = self.browser.find_element(By.ID, "id_login_password")
        input2.send_keys({password})

    def test_autorization_stepik3(click):
        click.browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button1 = click.browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button1.click()
