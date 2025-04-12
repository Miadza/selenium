from selenium import webdriver
from registration_page import RegistrationPage
import time
import random

# Инициализация Firefox-драйвера
driver = webdriver.Firefox()
driver.get("https://automationpractice.pl/index.php")

page = RegistrationPage(driver)
page.open_signup()

# Генерируем уникальный email
email = f"user{random.randint(1000, 9999)}@test.com"
page.enter_email(email)
page.click_create_account()

time.sleep(3)  # Ожидаем загрузку формы

page.fill_personal_info("Test", "User", "Password123")
page.submit_registration()

# Проверка успешной регистрации — наличие "Sign out"
assert "Sign out" in driver.page_source

driver.quit()
