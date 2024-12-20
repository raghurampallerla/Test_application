from appium.webdriver.common.appiumby import *

class HomeLocators:
    NAME_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Emma Smith"]')
    ROLE_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Senior Test Analyst"]')
    OFFICE_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Pier Walk"]')
    LOGOUT_BUTTON = (AppiumBy.XPATH, '//android.widget.Button')
    LOGOUT_BUTTON_POP_UP=(AppiumBy.XPATH, '//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')
