from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    ### BROWSERSTACK ###
    #bs_user = 'filsinaginatylli_XOWozV'
    #bs_key = 'Y1PtychCMbKC1ezmShFN'
    #url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
            # 'browserName': 'Safari',
             #'osVersion': 'Ventura',
             #'os': 'OS X',
             #'sessionName': scenario_name
        # }

    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
