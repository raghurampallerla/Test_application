import logging
from locators.home_locators import HomeLocators


# Configure logging for HomePage
logger = logging.getLogger("HomePage")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_label = HomeLocators.NAME_LABEL
        self.role_label = HomeLocators.ROLE_LABEL
        self.office_label = HomeLocators.OFFICE_LABEL
        self.logout_button = HomeLocators.LOGOUT_BUTTON
        self.logout_button_popup = HomeLocators.LOGOUT_BUTTON_POP_UP
        logger.info(f"HomePage initialized with driver: {self.driver}")

    def get_name(self):
        try:
            logger.info("Getting user name.")
            name = self.driver.find_element(*self.name_label).text
            logger.info(f"User name is: {name}")
            return name
        except Exception as e:
            logger.error(f"Error getting name: {e}")
            return None

    def get_role(self):
        try:
            logger.info("Getting user role.")
            role = self.driver.find_element(*self.role_label).text
            logger.info(f"User role is: {role}")
            return role
        except Exception as e:
            logger.error(f"Error getting role: {e}")
            return None

    def get_office(self):
        try:
            logger.info("Getting user office.")
            office = self.driver.find_element(*self.office_label).text
            logger.info(f"User office is: {office}")
            return office
        except Exception as e:
            logger.error(f"Error getting office: {e}")
            return None

    def logout(self):
        try:
            logger.info("Logging out of the application.")
            self.driver.find_element(*self.logout_button).click()
            logger.info("Logout button clicked.")
            self.driver.find_element(*self.logout_button_popup).click()
            logger.info("Logout confirmed from popup.")
        except Exception as e:
            logger.error(f"Error during logout: {e}")
