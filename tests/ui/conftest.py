import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture(scope="function")
def driver():
    """Create and configure Chrome WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # Configure ChromeDriver for Mac ARM
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    """Create HomePage instance"""
    return HomePage(driver)

@pytest.fixture
def login_page(driver):
    """Create LoginPage instance"""
    return LoginPage(driver)

@pytest.fixture
def products_page(driver):
    """Create ProductsPage instance"""
    return ProductsPage(driver)

@pytest.fixture
def cart_page(driver):
    """Create CartPage instance"""
    return CartPage(driver)

@pytest.fixture
def registered_user():
    """Return test user credentials"""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    } 