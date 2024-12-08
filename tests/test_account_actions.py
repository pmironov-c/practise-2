import os
import pytest
from datetime import datetime
from base_test import BaseTest
from pages.login_page import LoginPage
from pages.account_page import AccountPageLocators as account_locators, AccountPage


class TestAccounts(BaseTest):
    @pytest.fixture(autouse=True)
    @classmethod
    def pages_init(cls, browser):
        cls.login_page = LoginPage(browser)
        cls.account_page = AccountPage(browser)

    def test_open_account_module(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.account_page.click_accounts_in_nav_bar()

        assert self.account_page.get_text(account_locators.MODULE_TITLE) == "ACCOUNTS"

    def test_open_create_account_form(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.account_page.click_accounts_in_nav_bar()
        self.account_page.click_create_account()

        assert self.account_page.get_text(account_locators.MODULE_TITLE) == "CREATE"

    def test_save_empty_account(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.account_page.click_accounts_in_nav_bar()
        self.account_page.click_create_account()
        self.account_page.click_save_account()

        assert (
            self.account_page.get_text(account_locators.NAME_VERIF_MSG)
            == "Missing required field: Name"
        )

    def test_create_account(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.account_page.create_account(self.account_info)

        assert (
            self.account_page.get_text(account_locators.MODULE_TITLE).lower()
            == self.account_info["name"].lower()
        )
        assert (
            self.account_page.get_text(account_locators.ACCOUNT_NAME)
            == self.account_info["name"]
        )
        assert (
            self.account_page.get_text(account_locators.ACCOUNT_PHONE)
            == self.account_info["phone_number"]
        )
