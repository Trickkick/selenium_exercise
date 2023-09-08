from selenium.webdriver.common.by import By
import re

from page_objects.BasePage import BasePage


class HomePage(BasePage):
    SLIDESHOW_SWIPER = (By.CSS_SELECTOR, "div.slideshow.swiper-viewport")
    PRODUCTS = (By.CSS_SELECTOR, "div.product-layout")
    PRICES = (By.CSS_SELECTOR, ".price")

    def check_current_currency(self, cur):
        prices = self.elements(self.PRICES)
        for price in prices:
            match = re.search(fr'{cur}', price.text)
        return match.group()
