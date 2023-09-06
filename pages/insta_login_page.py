import logging

from selenium.common import NoSuchElementException

from BasePage import BasePage
from Resources.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.instagram.com/accounts/login/')

    def reject_cookies(self, ):
        try:
            self.click(LoginPageLocators.cookies_reject_btn)
            logging.info(f'Rejecting cookies.')
            print(f'ERROR - Rejecting cookies button not found')
        except NoSuchElementException as ex:
            logging.error(f'ERROR - Rejecting cookies button not found')
            print(f'ERROR - Rejecting cookies button not found')
            logging.error(f'{ex}')
            self.driver.close()



