import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def api_base_url():
    """Return the base URL for API testing."""
    return os.getenv("API_BASE_URL")

@pytest.fixture(scope="session")
def ui_base_url():
    """Return the base URL for UI testing."""
    return os.getenv("UI_BASE_URL")

@pytest.fixture(scope="function")
def driver():
    """Create and return a WebDriver instance."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def faker():
    """Create and return a Faker instance."""
    from faker import Faker
    return Faker() 