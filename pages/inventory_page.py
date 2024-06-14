from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_price = (By.XPATH, "//*[@id="header_container"]/div[2]/div/span/select/option[4]")
        self.add_to_cart_button = (By.XPATH, "//div[text()='Sauce Labs Onesie']/following-sibling::button")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def sort_products(self, option):
        sort_dropdown = self.driver.find_element(*self.sort_dropdown)
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, f"//option[@value='{option}']").click()

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def is_button_changed(self):
        return self.driver.find_element(*self.add_to_cart_button).text == "Remove"

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
