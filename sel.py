KO
from selenium import webdriver

   # Укажите путь к ChromeDriver, если он не в PATH
driver = webdriver.Chrome()  # или webdriver.Firefox() для Firefox
driver.get("https://www.google.com")

print(driver.title)
driver.quit()