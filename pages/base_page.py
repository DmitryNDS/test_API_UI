from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config.config import settings
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.IMPLICIT_WAIT)
        self.logger = logging.getLogger(__name__)

    def find_element(self, by: By, value: str, timeout: int = None):
        """Find element with explicit wait and retry on stale element"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        try:
            return wait.until(EC.presence_of_element_located((by, value)))
        except StaleElementReferenceException:
            self.logger.warning(f"Stale element encountered, retrying... ({by}={value})")
            return wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by: By, value: str, timeout: int = None):
        """Find elements with explicit wait"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        return wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by: By, value: str, timeout: int = None):
        """Click element with explicit wait and retry on stale element"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        try:
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except StaleElementReferenceException:
            self.logger.warning(f"Stale element encountered during click, retrying... ({by}={value})")
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()

    def input_text(self, by: By, value: str, text: str, timeout: int = None):
        """Input text with explicit wait and clear field first"""
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: By, value: str, timeout: int = None) -> str:
        """Get text with explicit wait"""
        element = self.find_element(by, value, timeout)
        return element.text

    def is_element_present(self, by: By, value: str, timeout: int = None) -> bool:
        """Check if element is present with explicit wait"""
        try:
            self.find_element(by, value, timeout)
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, by: By, value: str, timeout: int = None):
        """Wait for element to be visible"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_invisible(self, by: By, value: str, timeout: int = None):
        """Wait for element to be invisible"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        return wait.until(EC.invisibility_of_element_located((by, value)))

    def wait_for_element_clickable(self, by: By, value: str, timeout: int = None):
        """Wait for element to be clickable"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        return wait.until(EC.element_to_be_clickable((by, value)))

    def scroll_to_element(self, by: By, value: str, timeout: int = None):
        """Scroll element into view"""
        element = self.find_element(by, value, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def hover_over_element(self, by: By, value: str, timeout: int = None):
        """Hover over element"""
        element = self.find_element(by, value, timeout)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def wait_for_page_load(self, timeout: int = None):
        """Wait for page to load completely"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def wait_for_ajax(self, timeout: int = None):
        """Wait for all AJAX requests to complete"""
        wait = WebDriverWait(self.driver, timeout or settings.IMPLICIT_WAIT)
        wait.until(lambda driver: driver.execute_script('return jQuery.active == 0'))

    def get_current_url(self) -> str:
        """Get current URL"""
        return self.driver.current_url

    def refresh_page(self):
        """Refresh current page"""
        self.driver.refresh()
        self.wait_for_page_load() 