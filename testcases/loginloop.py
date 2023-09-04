import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import datetime
import os
import logging

ct = datetime.datetime.now()

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO, format=FORMAT)

# Variable de fonctionnement
driver = uc.Chrome()

connexion_url = 'https://www.instagram.com/accounts/login/'
account = '0669505991'
file_path = 'test.txt'


def file_to_list(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def read_words(lines):
    words = map(lambda line: line.split(), lines)
    for word in words:
        yield word


def navigate_to_home():
    # configuration du timeout
    timeout_time = 0.5
    driver.implicitly_wait(timeout_time)

    try:
        logging.info(f'Navigate to {connexion_url}...')
        driver.get(connexion_url)
    except TimeoutException as ex:
        logging.error(f'Connexion timeout ({ex})')
        driver.close()


    try:
        cookie_reject_btn = driver.find_element(By.XPATH, "//*[text()='Refuser les cookies optionnels']")
        cookie_reject_btn.click()
    except NoSuchElementException as ex:
        logging.info(f'Cookies message not found ({ex})')

    input('PAUSE')

    try:
        driver.find_element(By.NAME, 'username').send_keys(account)
    except NoSuchElementException as ex:
        logging.error(f'Username input not found ({ex})')
        driver.close()



    input('PAUSE')
    exit()
    logging.info(f'Logging to account : {account}')


navigate_to_home()


for word in read_words(file_to_list(file_path)):
    print(word)
