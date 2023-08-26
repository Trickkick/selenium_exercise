import pytest
import time
from page_objects.NavigationPage import NavigationPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_navigation_page_find_elements(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.element(navigation_page.SHOP_CART)
    navigation_page.element(navigation_page.NAVIGATION_BAR)
    navigation_page.element(navigation_page.SEARCH_BUTTON)
    navigation_page.element(navigation_page.SEARCH_INPUT)
    navigation_page.element(navigation_page.CURRENCY_DROPDOWN)
    navigation_page.element(navigation_page.CART_TOTAL)
    navigation_page.navigation_search("hoho")
    navigation_page.switch_currency("EUR")
    navigation_page.go_to_registration()
    time.sleep(3)


def test_home_page_find_elements(browser):
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.slideshow.swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div.row")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.carousel.swiper-viewport")))


def test_admin_login_page_find_elements(browser):
    browser.get(browser.current_url + "/admin")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-logo")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-title")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block > a")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-right > button")))


def test_product_card_find_elements(browser):
    browser.get(browser.current_url + "/component/monitor/test")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.thumbnails")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-original-title='Compare this Product']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.nav-tabs")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tab-content")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#button-cart")))


def test_user_registration_page_find_elements(browser):
    browser.get(browser.current_url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-right")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".radio-inline")))


def test_catalog_find_elements(browser):
    browser.get(browser.current_url + "/component/monitor")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-group")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#list-view")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-limit")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-layout")))


def test_admin_add_product(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_page()
    admin_page.login_admin()
    admin_page.add_product("aaa", "aaa", "aaa")
    time.sleep(2)
    assert admin_page.find_product("aaa") is not None


def test_admin_delete_product(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_page()
    admin_page.login_admin()
    admin_page.go_to_product_table()
    # admin_page.delete_product_by_number(1)
    admin_page.delete_product_by_name("aaa")
    time.sleep(2)
    assert admin_page.find_product("aaa") is None


def test_user_register_with_alert(browser):
    registration_page = RegistrationPage(browser)
    NavigationPage(browser).go_to_registration()
    registration_page.register_account("a", "aa", "a@mail.ru", 444, "a23s")
    registration_page.element(registration_page.AGREE_ALERT).is_displayed()
    time.sleep(2)


def test_user_register_no_alert(browser):
    registration_page = RegistrationPage(browser)
    NavigationPage(browser).go_to_registration()
    registration_page.register_account("a", "aa", "aaa@mail.ru", 444, "a23s", "agree")
    time.sleep(2)


def test_switch_currency_positive(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.switch_currency("EUR")
    assert HomePage(browser).check_current_currency('€') == '€'


def test_switch_currency_negative(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.switch_currency("RUB")


def test_switch_pages(browser):
    home_page = HomePage(browser)
    NavigationPage(browser).go_to_registration()
    time.sleep(1)
    browser.get(browser.url + "/admin")
    time.sleep(1)
    browser.get(browser.url)
    time.sleep(1)
    AdminPage(browser).go_to_page()
    time.sleep(1)
    RegistrationPage(browser).go_to_page()
