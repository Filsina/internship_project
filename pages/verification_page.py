from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class VerificationPage(BasePage):
    UPLOAD_IMAGE_BUTN = (By.XPATH, "//div[@class='upload-button-2 w-embed']")
    NEXT_PAGE_BUTN = (By.CSS_SELECTOR, "[class='next-step--']")

    def verify_upload_image_butn_present(self):
        self.wait_until_visible(*self.UPLOAD_IMAGE_BUTN)

    def verify_next_page_butn(self):
        self.wait_until_visible(*self.NEXT_PAGE_BUTN)
