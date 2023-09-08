import pytest
import allure
import time
from page_objects.NavigationPage import NavigationPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.HomePage import HomePage
from page_objects.AdminPage import AdminPage


@allure.feature("Navigation Page")
@allure.title("Find elements on navigation page")
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


@allure.feature("Home page")
@allure.title("Find elements on home page")
def test_home_page_find_elements(browser):
    home_page = HomePage(browser)
    home_page.element(home_page.SLIDESHOW_SWIPER)
    home_page.element(home_page.PRODUCTS)
    home_page.element(home_page.PRICES)


@allure.feature("Admin page")
@allure.feature("Find elements on admin login page")
def test_admin_login_page_find_elements(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_page()
    admin_page.element(admin_page.HEADER_LOGO)
    admin_page.element(admin_page.PANEL_TITLE)
    admin_page.element(admin_page.USERNAME)
    admin_page.element(admin_page.PASSWORD)
    admin_page.element(admin_page.LOGIN_BUTTON)


@allure.feature("Admin page")
@allure.feature("Add new product on admin page")
def test_admin_add_product(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_page()
    admin_page.login_admin()
    admin_page.add_product("aaa", "aaa", "aaa")
    time.sleep(2)
    assert admin_page.find_product("aaa") is not None


@allure.feature("Admin page")
@allure.feature("Delete new product on admin page")
def test_admin_delete_product(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_page()
    admin_page.login_admin()
    admin_page.go_to_product_table()
    # admin_page.delete_product_by_number(1)
    admin_page.delete_product_by_name("aaa")
    time.sleep(2)
    assert admin_page.find_product("aaa") is None


@allure.feature("Registration page")
@allure.feature("Register new user")
def test_user_register_with_alert(browser):
    registration_page = RegistrationPage(browser)
    NavigationPage(browser).go_to_registration()
    registration_page.register_account("a", "aa", "a@mail.ru", 444, "a23s")
    registration_page.element(registration_page.AGREE_ALERT).is_displayed()
    time.sleep(2)


@allure.feature("Registration page")
@allure.feature("Register new user without alert")
def test_user_register_no_alert(browser):
    registration_page = RegistrationPage(browser)
    NavigationPage(browser).go_to_registration()
    registration_page.register_account("a", "aa", "aaaa@mail.ru", 444, "a23asds", "agree")
    time.sleep(2)


@allure.feature("Navigation page")
@allure.feature("Switch currency positive")
def test_switch_currency_positive(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.switch_currency("EUR")
    assert HomePage(browser).check_current_currency('€') == '€'


@allure.feature("Navigation page")
@allure.feature("Switch currency negative")
def test_switch_currency_negative(browser):
    navigation_page = NavigationPage(browser)
    navigation_page.switch_currency("RUB")
