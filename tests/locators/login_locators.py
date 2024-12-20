from appium.webdriver.common.appiumby import *

class LoginLocators:
    USERNAME_FIELD = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
    PASSWORD_FIELD = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
    LOGIN_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")
    ERROR_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Looks like either your Username or Password is incorrect. Please try again."]')
    ERROR_BUTTON = (AppiumBy.XPATH,'//android.widget.Button')

