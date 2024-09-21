class TestData:
    BASE_URL = "https://borrow-3b1b3.web.app/"
    PHONE_NUMBER = "9986754795"
    CHROME_OPTIONS = {
        "mobile_emulation": {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": (
                "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.77 Mobile Safari/537.36"
            ),
        }
    }
