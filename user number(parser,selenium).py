from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_phone_number(url):
    # Запускаємо браузер (наприклад, Chrome)
    driver = webdriver.Chrome()

    try:
        # Відкриваємо веб-сайт
        driver.get(url)

        # Знаходимо кнопку, на яку ми хочемо натиснути
        block = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.css-1l3tcy7'))
        )

        # Натискаємо на кнопку
        block.click()

        # Отримуємо номер, який з'являється після натискання на блок
        number_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.css-v1ndtc'))
        )
        number = number_element.text

        return number
    finally:
        # Закриваємо браузер навіть у випадку помилки
        driver.quit()

# Передаємо URL сторінки, з якої ми хочемо отримати номер телефону
url = 'https://www.olx.ua/d/uk/obyavlenie/mazda-cx-5-black-edition-4wd-2023-IDUkdc8.html'
phone_number = get_phone_number(url)
print('Phone number:', phone_number)
