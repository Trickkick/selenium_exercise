from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class RegistrationPage(BasePage):
    PATH_TO_PAGE = "/index.php?route=account/register"
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASS = (By.CSS_SELECTOR, "#input-confirm")
    AGREE = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE = (By.CSS_SELECTOR, "input.btn.btn-primary")
    AGREE_ALERT = (By.CSS_SELECTOR, ".alert")

    def register_account(self, firstname, lastname, email, telephone, password, agreement="no"):
        self.browser.execute_script("window.scrollTo(0, 180)")
        self._input(self.element(self.FIRST_NAME), firstname)
        self._input(self.element(self.LAST_NAME), lastname)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), telephone)
        self._input(self.element(self.PASSWORD), password)
        self._input(self.element(self.CONFIRM_PASS), password)
        if agreement == "agree":
            self.click(self.element(self.AGREE))
        self.click(self.element(self.CONTINUE))
        return self

    def go_to_page(self):
        self.browser.get(self.browser.url + self.PATH_TO_PAGE)
        return self
