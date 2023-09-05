import random

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

import time
import logging

account = 'Tim0ut_13'
file_path = 'test.txt'
connexion_url = 'https://www.instagram.com/accounts/login/'

FORMAT = '%(asctime)s - %(levelname)s:%(message)s'
logging.basicConfig(filename='info.log', filemode='w', encoding='utf-8', level=logging.INFO, format=FORMAT,
                    datefmt="%H:%M:%S")


def fake_time_wait(min=0.2, max=1.1):
    t = random.uniform(min, max)
    time.sleep(t)
    print(f'Time waited: {t}')


def file_to_list(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def read_words(lines):
    words = map(lambda line: line.split(), lines)
    for word in words:
        yield word


def test_login():
    driver = uc.Chrome
    driver.implicitly_wait(0.5)

    bot = Main(driver)
    bot.gotohome()
    bot.login()


class Main(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'username_input': ('NAME', 'username'),
        'password_input': ('NAME', 'password'),
        'connect_btn': ('XPATH', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div['
                                 '1]/div[2]/form/div/div[3]/button/div'),
        'cookie_reject_btn': ('XPATH', "//*[text()='Refuser les cookies optionnels']")
    }

    def gotohome(self):
        self.driver.get(connexion_url)

    def login(self):
        self.username_input.set_text(account)
