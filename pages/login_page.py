from selenium.webdriver.common.by import By
from core.base_page import BasePage


# By putting BasePage in parentheses here, we tell Python:
# "LoginPage inherits everything from BasePage" (like 'extends' in Java)
class LoginPage(BasePage):
    # 1. Page Locators (Stored as Tuples)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 2. The Constructor
    def __init__(self, driver):
        # super().__init__() is Python's version of super(driver) in Java.
        # It hands the driver up to the BasePage.
        super().__init__(driver)

    # 3. Page Actions
    def login(self, username, password):
        # We use the smart methods we inherited from BasePage!
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)