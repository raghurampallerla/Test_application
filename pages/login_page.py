import logging
from locators.login_locators import LoginLocators
from config.appium_config import CREDENTIALS  # Import credentials from config


# Configure logging for LoginPage
logger = logging.getLogger("LoginPage")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = LoginLocators.USERNAME_FIELD
        self.password_field = LoginLocators.PASSWORD_FIELD
        self.login_button = LoginLocators.LOGIN_BUTTON
        self.error_message = LoginLocators.ERROR_MESSAGE
        self.error_button = LoginLocators.ERROR_BUTTON
        logger.info(f"LoginPage initialized with driver: {self.driver}")

    def enter_username(self, username):
        logger.info(f"Entering username: {username}")
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        logger.info("Entering password.")
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        logger.info("Clicking the login button.")
        self.driver.find_element(*self.login_button).click()

    def is_error_message_displayed(self):
        try:
            logger.info("Checking if error message is displayed.")
            self.driver.find_element(*self.error_message)
            logger.info("Error message is displayed.")
            return True  # Returns True if the element is visible
        except Exception as e:
            logger.error(f"Error message not displayed: {e}")
            return False

    def click_error_popup_button(self):
        logger.info("Clicking the error popup button.")
        self.driver.find_element(*self.error_button).click()

    def validate_login_page(self):
        try:
            logger.info("Validating if login page is displayed.")
            element = self.driver.find_element(*self.login_button)
            return element.is_displayed()  # Returns True if the element is visible
        except Exception as e:
            logger.error(f"Login page validation failed: {e}")
            return False

    def login(self, username=None, password=None):
        if username is None:
            username = CREDENTIALS["username"]
        if password is None:
            password = CREDENTIALS["password"]

        logger.info("Performing login with username and password.")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
