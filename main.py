import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 600)
        # Bouton 1
        btnMessage1 = QPushButton(self)
        btnMessage1.setFixedSize(150, 40)
        btnMessage1.setText('Message 1')
        btnMessage1.move(20, 150)
        btnMessage1.clicked.connect(lambda: self.evt_btnMessage_clicked(btnMessage1.text()))

        # Bouton 2
        btnMessage2 = QPushButton(self)
        btnMessage2.setFixedSize(150, 40)
        btnMessage2.setText('Message 2')
        btnMessage2.move(20, 250)
        btnMessage2.clicked.connect(lambda: self.evt_btnMessage_clicked(btnMessage2.text()))

    def evt_btnMessage_clicked(self, msg):
        # Création de la boîte de message
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle('Titre du message')
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        result = msgBox.exec_()


if __name__ == "__main__":
    app =QApplication(sys.argv)
    # Fenêtre principale
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())