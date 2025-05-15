import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def login(self, username: str, password: str):
        """Perform login action."""
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Get error message if login fails."""
        return self.get_text(*self.ERROR_MESSAGE)

@pytest.mark.ui
class TestLogin:
    def test_successful_login(self, driver, ui_base_url):
        """Test successful login with valid credentials."""
        driver.get(ui_base_url)
        login_page = LoginPage(driver)
        
        login_page.login("valid_user", "valid_password")
        
        # Add assertions based on your application's behavior
        # For example, check if user is redirected to dashboard
        assert driver.current_url.endswith("/dashboard")

    def test_failed_login(self, driver, ui_base_url):
        """Test login with invalid credentials."""
        driver.get(ui_base_url)
        login_page = LoginPage(driver)
        
        login_page.login("invalid_user", "invalid_password")
        
        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message 