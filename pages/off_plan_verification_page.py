from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OffPlanVerificationPage(BasePage):
    PRODUCT_CARDS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    SALES_STATUS_TAG = (By.CSS_SELECTOR, "[wized='projectStatus']")

    def verify_sales_status_tag(self):

        self.driver.execute_script("window.scrollBy(0, 4000);")

        self.wait.until(EC.presence_of_element_located(self.PRODUCT_CARDS))
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CARDS))

        products = self.driver.find_elements(*self.PRODUCT_CARDS)

        if not products:
            raise AssertionError("No product cards found on the page.")

        for index, product in enumerate(products):
            try:

                sale_status_element = WebDriverWait(product, 5).until(
                    EC.visibility_of_element_located(self.SALES_STATUS_TAG)
                )
                sale_status = sale_status_element.text.strip()  # Remove extra spaces

                print(f"✅ Product {index + 1} - Sales Status: {sale_status}")
                assert sale_status, f"❌ Product {index + 1} - Sales status not found."

            except Exception as e:
                print(f"❌ Error verifying sales status for product {index + 1}: {e}")
                raise
