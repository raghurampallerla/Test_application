import os
import logging
import pytest
from appium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.appium_config import get_appium_driver, CREDENTIALS
from appium.options.common import AppiumOptions

# Configure logging
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a logger
logger = logging.getLogger("TestLogin")
logger.setLevel(logging.DEBUG)
log_file = os.path.join(log_dir, "test_login.log")

# Create a file handler for logging
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a console handler for logging (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class TestLogin:

    @pytest.fixture(scope="class")
    def setup(self):
        logger.info("Initializing Appium driver...")
        self.driver = get_appium_driver()
        logger.info(f"Appium driver initialized: {self.driver}")
        yield self.driver
        self.driver.quit()
        logger.info("Appium driver quit.")

    def test_failed_login(self, setup):
        logger.info("Starting test for failed login...")
        login_page = LoginPage(setup)
        login_page.login("wrongemail@tfl.gov.uk", "wrongpassword")
        logger.info("Login attempt with invalid credentials made.")

        if login_page.is_error_message_displayed():
            logger.info("Error message displayed successfully.")
        else:
            logger.error("Error message not displayed.")

        login_page.click_error_popup_button()
        logger.info("Error popup button clicked.")

    def test_successful_login(self, setup):
        logger.info("Starting test for successful login...")
        login_page = LoginPage(setup)
        login_page.login()
        logger.info("Login attempt with valid credentials made.")

        home_page = HomePage(setup)

        # Assert and log user name
        expected_name = "Emma Smith"
        actual_name = home_page.get_name()
        assert actual_name == expected_name, f"Name does not match. Expected {expected_name}, got {actual_name}"
        logger.info(f"User name is {actual_name}, as expected.")

        # Assert and log role
        expected_role = "Senior Test Analyst"
        actual_role = home_page.get_role()
        assert actual_role == expected_role, f"Role does not match. Expected {expected_role}, got {actual_role}"
        logger.info(f"Role is {actual_role}, as expected.")

        # Assert and log office
        expected_office = "Pier Walk"
        actual_office = home_page.get_office()
        assert actual_office == expected_office, f"Office does not match. Expected {expected_office}, got {actual_office}"
        logger.info(f"Office is {actual_office}, as expected.")

    def test_logout(self, setup):
        logger.info("Starting test for logout functionality...")
        login_page = LoginPage(setup)
        login_page.login()
        logger.info("Login successful, navigating to home page.")

        home_page = HomePage(setup)
        home_page.logout()
        logger.info("Logged out from the home page.")

        if login_page.validate_login_page():
            logger.info("Login screen is displayed after logout.")
        else:
            logger.error("Login screen is not displayed after logout.")
