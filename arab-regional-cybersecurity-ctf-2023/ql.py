import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout , QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Open QListWindow")
        self.button.clicked.connect(self.openQListWindow)
        self.variable_to_pass = "Hello from MainWindow"

        self.setCentralWidget(self.button)

    def openQListWindow(self):
        self.qListWindow = QListWindow(self.variable_to_pass)
        self.qListWindow.exec_()

class QListWindow(QDialog):
    def __init__(self, variable_to_receive):
        super().__init__()
        self.variable_received = variable_to_receive
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Received Variable: {self.variable_received}"))

        self.setLayout(layout)
        self.setWindowTitle("QListWindow")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
