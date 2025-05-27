from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    # Locators
    SIGNUP_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    CART_BTN = (By.CSS_SELECTOR, "a[href='/view_cart']")
    CONTACT_US_BTN = (By.CSS_SELECTOR, "a[href='/contact_us']")
    TEST_CASES_BTN = (By.CSS_SELECTOR, "a[href='/test_cases']")
    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BTN = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    FEATURED_ITEMS = (By.CSS_SELECTOR, ".features_items .col-sm-4")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, ".btn-success")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/"

    def open(self):
        """Open the home page"""
        self.driver.get(self.url)

    def click_signup_login(self):
        """Click on Signup/Login button"""
        self.click(*self.SIGNUP_LOGIN_BTN)

    def click_products(self):
        """Click on Products button"""
        self.click(*self.PRODUCTS_BTN)

    def click_cart(self):
        """Click on Cart button"""
        self.click(*self.CART_BTN)

    def click_contact_us(self):
        """Click on Contact Us button"""
        self.click(*self.CONTACT_US_BTN)

    def click_test_cases(self):
        """Click on Test Cases button"""
        self.click(*self.TEST_CASES_BTN)

    def subscribe_to_newsletter(self, email):
        """Subscribe to newsletter with given email"""
        self.input_text(*self.SUBSCRIPTION_EMAIL, email)
        self.click(*self.SUBSCRIPTION_BTN)

    def get_subscription_success_message(self):
        """Get subscription success message"""
        return self.get_text(*self.SUBSCRIPTION_SUCCESS)

    def add_product_to_cart(self, product_index=0):
        """Add a product to cart by index"""
        products = self.find_elements(*self.FEATURED_ITEMS)
        if product_index < len(products):
            add_to_cart_btn = products[product_index].find_element(*self.ADD_TO_CART_BTN)
            self.driver.execute_script("arguments[0].click();", add_to_cart_btn)
            self.click(*self.CONTINUE_SHOPPING_BTN)
            return True
        return False

    def view_cart(self):
        """Click on View Cart button"""
        self.click(*self.VIEW_CART_BTN) 