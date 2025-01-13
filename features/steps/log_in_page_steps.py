from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL_INPUT = (By.ID, 'email-2')
PASSWORD_INPUT = (By.ID, 'field')


@given('Open Reelly main page')
def open_reelly(context):
    context.app.main_page.open_main()
    sleep(2)


@when('Enter email {valid_email}')
def enter_email(context, valid_email):
    context.wait.until(EC.element_to_be_clickable(EMAIL_INPUT))
    context.app.log_in.enter_email(valid_email)


@when('Enter password {password}')
def enter_pass(context, password):
    context.wait.until(EC.element_to_be_clickable(PASSWORD_INPUT))
    context.app.log_in.enter_pass(password)