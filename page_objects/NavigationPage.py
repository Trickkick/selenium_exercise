from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class NavigationPage(BasePage):
    SHOP_CART = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(4) > a > i")
    REG_LOG_DROPDOWN = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(2)")
    REG_BUTTON_IN_DROPDOWN = (By.CSS_SELECTOR, "ul > li:nth-child(1)")
    LOG_BUTTON_IN_DROPDOWN = (By.CSS_SELECTOR, "ul > li:nth-child(2)")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency > div > button")
    CURRENCY_EUR = (By.CSS_SELECTOR, "[name='EUR']")
    CURRENCY_GBP = (By.CSS_SELECTOR, "[name='GBP']")
    CURRENCY_USD = (By.CSS_SELECTOR, "[name='USD']")

    def navigation_search(self, input_search):
        self._input(self.element(self.SEARCH_INPUT), input_search)
        self.click(self.element(self.SEARCH_BUTTON))
        return self

    def navigation_to_cart(self):
        self.click(self.element(self.SHOP_CART))
        return self

    def switch_currency(self, currency):
        self.click(self.element(self.CURRENCY_DROPDOWN))
        if currency == "EUR":
            self.click(self.element(self.CURRENCY_EUR))
        elif currency == "GBP":
            self.click(self.element(self.CURRENCY_GBP))
        elif currency == "USD":
            self.click(self.element(self.CURRENCY_USD))
        else:
            try:
                self.click(self.element((By.CSS_SELECTOR, f"[name='{currency}']")))
            except AssertionError:
                print(f"{currency} отсутствует в списке")
        return self

    def go_to_registration(self):
        self.click(self.element(self.REG_LOG_DROPDOWN))
        button = self.element_in_element(self.REG_LOG_DROPDOWN, self.REG_BUTTON_IN_DROPDOWN)
        self.click(button)
        return self
