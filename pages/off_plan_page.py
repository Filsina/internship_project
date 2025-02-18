from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OffPlanPage(BasePage):
    OFFPLAN_PAGE_PRODUCT = (By.XPATH, "//*[text()='Wellington Ocean']")

    def click_off_plan_product(self):
        self.wait_until_clickable_click(*self.OFFPLAN_PAGE_PRODUCT)
