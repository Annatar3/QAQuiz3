from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_item_price(self):
        return self.driver.find_element(*self.cart_item_price).text

    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item_name).text

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
