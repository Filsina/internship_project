from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    MARKET_BUTN = (By.CSS_SELECTOR, "a[href='/market-companies']")
    SETTINGS_BUTTN = (By.CSS_SELECTOR, "a[href*='/settings']")
    LEFT_SIDE_MENU_OFF_PLAN = (By.XPATH, "//*[text()='Off-plan']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_market_butn(self):
        self.wait_until_clickable_click(*self.MARKET_BUTN)

    def click_setting(self):
        self.wait_until_clickable_click(*self.SETTINGS_BUTTN)

    def click_off_plan_butn_at_left_side(self):
        self.wait_until_clickable_click(*self.LEFT_SIDE_MENU_OFF_PLAN)
