from appium import webdriver
from appium.options.common import AppiumOptions

CREDENTIALS = {
    "username": "emma@tfl.gov.uk",
    "password": "password123"
}

def get_appium_driver():
    desired_caps_hinge = {
        "platformName": "Android",
        "udid": "RZ8N30GKF5F",
        "appPackage": "com.example.signinapp",
        "appActivity": "com.example.signinapp.MainActivity",
        "noReset": False,
        "newCommandTimeout": 300,
        "uiautomator2ServerLaunchTimeout": 60000
    }

    option = AppiumOptions().load_capabilities(desired_caps_hinge)
    driver = webdriver.Remote(f"http://localhost:4723/wd/hub", options=option)
    driver.implicitly_wait(5)
    print(f"Appium Driver initialized on Device::::::::: ", driver)
    return driver
