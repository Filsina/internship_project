from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when('Click setting butn')
def click_setting(context):
    context.app.main_page.click_setting()


@when('Click on market butn')
def click_market_butn(context):
    context.app.main_page.click_market_butn()
