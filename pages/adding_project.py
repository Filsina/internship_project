from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class AddingProject(BasePage):
    SETTING_BUTTN = (By.CSS_SELECTOR, "a[href*='/settings']")
    ADD_PROJECT_BUTTN = (By.CSS_SELECTOR, "a[href*='/add-a-project']")

    def click_setting(self):
        self.wait_until_clickable_click(*self.SETTING_BUTTN)
        #sleep(15)

    def click_add_project(self):
        self.wait_until_clickable_click(*self.ADD_PROJECT_BUTTN)
        #sleep(15)







