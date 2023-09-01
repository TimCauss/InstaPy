from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import datetime
import os
import logging

ct = datetime.datetime.now()

logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.DEBUG)




def main_task():

    #Variable de fonctionnement
    driver = webdriver.Chrome()
    timeout_time = 0.5
    connexion_url = 'https://www.instagram.com/accounts/login/'

    #configuration du driver
    driver.implicitly_wait(timeout_time)

    try :
        logging.info(f'{ct}: Navigate to {connexion_url}...')
        driver.get(connexion_url)
    except TimeoutException as ex:
        logging.error(f'')


def connexion_loop():

