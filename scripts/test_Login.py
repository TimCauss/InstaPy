import sys
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Resources.WebDriverSetup import WebDriverSetup
from pages.LoginPage import InstaLogin
from Resources.locators import InstaLocators

sys.path.append(sys.path[0] + "/...")

username = 'Tim0ut_13'
password = 'ifth#512h'


class test_Login(WebDriverSetup):
    def test_Login(self):
        driver = self.driver
        driver.set_page_load_timeout(10)

        driver.get('https://www.instagram.com/accounts/login/')
        sleep(0.5)

        # Create an instance of the class so that we can make use of the methods
        insta_login_page = InstaLogin(driver)

        # Wait for cookies btn
        try:
            print(f'\nRejecting Cookies')
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, InstaLocators.cookies_reject_btn)))
            print(f'bouton cookies activé')
            insta_login_page.cookies_reject_btn.click()
            WebDriverWait(driver, 5).until_not(
                EC.visibility_of_element_located((By.XPATH, InstaLocators.cookies_reject_btn)))
        except Exception as ex:
            print(f'Error in cookies management')
            print(f'{ex}')

        # filling username field
        try:
            print(f'Connecting to {username}')
            insta_login_page.username_field.send_keys(username)
        except Exception as ex:
            print(f'Error while filling the username input')

        # filling password field
        try:
            print(f'Trying password : {password}')
            insta_login_page.username_field.send_keys(password)
        except Exception as ex:
            print(f'Error while filling the password input')


test_Login()
