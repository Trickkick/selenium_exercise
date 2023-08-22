import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser you want to use")
    parser.addoption("--url", action="store", default="http://192.168.50.8:8081", help="testing url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers_path = "C:/drv/"

    if browser_name == "chrome":
        chrome_driver_path = os.path.expanduser(drivers_path + "chromedriver.exe")
        chrome_options = ChromiumOptions()
        chrome_service = ChromiumService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser_name == "firefox":
        firefox_driver_path = os.path.expanduser(drivers_path + "firefoxdriver.exe")
        firefox_options = FFOptions()
        firefox_service = FFService(executable_path=firefox_driver_path)
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    else:
        edge_driver_path = os.path.expanduser(drivers_path + "edgedriver.exe")
        edge_options = EdgeOptions()
        edge_service = EdgeService(executable_path=edge_driver_path)
        driver = webdriver.Edge(service=edge_service, options=edge_options)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
