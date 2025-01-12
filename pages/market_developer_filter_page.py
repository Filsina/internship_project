from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DeveloperPage(BasePage):
    SECOND_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")
    THIRD_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")
    FORTH_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")
    FIFTH_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")
    SIXTH_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")
    SEVENTH_PAGE = (By.XPATH, "//*[@wized='nextPageMarket']")

    def click_2_page(self):
        self.wait_until_clickable_click(*self.SECOND_PAGE)

    def click_3_page(self):
        self.wait_until_clickable_click(*self.THIRD_PAGE)

    def click_4_page(self):
        self.wait_until_clickable_click(*self.FORTH_PAGE)

    def click_5_page(self):
        self.wait_until_clickable_click(*self.FIFTH_PAGE)

    def click_6_page(self):
        self.wait_until_clickable_click(*self.SIXTH_PAGE)

    def click_7_page(self):
        self.wait_until_clickable_click(*self.SEVENTH_PAGE)
