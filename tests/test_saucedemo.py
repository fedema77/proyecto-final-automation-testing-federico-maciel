import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.file_reader import load_json

USERS = load_json("users.json")
VALID_USER = USERS["valid_user"]
INVALID_USER = USERS["invalid_user"]
LOCKED_USER = USERS["locked_user"]


@pytest.fixture
def logged_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    return driver


def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_on_inventory_page()
    assert inventory_page.get_page_title_text() == "Products"


def test_login_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(INVALID_USER["username"], INVALID_USER["password"])

    assert login_page.is_error_visible()
    assert "Username and password do not match" in login_page.get_error_message()


def test_login_locked_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOCKED_USER["username"], LOCKED_USER["password"])

    assert login_page.is_error_visible()
    assert "locked out" in login_page.get_error_message().lower()


def test_inventory_has_products(logged_driver):
    inventory_page = InventoryPage(logged_driver)

    assert inventory_page.is_menu_visible()
    assert inventory_page.is_sort_dropdown_visible()
    assert inventory_page.get_products_count() > 0
    assert "Sauce Labs Backpack" in inventory_page.get_first_product_name()


def test_add_product_to_cart(logged_driver):
    inventory_page = InventoryPage(logged_driver)
    inventory_page.add_first_product_to_cart()

    assert inventory_page.get_cart_badge_value() == "1"


def test_complete_checkout(logged_driver):
    inventory_page = InventoryPage(logged_driver)
    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_driver)
    assert cart_page.get_cart_items_count() == 1
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(logged_driver)
    checkout_page.fill_customer_info("Federico", "Maciel", "1234")
    checkout_page.finish_checkout()

    assert checkout_page.get_completion_message() == "Thank you for your order!"