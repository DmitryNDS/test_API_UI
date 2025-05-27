from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.IMPLICIT_WAIT)

    def find_element(self, by: By, value: str):
        """Find element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by: By, value: str):
        """Find elements with explicit wait."""
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by: By, value: str):
        """Click element with explicit wait."""
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_text(self, by: By, value: str, text: str):
        """Input text with explicit wait."""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: By, value: str) -> str:
        """Get text with explicit wait."""
        element = self.find_element(by, value)
        return element.text

    def is_element_present(self, by: By, value: str, timeout: int = None) -> bool:
        """Check if element is present."""
        try:
            self.wait.until(EC.presence_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, by: By, value: str, timeout: int = None):
        """Wait for element to be visible."""
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_invisible(self, by: By, value: str, timeout: int = None):
        """Wait for element to be invisible."""
        return self.wait.until(EC.invisibility_of_element_located((by, value))) 