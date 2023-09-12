from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = driver.find_element(By.NAME, 'username')
        self.password_textbox = driver.find_element(By.NAME, 'password')
        self.login_btn = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")

        self.cookie_accept_btn = driver.find_element(By.XPATH, "//*[text()='Autoriser tous les cookies'")
        self.cookie_reject_btn = driver.find_element(By.XPATH, "//*[text()='Refuser les cookies optionnels']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_textbox).send_keys(password)

    def login_action(self, username, password):
        self.driver.find_element(self.username_textbox).send_keys(username)
        self.driver.find_element(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(self.login_btn).click()

    def click_cookies(self, action):
        if action == 'reject':
            self.driver.find_element(self.cookie_reject_btn).click()
        if action == 'accept':
            self.driver.find_element(self.cookie_accept_btn).click()
