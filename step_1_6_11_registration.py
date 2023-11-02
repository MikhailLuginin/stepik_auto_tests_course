from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration_mandatory_fields(page_link: str):

    try:
        browser = webdriver.Chrome()
        browser.get(page_link)

        # Выводим ссылку на страницу
        print(page_link)

        # Заполнение обязательных полей
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys("test@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # выводим результат и с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if "Congratulations! You have successfully registered!" == welcome_text:
            print('test completed')

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':

    # проверяем каждую из ссылок
    links = [
        'http://suninjuly.github.io/registration1.html',
        'http://suninjuly.github.io/registration2.html'
    ]

    for link in links:
        test_registration_mandatory_fields(link)
