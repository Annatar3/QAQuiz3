import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="module")
def setup(driver):
    driver.get("https://www.saucedemo.com/")
    return driver

@allure.feature("Login Tests")
def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in setup.current_url

@allure.feature("Login Tests")
def test_login_invalid(setup):
    login_page = LoginPage(setup)
    login_page.login("invalid_user", "invalid_password")
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

@allure.feature("Product Sorting")
def test_sort_products(setup):
    inventory_page = InventoryPage(setup)
    inventory_page.sort_products("lohi")
    price = inventory_page.get_product_price()
    assert price == "$7.99"  # Assuming $7.99 is the lowest price product

@allure.feature("Add to Cart")
def test_add_to_cart(setup):
    inventory_page = InventoryPage(setup)
    inventory_page.add_to_cart()
    assert inventory_page.is_button_changed()

@allure.feature("Cart Operations")
def test_cart_operations(setup):
    inventory_page = InventoryPage(setup)
    inventory_page.go_to_cart()

    cart_page = CartPage(setup)
    cart_item_price = cart_page.get_cart_item_price()
    assert cart_item_price == "$7.99"  # Assuming this is the price of the item added to the cart

    cart_item_name = cart_page.get_cart_item_name()
    assert cart_item_name == "Sauce Labs Onesie"  # Assuming this is the item name

@allure.feature("Checkout")
def test_checkout_error_message(setup):
    cart_page = CartPage(setup)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(setup)
    checkout_page.click_continue()
    error_message = checkout_page.get_error_message()
    assert "Error: First Name is required" in error_message  # Assuming this is the error message for missing first name
