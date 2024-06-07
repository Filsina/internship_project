from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class SendApplic(BasePage):
    EMAIL_BUTT = (By.ID, 'Email-add-project')
    PHONE_BUTT = (By.ID, 'Phone')
    NAME_BUTTN = (By.ID, 'Your-name')
    COUNTRY_BUTTN = (By.ID, 'Country')
    ROLE_BUTTN = (By.ID, 'Role')

    def input_email(self, data):
        self.input_text(data, *self.EMAIL_BUTT)

    def input_number(self, number):
        self.input_text(number, *self.PHONE_BUTT)

    def input_name(self, name):
        self.input_text(name, *self.NAME_BUTTN)

    def input_country(self, country):
        self.input_text(country, *self.COUNTRY_BUTTN)

    def input_role(self, role):
        self.input_text(role, *self.ROLE_BUTTN)



