import sys

from selenium.webdriver.common.by import By

from Resources.locators import InstaLocators

sys.path.append(sys.path[0] + "/....")


class InstaLogin(object):
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.NAME, InstaLocators.username_field)
        self.password_field = driver.find_element(By.NAME, InstaLocators.password_field)
        self.connect_btn = driver.find_element(By.XPATH, InstaLocators.connect_btn)

        self.cookies_accept_btn = driver.find_element(By.XPATH, InstaLocators.cookies_accept_btn)
        self.cookies_reject_btn = driver.find_element(By.XPATH, InstaLocators.cookies_reject_btn)

        # self.login_error = driver.find_element(By.XPATH, InstaLocators.login_error_text)

    def get_username_field(self):
        return self.username_field

    def get_password_field(self):
        return self.password_field

    def get_connect_btn(self):
        return self.connect_btn

    def get_cookies_accept_btn(self):
        return self.cookies_accept_btn

    def get_cookies_reject_btn(self):
        return self.cookies_reject_btn

    def get_login_error(self):
        return self.login_error
