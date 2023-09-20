import sys
from PyQt5.QtWidgets import QApplication
from GUI.gui import Fenetre


def main():
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        fenetre = Fenetre()
        fenetre.show()

        # Exécution de l'application Qt
        app.exec_()
