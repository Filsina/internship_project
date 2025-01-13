from behave import given, when, then


@when('Click verification butn')
def click_verification_butn(context):
    context.app.settings_page.click_verification_butn()

