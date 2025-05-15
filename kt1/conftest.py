# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Тип браузера: chrome или firefox"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")  # можно убрать, если хочешь видеть браузер
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")  # можно убрать
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    yield driver
    driver.quit()
