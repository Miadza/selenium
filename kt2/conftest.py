import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "firefox":
        options = Options()
        # options.add_argument("--headless")  # если нужно скрыть окно
        service = Service()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается")

    yield driver
    driver.quit()
