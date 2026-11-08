from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    def is_on_inventory_page(self):
        return self.driver.current_url.endswith("/inventory.html") and self.get_title() == "Swag Labs"

    def get_products_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_first_product_name(self):
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return items[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.ADD_TO_CART_BUTTON)[0].click()

    def get_cart_badge_value(self):
        try:
            return self.find(self.CART_BADGE).text
        except Exception:
            return "0"

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    def is_menu_visible(self):
        return self.is_displayed(self.MENU_BUTTON)

    def is_sort_dropdown_visible(self):
        return self.is_displayed(self.SORT_DROPDOWN)

    def get_page_title_text(self):
        return self.get_text(self.PAGE_TITLE)
