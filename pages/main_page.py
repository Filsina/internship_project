from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    MARKET_BUTN = (By.CSS_SELECTOR, "a[href='/market-companies']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_market_butn(self):
        self.wait_until_clickable_click(*self.MARKET_BUTN)
