from behave import given, when, then
from time import sleep


@then('Verify market page displayed')
def market_page_displayed(context):
    context.app.market_page.market_page_displayed()


@when('Click on Developer filter')
def click_developer_filter(context):
    context.app.market_page.click_developer_filter()
    sleep(4)
