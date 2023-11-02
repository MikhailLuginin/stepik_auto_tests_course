import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepik():

    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_autorization_stepik(self, browser, links):
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(10)
        button = browser.find_element(By.LINK_TEXT, "Войти")
        button.click()
        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("rabotaluginin@gmail.com")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("Mihail221090")
        button1 = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button1.click()
        time.sleep(5)
        browser.implicitly_wait(10)
        input3 = browser.find_element(By.TAG_NAME, "textarea")
        input3.send_keys(str(math.log(int(time.time()))))
        time.sleep(5)
        browser.implicitly_wait(10)
        wait = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        wait.click()
        input4 = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "p"))).text
        welcome_text = input4

        assert "Correct!" == welcome_text

        if __name__ == "__main__":
            pytest.main()

