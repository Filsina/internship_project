from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


EMAIL_INPUT = (By.ID, 'email-2')
PASSWORD_INPUT = (By.ID, 'field')
CONTINUE_BUTTN = (By.XPATH, "//*[contains(@class, 'login-button w-button')]")
SETTING_BUTTN = (By.CSS_SELECTOR,"a[href*='/settings']")
ADD_PROJECT_BUTTN = (By.CSS_SELECTOR, "a[href*='/add-a-project']")
EMAIL_BUTT = (By.ID, 'Email-add-project')
PHONE_BUTT = (By.ID,'Phone')


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


@when('Click setting butn')
def click_setting(context):
    context.driver.find_element(*SETTING_BUTTN).click()
    sleep(4)


@when('Click add project butn')
def click_add_project(context):
    context.driver.find_element(*ADD_PROJECT_BUTTN).click()
    sleep(2)


@when('Email input {data}')
def input_email(context, data):
    context.wait.until(EC.element_to_be_clickable(EMAIL_BUTT))
    context.app.send_applic.input_email(data)


@when('Enter phone{number}')
def input_number(context, number):
    context.app.send_applic.input_number(number)
    sleep(4)









