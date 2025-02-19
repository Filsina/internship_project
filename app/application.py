from pages.main_page import MainPage
from pages.log_in import LogIn
from pages.add_project_result_page import AddProjectResultPage
from pages.send_applic import SendApplic
from pages.market_page import MarketPage
from pages.market_developer_filter_page import DeveloperPage
from pages.market_developfilter_licensetags_page import MarketDevelopersPage
from pages.verification_page import VerificationPage
from pages.settings_page import SettingPage
from pages.off_plan_page import OffPlanPage
from pages.off_plan_verification_page import OffPlanVerificationPage



class Application:
    def __init__(self,driver):
        self.main_page = MainPage(driver)
        self.log_in = LogIn(driver)
        self.add_project_result_page = AddProjectResultPage(driver)
        self.send_applic = SendApplic(driver)
        self.market_page = MarketPage(driver)
        self.market_developer_filter_page = DeveloperPage(driver)
        self.market_developerfilter_licensetags_page = MarketDevelopersPage(driver)
        self.verification_page = VerificationPage(driver)
        self.settings_page = SettingPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.off_plan_verification_page = OffPlanVerificationPage(driver)





