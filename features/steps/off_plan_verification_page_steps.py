from behave import given, when, then


@then('Verify each product contains the Sales status')
def verify_sales_status_tag(context):
    context.app.off_plan_verification_page.verify_sales_status_tag()
