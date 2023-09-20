from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QCheckBox, QSlider, QTextEdit

from testcases.test_login import login

# Déclaration des variables globales
headless = False
cpu = 5


def run():
    login(core)


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
        self.boutonRun.clicked.connect(run)

        # Affichage de la fenêtre
        self.show()

    def updateLabelCPU(self):
        self.nbrCPU.setText(str(self.sliderCPU.value()))

    def print_message(self, message):
        now = QDateTime.currentDateTime()
        self.console.append(f"{now.toString('hh:mm:ss')} $ {message}")
