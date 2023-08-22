import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_home_page_find_elements(browser):
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.pull-left")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.nav.pull-right")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.navbar-nav")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.col-sm-5")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.slideshow.swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div.row")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.carousel.swiper-viewport")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))


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
