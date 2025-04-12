from selenium import webdriver
from search_page import SearchPage

# Инициализация Firefox-драйвера
driver = webdriver.Firefox()
driver.get("https://automationpractice.pl/index.php")

page = SearchPage(driver)
page.search_for("dress")

# Проверка отображения результатов поиска
assert page.is_result_displayed()

driver.quit()
