from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element not clickable by{locator}').click()

    def wait_until_visible(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
                            message=f'Element not clickable by{locator}')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Error!{expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_url):
        self.wait.until(EC.url_contains(expected_url), message=f"No {expected_url} in URL")
