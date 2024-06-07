from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element not clickable by{locator}').click()

    def verify_partial_url(self, expected_url):
        self.wait.until(EC.url_contains(expected_url), message=f"No {expected_url} in URL")









