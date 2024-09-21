import os
import time


class Utils:
    @staticmethod
    def take_screenshot(driver, file_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_dir = "screenshots/"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        driver.save_screenshot(f"{screenshot_dir}/{file_name}_{timestamp}.png")
