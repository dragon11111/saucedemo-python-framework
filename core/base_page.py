from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # 1. The Constructor (Equivalent to public BasePage(WebDriver driver) in Java)
    def __init__(self, driver):
        self.driver = driver
        # We set a default Explicit Wait of 10 seconds for all actions
        self.wait = WebDriverWait(self.driver, 10)

    # 2. Smart Click Method
    def click(self, locator):
        # Waits for the element to be clickable, then clicks it
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # 3. Smart Type Method (Equivalent to sendKeys)
    def enter_text(self, locator, text):
        # Waits for the element to be visible, clears any existing text, then types
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # 4. Smart Get Text Method
    def get_text(self, locator):
        # Waits for visibility, then returns the text inside the element
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text