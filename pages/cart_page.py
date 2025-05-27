from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    ITEM_NAME = (By.CSS_SELECTOR, ".cart_description h4 a")
    ITEM_PRICE = (By.CSS_SELECTOR, ".cart_price p")
    ITEM_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity button")
    ITEM_TOTAL = (By.CSS_SELECTOR, ".cart_total p")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, ".btn-default.check_out")
    EMPTY_CART_BTN = (By.CSS_SELECTOR, ".btn-danger")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#empty_cart p")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, ".btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/view_cart"

    def open(self):
        """Open the cart page"""
        self.driver.get(self.url)

    def get_cart_items(self):
        """Get all items in the cart"""
        items = self.find_elements(*self.CART_ITEMS)
        cart_items = []
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            quantity = item.find_element(*self.ITEM_QUANTITY).text
            total = item.find_element(*self.ITEM_TOTAL).text
            cart_items.append({
                "name": name,
                "price": price,
                "quantity": quantity,
                "total": total
            })
        return cart_items

    def get_cart_total(self):
        """Get total number of items in cart"""
        return len(self.find_elements(*self.CART_ITEMS))

    def remove_item(self, item_index=0):
        """Remove item from cart by index"""
        items = self.find_elements(*self.CART_ITEMS)
        if item_index < len(items):
            remove_btn = items[item_index].find_element(*self.EMPTY_CART_BTN)
            remove_btn.click()
            return True
        return False

    def clear_cart(self):
        """Remove all items from cart"""
        items = self.find_elements(*self.CART_ITEMS)
        for _ in range(len(items)):
            self.remove_item(0)

    def proceed_to_checkout(self):
        """Click on Proceed to Checkout button"""
        self.click(*self.PROCEED_TO_CHECKOUT_BTN)

    def continue_shopping(self):
        """Click on Continue Shopping button"""
        self.click(*self.CONTINUE_SHOPPING_BTN)

    def is_cart_empty(self):
        """Check if cart is empty"""
        return self.is_element_present(*self.EMPTY_CART_MESSAGE)

    def get_empty_cart_message(self):
        """Get empty cart message"""
        return self.get_text(*self.EMPTY_CART_MESSAGE) 