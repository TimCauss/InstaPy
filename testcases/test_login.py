import os
import time
from datetime import datetime

import pytest
import undetected_chromedriver as uc

from pages.login_page import LoginPage
from Resources.pass_to_temp import split_words
from Resources.pass_to_temp import password_list

# Config var
url = 'https://www.instagram.com/accounts/login/'
proc = 0
input_file = "test.txt"
num_temp = 6
groups = split_words(password_list(input_file), num_temp)
username = 'Tim0ut_13'


#


@pytest.fixture()
def driver():
    driver = uc.Chrome(headless=False, use_subprocess=True)
    driver.implicitly_wait(1.5)
    yield driver
    driver.quit()
    for i in range(num_temp):
        file = f'temp{i + 1}.txt'
        if os.path.isfile(file):
            os.remove(file)


def test_login(driver):
    global proc
    proc += 1


    login_page = LoginPage(driver, proc)
    cpu = f'Process n°{login_page.proc}'

    # Todo:
    #   1. password_list() method who return a list of strings
    #   form a temp file. Charge the list from file HERE

    print(f'\n{cpu} - Starting')
    print(f'\n{cpu} - Configuration')

    print(f'{cpu} - Connecting to {url}')
    login_page.open_page(url)
    login_page.is_cookies_here()


    # passwords = password_list(f'temp{proc}.txt')

    t1 = datetime.now()

    login_page.enter_username(username)
    login_page.login_action('test')
    t = (datetime.now() - t1).seconds
    print(f'Logging Exec Time : {t}')
    login_page.is_password_works()
    time.sleep(5)
