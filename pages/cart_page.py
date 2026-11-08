from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_name(self):
        return self.driver.find_element(*self.ITEM_NAME).text

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
