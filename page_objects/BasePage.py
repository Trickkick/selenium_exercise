import os
import logging
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()
        self.class_name = type(self).__name__

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step
    def click(self, element):
        self.logger.info(f"{self.class_name}: Clicking element: {element}")
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def _input(self, element, value):
        self.logger.info(f"{self.class_name}: Input {value} in {element}")
        self.click(element)
        element.clear()
        element.send_keys(value)

    @allure.step
    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info(f"{self.class_name}: search {child_locator} in {parent_locator}")
        return self.element(parent_locator).find_element(*child_locator)

    @allure.step
    def element(self, locator: tuple):
        try:
            self.logger.info(f"{self.class_name}: Search element: {locator}")
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout Exception: {locator}")
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    @allure.step
    def elements(self, locator: tuple):
        try:
            self.logger.info(f"{self.class_name}: Search element {locator}")
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout Exception: {locator}")
            with allure.step("Attach screenshot"):
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="Screenshot",
                    attachment_type = allure.attachment_type.PNG
                )
                raise AssertionError(f"Не дождался видимости элементов {locator}")

    @allure.step
    def verify_product_item(self, product_name):
        self.logger.info(f"{self.class_name}: Verify product {product_name}")
        return self.element((By.LINK_TEXT, product_name))

    @allure.step
    def accept_alert(self):
        self.logger.info(f"{self.class_name}: Accept alert")
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        self.browser.switch_to.alert.accept()
