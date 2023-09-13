import os
import time

import pytest
import undetected_chromedriver as uc

from pages.login_page import LoginPage
from Resources.pass_to_temp import split_words


# Config var
url = 'https://www.instagram.com/accounts/login/'
proc = 0
input_file = "test.txt"
num_temp = 6
groups = split_words(input_file, num_temp)
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
    print(f'\n{cpu} - Configuration')

    print(f'{cpu} - Connecting to {url}')
    login_page.open_page(url)
    login_page.is_cookies_here()
    login_page.login_action(username, 'ifth#512h')
    time.sleep(5)


def test_groups():
    c = 0
    for group in groups:
        for i in group:
            c += 1
            print(f'\n{c} - {i}')
