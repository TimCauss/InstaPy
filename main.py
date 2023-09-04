from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import datetime
import os
import logging

ct = datetime.datetime.now()

logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO)

# Variable de fonctionnement
driver = webdriver.Chrome()

connexion_url = 'https://www.instagram.com/accounts/login/'


class SignInPage:

    def __init__(self, connexion_url):


def navigate_to_home():
    # configuration du timeout
    timeout_time = 0.5
    driver.implicitly_wait(timeout_time)

    rt = 0
    while True:
        try:
            rt += 1
            logging.info(f'{ct}: Navigate to {connexion_url}...')
            driver.get(connexion_url)
        except TimeoutException as ex:
            logging.error(f'{ct}: Connexion timeout ({ex})')
            logging.error(f'{ct}: Retrying... ({rt})')
            if rt > 3:
                driver.close()
                break


navigate_to_home()
