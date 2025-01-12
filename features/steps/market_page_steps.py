from behave import given, when, then
from time import sleep


@when('Click on market butn')
def click_market_butn(context):
    context.app.main_page.click_market_butn()


@then('Verify market page displayed')
def market_page_displayed(context):
    context.app.market_page.market_page_displayed()


@when('Click on Developers filter')
def click_developers_filter(context):
    context.app.market_page.click_developers_filter()
    sleep(4)

