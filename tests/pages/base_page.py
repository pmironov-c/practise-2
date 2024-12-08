import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def click_element(self, locator, timeout=5):
        self.find_element(locator, timeout).click()

    def wait_element(self, locator, explicit_timeout=5):
        errors = [NoSuchElementException, ElementNotInteractableException]
        WebDriverWait(
            self.driver,
            timeout=explicit_timeout,
            poll_frequency=0.2,
            ignored_exceptions=errors,
        ).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def hover_element(self, locator):
        e = self.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(e)
        hover.perform()

    def get_text(self, locator):
        return self.find_element(locator).text
