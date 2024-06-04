from pages.main_page import MainPage
from pages.log_in import LogIn
from pages.add_project_result_page import AddProjectResultPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.send_applic import SendApplic


class Application:
    def __init__(self,driver):
        self.main_page = MainPage(driver)
        self.log_in = LogIn(driver)
        self.add_project_result_page = AddProjectResultPage(driver)
        self.send_applic = SendApplic(driver)



