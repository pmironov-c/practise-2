import os
import subprocess
from datetime import datetime

import pytest
from dotenv import load_dotenv
from selenium import webdriver


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.environ.get("BROWSER"))
    parser.addoption("--base-url", action="store", default=os.environ.get("BASE_URL"))


@pytest.fixture()
def browser_type():
    return os.environ.get("BROWSER")


@pytest.fixture()
def browser(browser_type):
    driver = []
    if browser_type == "chrome":
        options = webdriver.ChromeOptions()
        options.timeouts = {"pageLoad": 5 * 10e3, "script": 5 * 10e3}
        options.page_load_strategy = "normal"
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized --auto-open-devtools-for-tabs")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_type == "firefox":
        options = webdriver.FirefoxOptions()
        options.timeouts = {"pageLoad": 5 * 10e3, "script": 5 * 10e3}
        options.page_load_strategy = "normal"
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    yield driver
    driver.quit()
