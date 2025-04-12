from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def register_user(driver, name, email, password):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(1)

    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()
    time.sleep(2)

    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("2000")
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()
    time.sleep(2)

def login_user(driver, email, password):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(1)

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

def add_to_cart(driver):
    driver.get("https://automationexercise.com/products")
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//a[contains(text(), 'Add to cart')])[1]").click()
    time.sleep(1)

def checkout_cart(driver):
    driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "check_out").click()
