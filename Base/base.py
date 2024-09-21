from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return bool(self.wait.until(EC.visibility_of_element_located(by_locator)))
