import time

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QCheckBox, QSlider, QTextEdit, QFileDialog, QProgressBar

from worker.worker import Worker
from Resources.counter import count_to_percent, count


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.words_nbr = None
        self.groups = []
        self.threads = []
        self.core = 1
        self.setWindowTitle("InstaFu")
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)

        # Main layer UI
        self.layer = QWidget(self)
        self.layer.setGeometry(0, 0, 800, 50)
        self.layer.setStyleSheet("background-color: rgb(51, 51, 51);")

        # Run button UI
        self.buttonRun = QPushButton("Run", self.layer)
        self.buttonRun.setGeometry(730, 12, 50, 25)
        self.buttonRun.setEnabled(False)
        self.buttonRun.setStyleSheet(
            "QPushButton:hover {background-color: #00CC91;}"
            "QPushButton:disabled {background-color: #ff0000;}"
            "QPushButton:enabled {background-color: #14B58A;}"
        )

        # Run button UI connect function
        self.buttonRun.clicked.connect(self.run)

        # Stop button UI
        self.buttonStop = QPushButton("Stop", self.layer)
        self.buttonStop.setGeometry(670, 12, 50, 25)
        self.buttonStop.setStyleSheet(
            "QPushButton {color: #ccc;}"
        )

        # Stop button UI connect function
        self.buttonStop.clicked.connect(self.stop)

        # File button UI
        self.buttonFile = QPushButton("File", self.layer)
        self.buttonFile.setGeometry(610, 12, 50, 25)
        self.buttonFile.setStyleSheet(
            "QPushButton {color: #ccc;}"
        )

        # File button UI connect function
        self.buttonFile.clicked.connect(self.openFile)

        # Headless checkbox UI
        self.checkboxHeadless = QCheckBox("Headless", self.layer)
        self.checkboxHeadless.setGeometry(25, 0, 200, 50)
        self.checkboxHeadless.setChecked(False)
        self.checkboxHeadless.setStyleSheet(
             "QCheckBox {color: #e6e6e6;}"
         )

        # CORES Slider Title UI
        self.labelCPU = QLabel("CORE:", self.layer)
        self.labelCPU.setGeometry(140, 0, 200, 50)
        self.labelCPU.setStyleSheet(
            "QLabel {color: #ccc;}"
        )

        # CORES Slider UI
        self.sliderCPU = QSlider(Qt.Horizontal, self)
        self.sliderCPU.setGeometry(200, 2, 100, 50)
        self.sliderCPU.setMinimum(1)
        self.sliderCPU.setMaximum(10)
        self.sliderCPU.setValue(1)

        # CORES Number Label UI
        self.nbrCPU = QLabel(self)
        self.nbrCPU.setGeometry(180, 0, 20, 50)
        self.nbrCPU.setAlignment(Qt.AlignCenter)
        self.nbrCPU.setText(str(self.sliderCPU.value()))
        self.nbrCPU.setStyleSheet(
            "QLabel {color: #ccc;}"
        )

        # Progress Bar UI
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(350, 15, 200, 20)
        self.progressBar.setValue(0)

        # Progress Label UI
        self.valueLabel = QLabel(self)
        self.valueLabel.setGeometry(353, 14, 50, 20)
        self.valueLabel.setText('0')

        # ProgressMax Label UI
        self.MaxValueLabel = QLabel(self)
        self.MaxValueLabel.setGeometry(550, 14, 50, 20)
        self.MaxValueLabel.setText('0')
        self.MaxValueLabel.setStyleSheet(
            "QLabel {color: #ccc;}"
        )

        # CORES Slider UI connect function
        self.sliderCPU.valueChanged.connect(self.updateLabelCPU)

        # Console Window UI
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

        # Show window UI
        self.show()

    def updateLabelCPU(self):
        self.nbrCPU.setText(str(self.sliderCPU.value()))
        self.core = self.sliderCPU.value()

    def updateLabelCounter(self):
        value = count_to_percent(self.words_nbr)
        self.progressBar.setValue(value)
        self.valueLabel.setText(str(count()))

    def print_message(self, message):
        now = QDateTime.currentDateTime()
        self.console.append(f"{now.toString('hh:mm:ss')} $: {message}")

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = (QFileDialog.getOpenFileName
                       (self, "QFileDialog.getOpenFileName()",
                        "", "All Files (*);;Text Files (*.txt)",
                        options=options))
        if fileName:
            self.print_message(f'File loaded: {fileName}')
            self.create_temp(fileName)
            self.buttonRun.setEnabled(True)

    def create_temp(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()

        self.words_nbr = len(lines)
        groups_len = self.words_nbr // self.core

        self.MaxValueLabel.setText(str(self.words_nbr))

        self.groups = []
        for i in range(self.core):
            start = i * groups_len
            end = start + groups_len if i < self.core - 1 else self.words_nbr
            self.groups.append(lines[start:end])

        self.print_message(f'Words loaded: {self.words_nbr}')
        self.print_message(f'Core configuration : {self.core}')
        self.print_message(f'Processing groups: {groups_len}')
        self.print_message(f'You can reload a file with different core numbers before running')
        self.print_message(f'You can now run the program')
        self.print_message(f'----------------------------------------------------------------')
        self.print_message(f'----------------------------------------------------------------')
        self.buttonRun.setEnabled(True)

    def run(self):
        self.buttonRun.setEnabled(False)
        option = self.checkboxHeadless.isChecked()
        # Create Thread for each core
        self.threads = []
        x, y = 0, 0
        for i, words in enumerate(self.groups):
            worker = Worker(i+1, self, option, x, words)
            worker.signal.connect(self.print_message)
            self.threads.append(worker)
            worker.start()
            x += 100
            time.sleep(0.45)

    def stop(self):
        for worker in self.threads:
            worker.stop()
            self.threads = []
            self.print_message(f'Core number(s) : {str(self.core)}')
            self.buttonRun.setEnabled(True)
