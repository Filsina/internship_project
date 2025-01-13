from behave import given, when, then


@then('Verify URL contains {word}')
def verify_partial_url(context, word):
    context.app.add_project_result_page.verify_partial_url(word)


@then('Verify Upload image butn is present')
def verify_upload_image_butn_present(context):
    context.app.verification_page.verify_upload_image_butn_present()


@then('Verify Next step butn is present')
def verify_next_page_butn(context):
    context.app.verification_page.verify_next_page_butn()
