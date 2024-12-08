from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPageLocators:
    MARKETING_NAV_BAR = (By.ID, "grouptab_1")
    ACCOUNTS_MENU_OPTION = (
        By.XPATH,
        '//*[@id="grouptab_1"]/..//*[@id="moduleTab_2_Accounts"]',
    )

    MODULE_TITLE = (By.CSS_SELECTOR, ".moduleTitle .module-title-text")

    CREATE_ACCOUNT = (
        By.XPATH,
        '//*[@class="actionmenulink" and text()="Create Account"]',
    )

    EDIT_VIEW = (By.ID, "EditView")
    SAVE_BTN = (By.ID, "SAVE")
    NAME_INPUT = (By.ID, "name")
    PHONE_NUMBER_INPUT = (By.ID, "phone_office")
    NAME_VERIF_MSG = (
        By.CSS_SELECTOR,
        '*[field="name"] .required.validation-message',
    )
    ACCOUNT_CONTENT = (By.CSS_SELECTOR, '#pagecontent[data-module="Accounts"]')
    ACCOUNT_NAME = (By.ID, "name")
    ACCOUNT_PHONE = (By.CSS_SELECTOR, 'div[field="phone_office"]>a')


class AccountPage(BasePage):

    def click_accounts_in_nav_bar(self):
        self.hover_element(AccountPageLocators.MARKETING_NAV_BAR)
        self.click_element(AccountPageLocators.ACCOUNTS_MENU_OPTION)
        self.wait_element(AccountPageLocators.MODULE_TITLE)

    def click_create_account(self):
        self.click_element(AccountPageLocators.CREATE_ACCOUNT)
        self.wait_element(AccountPageLocators.EDIT_VIEW)

    def fill_name(self, last_name):
        self.find_element(AccountPageLocators.NAME_INPUT).send_keys(last_name)

    def fill_phone_number(self, phone):
        self.find_element(AccountPageLocators.PHONE_NUMBER_INPUT).send_keys(phone)

    def click_save_account(self):
        self.click_element(AccountPageLocators.SAVE_BTN)

    def save_account(self):
        self.click_save_account()
        self.wait_element(AccountPageLocators.ACCOUNT_CONTENT)

    def create_account(self, account_info):
        self.click_accounts_in_nav_bar()
        self.click_create_account()
        self.fill_name(account_info["name"])
        self.fill_phone_number(account_info["phone_number"])
        self.save_account()
