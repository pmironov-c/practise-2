import os
import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPageLocators, LoginPage


class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    @classmethod
    def class_init(cls, browser):
        cls.url = os.environ.get("BASE_URL")
        cls.user_login = os.environ.get("USER_LOGIN")
        cls.user_password = os.environ.get("USER_PASSWORD")

        cls.login_page = LoginPage(browser)

    def test_login_as_user(self):
        TestLogin.login_page.login_as_user(
            TestLogin.url, TestLogin.user_login, TestLogin.user_password
        )

        assert TestLogin.login_page.find_element(
            LoginPageLocators.DESKTOP_LOGOUT
        ), "There is no logout button after login"
