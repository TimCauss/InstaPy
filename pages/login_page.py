from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException

from selenium.webdriver.support.wait import WebDriverWait
from Resources.fake_reaction import fake_time_wait


class LoginPage:

    def __init__(self, driver, proc):
        self.correct_password = False
        self.driver = driver
        self.proc = proc

        # Login locators:
        self.username_textbox = (By.NAME, 'username')
        self.password_textbox = (By.NAME, 'password')
        self.login_btn = (By.XPATH, "//*[@id='loginForm']/div/div[3]/button")

        # Error msg locators:
        self.login_error_msg = (By.CLASS_NAME, "_ab2z")


        # Account page locators:
        self.foryou_btn = (By.CLASS_NAME, "_ab1a")

        # Cookies locators:
        self.cookie_accept_btn = (By.CSS_SELECTOR, ".\\_a9_0")
        self.cookie_reject_btn = (By.CSS_SELECTOR, ".\\_a9_1")

    def open_page(self, url):
        self.driver.get(url)
        # self.driver.save_screenshot('open_page.png')
        fake_time_wait(self.proc)

    def is_cookies_here(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.cookie_accept_btn))
            print(f'Process n°{self.proc} - Cookies page detected, rejecting...')
            # self.driver.save_screenshot('cookies_detected.png')
            fake_time_wait(self.proc)
            self.driver.find_element(*self.cookie_reject_btn).click()
            WebDriverWait(self.driver, 3).until_not(EC.visibility_of_element_located(self.cookie_accept_btn))
            print(f'Process n°{self.proc} - Cookies page disappeared, continue')
            # self.driver.save_screenshot('cookies_disappeared.png')
        except TimeoutException:
            print(f'Process n°{self.proc} - Cookies page not detected. Continue')
            # self.driver.save_screenshot('cookies_not_detect.png')

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def login_action(self, password):
        # self.driver.execute_script("document.querySelector('[name='password']'")
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.password_textbox).send_keys(Keys.ENTER)
        print(f'Process n°{self.proc} - Trying password {password}')

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def take_screen(self, name):
        self.driver.save_screenshot(f'{name}.png')

    # TODO:
    #   Fonction de detection du message d'erreur de login
    def is_password_works(self):
        try:
            self.driver.find_element(*self.login_error_msg).is_displayed()
        except NoSuchElementException:
            print(f'Process n°{self.proc} - Right password')
            self.correct_password = True
        else:
            print(f'Process n°{self.proc} - Wrong password')
            self.correct_password = False

        # if self.driver.find_element(*self.foryou_btn).is_displayed():
        #     print(f'Congratulations! You have successfully logged in!')


    # TODO:
    #  Create method to adding cookies to driver session
    #  Using cookie_login method or class
    # def adding_cookies(self):
