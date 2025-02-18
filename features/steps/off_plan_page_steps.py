from behave import given, when, then
from selenium.webdriver.common.by import By

VISUALISATIONS_OPTIONS = (By.XPATH, "//a[@role='tab']")
OPTIONS_TITLE = (By.XPATH, "//*[text()='Architecture']")


@when('Click on off_plan product')
def click_off_plan_product(context):
    context.app.off_plan_page.click_off_plan_product()


@then('Verify option “Architecture”, “Interior”, “lobby” are present and clickable')
def verify_options_are_present(context):
    expected_options = ['Architecture', 'Interior', 'lobby']
    actual_options = []

    visual_options = context.driver.find_elements(*VISUALISATIONS_OPTIONS)
    for option in visual_options:
        option.click()
        selected_option = context.driver.find_element(*OPTIONS_TITLE)
        actual_options.append(selected_option)
        print(actual_options)



