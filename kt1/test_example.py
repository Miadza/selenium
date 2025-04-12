# test_example.py

def test_example(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
