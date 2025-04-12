from test_utils import register_user, login_user, add_to_cart, checkout_cart
from selenium.webdriver.common.by import By
import time

def test_register(browser):
    register_user(browser, "TestUser", "testuser1234@example.com", "testpass123")
    assert "Account Created!" in browser.page_source

def test_login(browser):
    login_user(browser, "testuser1234@example.com", "testpass123")
    assert "Logged in as" in browser.page_source

def test_add_to_cart(browser):
    add_to_cart(browser)
    assert "View Cart" in browser.page_source

def test_checkout(browser):
    checkout_cart(browser)
    assert "Address Details" in browser.page_source
