from selenium.webdriver.common.by import By
from core.base_page import BasePage


class InventoryPage(BasePage):
    # Static Locators
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        super().__init__(driver)

    # Dynamic Locators (Generates the locator based on the product name!)
    def get_add_to_cart_button(self, item_name):
        return (By.ID, f"add-to-cart-{item_name}")

    def get_remove_button(self, item_name):
        return (By.ID, f"remove-{item_name}")

    # Page Actions
    def add_item_to_cart(self, item_name):
        self.click(self.get_add_to_cart_button(item_name))

    def remove_item_from_cart(self, item_name):
        self.click(self.get_remove_button(item_name))

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def logout(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)