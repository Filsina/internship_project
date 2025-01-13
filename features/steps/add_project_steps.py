from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ADD_PROJECT_BUTTN = (By.CSS_SELECTOR, "a[href*='/add-a-project']")
EMAIL_BUTT = (By.ID, 'Email-add-project')
PHONE_BUTT = (By.ID, 'Phone')
NAME_BUTTN = (By.ID, 'Your-name')
COUNTRY_BUTTN = (By.ID, 'Country')
ROLE_BUTTN = (By.ID, 'Role')


@when('Click add project butn')
def click_add_project(context):
    context.app.adding_project.click_add_project()
    #sleep(10)


@when('Email input {data}')
def input_email(context, data):
    context.wait.until(EC.element_to_be_clickable(EMAIL_BUTT))
    context.app.send_applic.input_email(data)
    #sleep(5)


@when('Enter phone{number}')
def input_number(context, number):
    context.wait.until(EC.element_to_be_clickable(PHONE_BUTT))
    context.app.send_applic.input_number(number)
    #sleep(5)


@when('Enter name{name}')
def input_name(context, name):
    context.wait.until(EC.element_to_be_clickable(NAME_BUTTN))
    context.app.send_applic.input_name(name)
    #sleep(5)


@when('Enter country{country}')
def input_country(context, country):
    context.wait.until(EC.element_to_be_clickable(COUNTRY_BUTTN))
    context.app.send_applic.input_country(country)
    #sleep(5)


@when('Enter role{role}')
def input_role(context, role):
    context.wait.until(EC.element_to_be_clickable(ROLE_BUTTN))
    context.app.send_applic.input_role(role)
    #sleep(5)
