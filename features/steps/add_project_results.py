from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from sample_script import driver

APPLICATION_BUTTN = (By.XPATH,"//input[@type='submit' and @value='Send an application']")


@then('Verify add-a-project page opens')
def verify_add_project_url(context):
    assert 'https://soft.reelly.io/add-a-project' in context.driver.current_url
    print('Correct page opens')


@then('Verify application buttn is available and clickable')
def applictn_send_buttn(context):
    context.wait.until(EC.element_to_be_clickable(APPLICATION_BUTTN))
    context.app.add_project_result_page.applictn_send_buttn()




