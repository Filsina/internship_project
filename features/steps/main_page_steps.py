from behave import given, when, then


@when('Click setting butn')
def click_setting(context):
    context.app.main_page.click_setting()


@when('Click on market butn')
def click_market_butn(context):
    context.app.main_page.click_market_butn()


@when('Click on off-plan butn at the left side menu')
def click_off_plan_butn_at_left_side(context):
    context.app.main_page.click_off_plan_butn_at_left_side()
