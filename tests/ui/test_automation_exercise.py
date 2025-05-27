import pytest
import allure
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

fake = Faker()

@allure.feature("Home Page")
@allure.story("Home Page Functionality")
class TestHomePage:
    @allure.title("Verify home page is visible")
    @allure.description("""
    Test Steps:
    1. Open the home page
    2. Verify that the page is loaded by checking the presence of Signup/Login button
    3. Verify that the page title is correct
    """)
    def test_home_page_visibility(self, home_page):
        with allure.step("Open home page"):
            home_page.open()
        
        with allure.step("Verify page elements"):
            assert home_page.is_element_present(*home_page.SIGNUP_LOGIN_BTN)
            assert "Automation Exercise" in home_page.driver.title

    @allure.title("Subscribe to newsletter")
    @allure.description("""
    Test Steps:
    1. Open the home page
    2. Scroll to newsletter subscription section
    3. Enter a valid email address
    4. Click subscribe button
    5. Verify success message
    """)
    def test_newsletter_subscription(self, home_page):
        with allure.step("Open home page"):
            home_page.open()
        
        with allure.step("Generate and enter email"):
            email = fake.email()
            home_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # Wait for scroll animation
        
        with allure.step("Subscribe to newsletter"):
            home_page.subscribe_to_newsletter(email)
        
        with allure.step("Verify subscription success"):
            success_message = home_page.get_subscription_success_message()
            assert "You have been successfully subscribed!" in success_message

@allure.feature("Login and Registration")
@allure.story("User Authentication")
class TestLoginRegistration:
    @allure.title("Register new user")
    @allure.description("""
    Test Steps:
    1. Open login page
    2. Generate random user data
    3. Fill in registration form
    4. Submit registration
    5. Verify registration form is visible
    """)
    def test_register_new_user(self, login_page):
        with allure.step("Open login page"):
            login_page.open()
        
        with allure.step("Generate user data"):
            name = fake.name()
            email = fake.email()
        
        with allure.step("Fill registration form"):
            login_page.signup(name, email)
        
        with allure.step("Verify registration form"):
            assert login_page.is_signup_form_visible()

    @allure.title("Login with valid credentials")
    @allure.description("""
    Test Steps:
    1. Open login page
    2. Enter valid credentials
    3. Submit login form
    4. Verify successful login
    """)
    def test_login_valid_credentials(self, login_page, registered_user):
        with allure.step("Open login page"):
            login_page.open()
        
        with allure.step("Enter credentials"):
            login_page.login(registered_user["email"], registered_user["password"])
        
        with allure.step("Verify successful login"):
            assert not login_page.is_element_present(*login_page.ERROR_MESSAGE)

    @allure.title("Login with invalid credentials")
    @allure.description("""
    Test Steps:
    1. Open login page
    2. Enter invalid credentials
    3. Submit login form
    4. Verify error message
    """)
    def test_login_invalid_credentials(self, login_page):
        with allure.step("Open login page"):
            login_page.open()
        
        with allure.step("Enter invalid credentials"):
            login_page.login("invalid@email.com", "wrongpassword")
        
        with allure.step("Verify error message"):
            assert login_page.is_element_present(*login_page.ERROR_MESSAGE)
            error_message = login_page.get_error_message()
            assert "Your email or password is incorrect!" in error_message

@allure.feature("Products")
@allure.story("Product Management")
class TestProducts:
    @allure.title("Search products")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Enter search term
    3. Submit search
    4. Verify search results
    """)
    def test_search_products(self, products_page):
        with allure.step("Open products page"):
            products_page.open()
        
        with allure.step("Search for products"):
            products_page.search_product("dress")
            time.sleep(1)  # Wait for search results to load
        
        with allure.step("Verify search results"):
            assert products_page.get_products_count() > 0

    @allure.title("Add product to cart")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Get initial cart count
    3. Add product to cart
    4. Verify cart count increased
    """)
    def test_add_product_to_cart(self, products_page, cart_page):
        with allure.step("Open products page"):
            products_page.open()
        
        with allure.step("Get initial cart count"):
            initial_cart_count = cart_page.get_cart_total()
        
        with allure.step("Add product to cart"):
            products_page.add_product_to_cart(0, 2)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Verify cart update"):
            cart_page.open()
            assert cart_page.get_cart_total() > initial_cart_count

    @allure.title("Filter products by brand")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Select brand filter
    3. Verify filtered results
    """)
    def test_filter_by_brand(self, products_page):
        with allure.step("Open products page"):
            products_page.open()
        
        with allure.step("Apply brand filter"):
            products_page.filter_by_brand("Polo")
            time.sleep(1)  # Wait for filter to apply
        
        with allure.step("Verify filtered results"):
            assert "Polo" in products_page.get_category_title()

@allure.feature("Shopping Cart")
@allure.story("Cart Management")
class TestShoppingCart:
    @allure.title("Add multiple products to cart")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Add first product to cart
    3. Add second product to cart
    4. Verify cart contains both products
    """)
    def test_add_multiple_products(self, products_page, cart_page):
        with allure.step("Open products page"):
            products_page.open()
        
        with allure.step("Add first product"):
            products_page.add_product_to_cart(0)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Add second product"):
            products_page.add_product_to_cart(1)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Verify cart contents"):
            cart_page.open()
            assert cart_page.get_cart_total() == 2

    @allure.title("Remove product from cart")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Add product to cart
    3. Open cart
    4. Remove product
    5. Verify cart is empty
    """)
    def test_remove_product(self, products_page, cart_page):
        with allure.step("Add product to cart"):
            products_page.open()
            products_page.add_product_to_cart(0)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Open cart and remove product"):
            cart_page.open()
            initial_count = cart_page.get_cart_total()
            cart_page.remove_item(0)
            time.sleep(1)  # Wait for removal
        
        with allure.step("Verify product removal"):
            assert cart_page.get_cart_total() < initial_count

    @allure.title("Clear cart")
    @allure.description("""
    Test Steps:
    1. Open products page
    2. Add multiple products
    3. Open cart
    4. Clear cart
    5. Verify cart is empty
    """)
    def test_clear_cart(self, products_page, cart_page):
        with allure.step("Add products to cart"):
            products_page.open()
            products_page.add_product_to_cart(0)
            time.sleep(1)  # Wait for cart update
            products_page.add_product_to_cart(1)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Clear cart"):
            cart_page.open()
            cart_page.clear_cart()
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Verify cart is empty"):
            assert cart_page.is_cart_empty()

@allure.feature("End-to-End Flow")
@allure.story("Complete Purchase Process")
class TestEndToEnd:
    @allure.title("Complete purchase flow")
    @allure.description("""
    Test Steps:
    1. Open home page
    2. Login with valid credentials
    3. Add products to cart
    4. Verify cart contents
    5. Proceed to checkout
    """)
    def test_complete_purchase(self, home_page, login_page, products_page, cart_page, registered_user):
        with allure.step("Login to account"):
            home_page.open()
            home_page.click_signup_login()
            login_page.login(registered_user["email"], registered_user["password"])
            time.sleep(1)  # Wait for login
        
        with allure.step("Add products to cart"):
            products_page.open()
            products_page.add_product_to_cart(0)
            time.sleep(1)  # Wait for cart update
            products_page.add_product_to_cart(1)
            time.sleep(1)  # Wait for cart update
        
        with allure.step("Verify cart and proceed to checkout"):
            cart_page.open()
            assert cart_page.get_cart_total() == 2
            cart_page.proceed_to_checkout() 