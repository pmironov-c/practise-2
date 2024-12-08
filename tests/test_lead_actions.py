import os
import pytest
from base_test import BaseTest
from pages.login_page import LoginPage
from pages.lead_page import LeadPageLocators as lead_locators, LeadPage


class TestLeads(BaseTest):
    @pytest.fixture(autouse=True)
    @classmethod
    def class_init(cls, browser):
        cls.login_page = LoginPage(browser)
        cls.lead_page = LeadPage(browser)

    def test_open_lead_module(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.lead_page.click_leads_in_nav_bar()

        assert self.lead_page.get_text(lead_locators.MODULE_TITLE) == "LEADS"

    def test_open_create_lead_form(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.lead_page.click_leads_in_nav_bar()
        self.lead_page.click_create_lead()

        assert self.lead_page.get_text(lead_locators.MODULE_TITLE) == "CREATE"

    def test_save_empty_lead(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.lead_page.click_leads_in_nav_bar()
        self.lead_page.click_create_lead()
        self.lead_page.click_save_lead()

        assert (
            self.lead_page.get_text(lead_locators.LASTNAME_VERIF_MSG)
            == "Missing required field: Last Name"
        )

    def test_create_lead(self):
        self.login_page.login_as_user(self.url, self.user_login, self.user_password)
        self.lead_page.create_lead(self.lead_info)

        assert (
            self.lead_page.get_text(lead_locators.MODULE_TITLE).lower()
            == self.lead_info["lead_name"].lower()
        )
        assert (
            self.lead_page.get_text(lead_locators.LEAD_NAME)
            == self.lead_info["lead_name"]
        )
        assert (
            self.lead_page.get_text(lead_locators.LEAD_PHONE)
            == self.lead_info["phone_number"]
        )
