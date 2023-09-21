import sys
from PyQt5.QtWidgets import QApplication
from GUI.gui import MainWindow
from Resources.counter import add_count

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.print_message("")
    window.print_message("")
    window.print_message("          /$$$$$$                       /$$               /$$$$$$$$       ")
    window.print_message("         |_  $$_/                      | $$              | $$_____/       ")
    window.print_message("           | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$    /$$   /$$")
    window.print_message("           | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$$$$| $$  | $$")
    window.print_message("           | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$__/| $$  | $$")
    window.print_message("           | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$   | $$  | $$")
    window.print_message("          /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$   |  $$$$$$/")
    window.print_message("         |______/|__/  |__/|_______/    \___/   \_______/|__/    \______/ ")
    window.print_message("")
    window.print_message("")
    window.print_message("       -------------Welcome-to-InstaFu----------------------------------------")
    window.print_message("       |                                                                     |")
    window.print_message("       |     1 - Choose a txt file with the 'File' button                    |")
    window.print_message("       |     2 - Choose number of Core with the 'Core' Slider                |")
    window.print_message("       |     3 - You can choose headless option on/off                       |")
    window.print_message("       |     4 - Press Run to launch the program                             |")
    window.print_message("       |                                                                     |")
    window.print_message("       ------------------------------------------------------Have-Fun---------")
    window.print_message("")
    window.print_message("")
    # Execut QT application
    app.exec_()

