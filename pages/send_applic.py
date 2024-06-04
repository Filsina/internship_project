from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class SendApplic(BasePage):
    EMAIL_BUTT = (By.ID, 'Email-add-project')
    PHONE_BUTT = (By.ID, 'Phone')

    def input_email(self, data):
        self.input_text(data, *self.EMAIL_BUTT)

    def input_number(self, number):
        self.input_text(number, *self.PHONE_BUTT)
        sleep(4)
