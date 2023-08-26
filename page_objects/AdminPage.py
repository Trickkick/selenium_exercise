import time

from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    PATH_TO_PAGE = "/admin"
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".text-right > button")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_MENU = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)")
    ADD_NEW = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    PRODUCT_TAGS_INPUT = (By.CSS_SELECTOR, "#input-tag1")
    DATA_TAB = (By.CSS_SELECTOR, "[href='#tab-data']")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Save']")
    TABLE = (By.CSS_SELECTOR, ".table-hover > tbody ")
    TABLE_PRODUCTS = (By.CSS_SELECTOR, ".table-hover > tbody > tr")
    CHECK_BOX = (By.CSS_SELECTOR, '.table-hover > tbody > tr:first-child > td:first-child >input')
    PRODUCT_NAME_ELEMENT = (By.CSS_SELECTOR, "td:nth-child(3)")
    CHECK_BOX_ELEMENT = (By.CSS_SELECTOR, "td:first-child >input")
    DELETE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Delete']")

    def go_to_page(self):
        self.browser.get(self.browser.url + self.PATH_TO_PAGE)
        return self

    def login_admin(self, username="user", password="bitnami"):
        self._input(self.element(self.USERNAME), username)
        self._input(self.element(self.PASSWORD), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def go_to_product_table(self):
        self.click(self.element(self.CATALOG_MENU))
        self.click(self.element(self.PRODUCTS_MENU))
        return self

    def add_product(self, product_name, meta_tag, model, tags=""):
        self.go_to_product_table()
        self.click(self.element(self.ADD_NEW))
        self._input(self.element(self.PRODUCT_NAME_INPUT), product_name)
        self._input(self.element(self.META_TAG_INPUT), meta_tag)
        self.click(self.element(self.DATA_TAB))
        self._input(self.element(self.MODEL_INPUT), model)
        self.browser.execute_script("window.scrollTo(0, 0)")
        self.click(self.element(self.SAVE_BUTTON))
        return self

    def delete_product_by_number(self, number):
        self.go_to_product_table()
        self.click(
            self.element_in_element(self.TABLE, (By.CSS_SELECTOR, f"tr:nth-child({number}) > td:first-child >input")))
        self.click(self.element(self.DELETE_BUTTON))
        self.accept_alert()
        return self

    def save_product_name(self, product):
        prod_name = product.find_element(*self.PRODUCT_NAME_ELEMENT).text
        return prod_name

    def find_product(self, product_name):
        products = self.elements(self.TABLE_PRODUCTS)
        for product in products:
            prod_name = self.save_product_name(product)
            if prod_name == product_name:
                return product

    def select_product(self, product_name):
        product = self.find_product(product_name)
        self.click(product.find_element(*self.CHECK_BOX_ELEMENT))
        return self

    def delete_product_by_name(self, product_name):
        self.go_to_product_table()
        self.select_product(product_name)
        self.click(self.element(self.DELETE_BUTTON))
        self.accept_alert()
        return self
