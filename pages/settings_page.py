from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SettingPage(BasePage):
    VERIFICATION_BUTN = (By.CSS_SELECTOR, "a[href*='/verification/step-0']")
    ADD_PROJECT_BUTTN = (By.CSS_SELECTOR, "a[href*='/add-a-project']")

    def click_verification_butn(self):
        self.wait_until_clickable_click(*self.VERIFICATION_BUTN)

    def click_add_project(self):
        self.wait_until_clickable_click(*self.ADD_PROJECT_BUTTN)

