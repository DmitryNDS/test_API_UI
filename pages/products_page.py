from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".features_items .col-sm-4")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    PRODUCT_QUANTITY = (By.ID, "quantity")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.cart")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/view_cart']")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, ".btn-success")
    CATEGORY_TITLE = (By.CSS_SELECTOR, ".title")
    BRAND_FILTER = (By.CSS_SELECTOR, ".brands-name")
    BRAND_LINKS = (By.CSS_SELECTOR, ".brands-name a")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/products"

    def open(self):
        """Open the products page"""
        self.driver.get(self.url)

    def search_product(self, product_name):
        """Search for a product"""
        self.input_text(*self.SEARCH_INPUT, product_name)
        self.click(*self.SEARCH_BTN)

    def get_products_count(self):
        """Get total number of products displayed"""
        products = self.find_elements(*self.PRODUCTS_LIST)
        return len(products)

    def get_product_details(self, product_index=0):
        """Get product details by index"""
        products = self.find_elements(*self.PRODUCTS_LIST)
        if product_index < len(products):
            product = products[product_index]
            name = product.find_element(*self.PRODUCT_NAME).text
            price = product.find_element(*self.PRODUCT_PRICE).text
            return {"name": name, "price": price}
        return None

    def add_product_to_cart(self, product_index=0, quantity=1):
        """Add a product to cart with specified quantity"""
        products = self.find_elements(*self.PRODUCTS_LIST)
        if product_index < len(products):
            product = products[product_index]
            self.input_text(*self.PRODUCT_QUANTITY, str(quantity))
            self.click(*self.ADD_TO_CART_BTN)
            self.click(*self.CONTINUE_SHOPPING_BTN)
            return True
        return False

    def filter_by_brand(self, brand_name):
        """Filter products by brand name"""
        brand_links = self.find_elements(*self.BRAND_LINKS)
        for link in brand_links:
            if link.text.lower() == brand_name.lower():
                link.click()
                return True
        return False

    def get_category_title(self):
        """Get current category title"""
        return self.get_text(*self.CATEGORY_TITLE)

    def view_cart(self):
        """Click on View Cart button"""
        self.click(*self.VIEW_CART_BTN) 