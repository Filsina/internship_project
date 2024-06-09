from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class LogIn(BasePage):
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BUTTN = (By.XPATH, "//*[contains(@class, 'login-button w-button')]")

    def enter_email(self, valid_email):
        self.input_text(valid_email, *self.EMAIL_INPUT)

    def enter_pass(self, password):
        self.input_text(password, *self.PASSWORD_INPUT)
        self.click(*self.CONTINUE_BUTTN)
        #sleep(4)



