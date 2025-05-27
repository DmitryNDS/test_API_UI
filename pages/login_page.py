from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Locators
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    SIGNUP_FORM = (By.CSS_SELECTOR, ".signup-form")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/login"

    def open(self):
        """Open the login page"""
        self.driver.get(self.url)

    def signup(self, name, email):
        """Sign up with name and email"""
        self.input_text(*self.SIGNUP_NAME, name)
        self.input_text(*self.SIGNUP_EMAIL, email)
        self.click(*self.SIGNUP_BTN)

    def login(self, email, password):
        """Login with email and password"""
        self.input_text(*self.LOGIN_EMAIL, email)
        self.input_text(*self.LOGIN_PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def get_error_message(self):
        """Get error message if login/signup fails"""
        return self.get_text(*self.ERROR_MESSAGE)

    def is_signup_form_visible(self):
        """Check if signup form is visible"""
        return self.is_element_present(*self.SIGNUP_FORM)

    def is_login_form_visible(self):
        """Check if login form is visible"""
        return self.is_element_present(*self.LOGIN_FORM) 