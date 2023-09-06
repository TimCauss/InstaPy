from BasePage import BasePage
from Resources.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.instagram.com/accounts/login/')

    def denied_cookies(self, ):
        self.click(LoginPageLocators.cookies_reject_btn)
