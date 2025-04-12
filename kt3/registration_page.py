from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    SIGN_IN_LINK = (By.CLASS_NAME, "login")
    EMAIL_INPUT = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    GENDER_MALE_RADIO = (By.ID, "id_gender1")
    FIRSTNAME_INPUT = (By.ID, "customer_firstname")
    LASTNAME_INPUT = (By.ID, "customer_lastname")
    PASSWORD_INPUT = (By.ID, "passwd")
    REGISTER_BUTTON = (By.ID, "submitAccount")

    # Методы
    def open_signup(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_create_account(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()

    def fill_personal_info(self, firstname, lastname, password):
        self.driver.find_element(*self.GENDER_MALE_RADIO).click()
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()
