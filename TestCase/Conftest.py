import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse='True')
def setup():
    # Initialize Chrome Options
    chrome_options = Options()
    # Set Mobile Emulation properties
    mobile_emulation = {
        "deviceMetrics": {
            "width": 360,  # Width of the screen
            "height": 640,  # Height of the screen
            "pixelRatio": 3.0  # Pixel ratio
        },
        "userAgent": (
            "Chrome/91.0.4472.77 Mobile Safari/537.36"
        )
    }

    # Apply mobile emulation settings
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Initialize WebDriver with Chrome Options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Set an implicit wait once
    driver.implicitly_wait(10)

    # Navigate to the web page
    driver.get("https://borrow-3b1b3.web.app/")


