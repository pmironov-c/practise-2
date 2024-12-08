from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME_INPUT = (By.ID, "user_name")
    PASSWORD_INPUT = (By.ID, "username_password")
    SUBMIT_LOGIN = (By.ID, "bigbutton")
    DESKTOP_LOGOUT = (By.CSS_SELECTOR, ".desktop-bar #logout_link")


class LoginPage(BasePage):
    def set_user_name(self, user_name):
        self.find_element(LoginPageLocators.USER_NAME_INPUT).send_keys(user_name)

    def set_user_password(self, user_password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(user_password)

    def submit_login(self):
        self.click_element(LoginPageLocators.SUBMIT_LOGIN)
        self.wait_element(LoginPageLocators.DESKTOP_LOGOUT)

    def login_as_user(self, url, user_login, user_password):
        self.open_page(url)
        self.set_user_name(user_login)
        self.set_user_password(user_password)
        self.submit_login()
