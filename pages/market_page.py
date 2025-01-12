from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MarketPage(BasePage):
    HEADER = (By.XPATH, "//div[text()='Market' and @class='page-title agency']")
    DEV_FILTER_BUTTN = (By.XPATH, "//*[@wized='marketTagDevelopers']")

    def market_page_displayed(self):
        self.wait_until_visible(*self.HEADER)
        self.verify_text('Market', *self.HEADER)

    def click_developers_filter(self):
        self.wait_until_clickable_click(*self.DEV_FILTER_BUTTN)
