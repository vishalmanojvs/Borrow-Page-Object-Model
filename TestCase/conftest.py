import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": (
            "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
        )
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)

    request.cls.driver = driver  # Attach driver to the test class

    yield driver
    driver.quit()
