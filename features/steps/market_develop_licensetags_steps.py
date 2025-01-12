from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

LICENSE_TAGS_1 = (By.CSS_SELECTOR, "div.license-block")
LICENSE_TAGS_2 = (By.CSS_SELECTOR, "div.license-block")
LICENSE_TAGS_3 = (By.CSS_SELECTOR, "div.license-block")
LICENSE_TAGS_4 = (By.CSS_SELECTOR, "div.license-block")
LICENSE_TAGS_5 = (By.CSS_SELECTOR, "div.license-block")
LICENSE_TAGS_6 = (By.CSS_SELECTOR, 'div.license-block')
LICENSE_TAGS_7 = (By.CSS_SELECTOR, 'div.license-block')


@then('Verify {expected_amount} License tags are shown page1')
def verify_license_tags1(context, expected_amount):
    context.driver.execute_script("window.scrollBy(0, 4000);")
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_1))
    context.app.market_developerfilter_licensetags_page.verify_license_tags1(expected_amount)


@then('Verify {expected_amount} license tags are shown page2')
def verify_license_tags2(context, expected_amount):
    context.driver.execute_script("window.scrollBy(0, 4000);")
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_2))
    context.app.market_developerfilter_licensetags_page.verify_license_tags2(expected_amount)


@then('Verify {expected_amount} license tags are shown page3')
def verify_license_tags3(context, expected_amount):
    context.driver.execute_script("window.scrollBy(0, 4000);")
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_3))
    context.app.market_developerfilter_licensetags_page.verify_license_tags3(expected_amount)


@then('Verify {expected_amount} license tags are shown page4')
def verify_license_tags4(context, expected_amount):
    sleep(3)
    context.app.market_developerfilter_licensetags_page.verify_license_tags4(expected_amount)


@then('Verify {expected_amount} license tags are shown page5')
def verify_license_tags5(context, expected_amount):
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_4))
    context.app.market_developerfilter_licensetags_page.verify_license_tags5(expected_amount)


@then('Verify {expected_amount} license tags are shown page6')
def verify_license_tags6(context, expected_amount):
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_4))
    context.app.market_developerfilter_licensetags_page.verify_license_tags6(expected_amount)


@then('Verify {expected_amount} license tags are shown page7')
def verify_license_tags7(context, expected_amount):
    context.wait.until(EC.visibility_of_element_located(LICENSE_TAGS_7))
    context.app.market_developerfilter_licensetags_page.verify_license_tags7(expected_amount)
