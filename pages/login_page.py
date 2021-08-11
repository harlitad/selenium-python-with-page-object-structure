from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # locators
    EMAIL = (By.ID, "ui-sign-in-email-input")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Next')]")
    PASSWORD = (By.ID, "ui-sign-in-password-input")
    BUTTON_SIGNIN = (By.CSS_SELECTOR, ".firebaseui-id-submit")

    def set_email(self, email):
        field_email = self.driver.find_element(*self.EMAIL)
        field_email.send_keys(email)

    def click_button_next(self):
        button_next = self.driver.find_element(*self.BUTTON_NEXT)
        button_next.click()

    def set_password(self, password):
        wait = WebDriverWait(self.driver, 3000, 1)
        passw = wait.until(EC.visibility_of_element_located(self.PASSWORD))
        passw.send_keys(password)

    def click_button_signin(self):
        button_signin = self.driver.find_element(*self.BUTTON_SIGNIN)
        button_signin.click()
