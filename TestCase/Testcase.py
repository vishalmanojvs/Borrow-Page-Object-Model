import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Configfiles.config import TestData
from Pages.page import LoginPage
from Utilies.Logging import LogGen
from Utilies.utilies import Utils
from TestCase.conftest import setup
logger = LogGen.loggen()


@pytest.mark.usefixtures("setup")
class TestLogin:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def test_valid_login(self):
        logger.info("Starting test_valid_login")
        self.driver.get(TestData.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.enter_phone_number(TestData.PHONE_NUMBER)
        login_page.click_sign_in()

        # Example for OTP
        otp = "123456"  # Replace with actual OTP fetching logic
        login_page.enter_otp(otp)
        login_page.click_verify()

        assert login_page.is_visible(LoginPage.VERIFY_BUTTON), "Login failed"
        Utils.take_screenshot(self.driver, "login_success")
