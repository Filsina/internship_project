from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MarketDevelopersPage(BasePage):
    LICENSE_TAGS_1 = (By.CSS_SELECTOR, "div.license-block")
    LICENSE_TAGS_2 = (By.CSS_SELECTOR, "div.license-block")
    LICENSE_TAGS_3 = (By.CSS_SELECTOR, "div.license-block")
    LICENSE_TAGS_4 = (By.CSS_SELECTOR, "div.license-block")
    LICENSE_TAGS_5 = (By.CSS_SELECTOR, "div.license-block")
    LICENSE_TAGS_6 = (By.CSS_SELECTOR, 'div.license-block')
    LICENSE_TAGS_7 = (By.CSS_SELECTOR, 'div.license-block')

    def verify_license_tags1(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.driver.find_elements(*self.LICENSE_TAGS_1)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags2(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_2)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags3(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_3)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags4(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_4)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags5(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_5)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags6(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_6)
        assert len(links) == 16, f"Expected 16,but got {len(links)}"

    def verify_license_tags7(self,expected_amount):
        links = self.driver.find_elements(*self.LICENSE_TAGS_7)
        assert len(links) == 7, f"Expected 7,but got {len(links)}"
