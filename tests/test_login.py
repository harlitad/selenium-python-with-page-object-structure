from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    EMAIL_VALID = "admin@admin.com"
    PASSWORD_VALID = "admin10"
    EMAIL_NOT_REGISTERED = "admin@admin.admin"
    PASSWORD_INVALID = "adminadmin10"
    EMAIL_INVALID = "halopakabar"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://staging-partner-explore.misterb2b.com/login')

    def teardown_method(self):
        self.driver.close()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        login_page.set_email(self.EMAIL_VALID)
        login_page.click_button_next()
        login_page.set_password(self.PASSWORD_VALID)
        login_page.click_button_signin()
        assert dashboard_page.get_toast_success_login == "Logging in"
