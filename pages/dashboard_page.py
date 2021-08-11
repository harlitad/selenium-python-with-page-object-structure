from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    # locators
    TOAST_SUCCESS_LOGIN = (By.CSS_SELECTOR, ".Vue-Toastification__toast-body")

    @property
    def get_toast_success_login(self):
        toast_success_login = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.TOAST_SUCCESS_LOGIN))
        return toast_success_login.text