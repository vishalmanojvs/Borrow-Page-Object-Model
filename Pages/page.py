# pages/login_page.py
from selenium.webdriver.common.by import By
from Base.base import BasePage


class LoginPage(BasePage):
    PHONE_INPUT = (By.XPATH, '//*[@id="ion-input-0"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="sign-in"]')
    OTP_INPUT = (By.XPATH, '//*[@id="otp-input"]')
    VERIFY_BUTTON = (By.XPATH, '//*[@id="ion-overlay-2"]/app-confirm-otp/div/ion-button[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_phone_number(self, phone_number):
        self.send_keys(self.PHONE_INPUT, phone_number)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def enter_otp(self, otp):
        self.send_keys(self.OTP_INPUT, otp)

    def click_verify(self):
        self.click(self.VERIFY_BUTTON)
