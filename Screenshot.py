from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def take_screenshot(self, file_name: str):
        """
        Takes a screenshot of the current page.

        :param file_name: The name of the file to save the screenshot as.
        """
        self.driver.save_screenshot(file_name)
