from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LeadPageLocators:
    MARKETING_NAV_BAR = (By.ID, "grouptab_1")
    LEADS_MENU_OPTION = (
        By.XPATH,
        '//*[@id="grouptab_1"]/..//*[@id="moduleTab_2_Leads"]',
    )

    MODULE_TITLE = (By.CSS_SELECTOR, ".moduleTitle .module-title-text")

    CREATE_LEAD = (By.XPATH, '//*[@class="actionmenulink" and text()="Create Lead"]')

    EDIT_VIEW = (By.ID, "EditView")
    SAVE_BTN = (By.ID, "SAVE")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    PHONE_NUMBER_INPUT = (By.ID, "phone_mobile")
    LASTNAME_VERIF_MSG = (
        By.CSS_SELECTOR,
        '*[field="last_name"] .required.validation-message',
    )
    LEAD_CONTENT = (By.CSS_SELECTOR, '#pagecontent[data-module="Leads"]')
    LEAD_NAME = (By.ID, "full_name")
    LEAD_PHONE = (By.CSS_SELECTOR, 'div[field="phone_mobile"]>a')


class LeadPage(BasePage):

    def click_leads_in_nav_bar(self):
        self.hover_element(LeadPageLocators.MARKETING_NAV_BAR)
        self.click_element(LeadPageLocators.LEADS_MENU_OPTION)
        self.wait_element_text(LeadPageLocators.MODULE_TITLE)

    def click_create_lead(self):
        self.click_element(LeadPageLocators.CREATE_LEAD)
        self.wait_element(LeadPageLocators.EDIT_VIEW)
        self.wait_element_text(LeadPageLocators.MODULE_TITLE)

    def fill_last_name(self, last_name):
        self.find_element(LeadPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    def fill_first_name(self, first_name):
        self.find_element(LeadPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    def fill_phone_number(self, phone):
        self.find_element(LeadPageLocators.PHONE_NUMBER_INPUT).send_keys(phone)

    def click_save_lead(self):
        self.wait_element_clickable(LeadPageLocators.SAVE_BTN)
        self.click_element(LeadPageLocators.SAVE_BTN)

    def save_lead(self):
        self.click_save_lead()
        self.wait_element(LeadPageLocators.LEAD_CONTENT)

    def create_lead(self, lead_info):
        self.click_leads_in_nav_bar()
        self.click_create_lead()
        self.fill_last_name(lead_info["last_name"])
        self.fill_first_name(lead_info["first_name"])
        self.fill_phone_number(lead_info["phone_number"])
        self.save_lead()
