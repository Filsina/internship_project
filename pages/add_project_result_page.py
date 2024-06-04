from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddProjectResultPage(BasePage):
    APPLICATION_BUTTN = (By.XPATH, "//input[@type='submit' and @value='Send an application']")

    def applictn_send_buttn(self):
        self.driver.find_element(*self.APPLICATION_BUTTN).click()


