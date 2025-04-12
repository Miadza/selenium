from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    SEARCH_RESULTS = (By.CLASS_NAME, "product_list")

    def search_for(self, query):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def is_result_displayed(self):
        return self.driver.find_element(*self.SEARCH_RESULTS).is_displayed()
