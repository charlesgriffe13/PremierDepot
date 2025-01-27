import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LblColor(QPushButton):

    def __init__(self, color):
        super().__init__()
        self.color = color
        print(color)
        self.setFixedSize(75, 75)
        self.setStyleSheet(f'background-color : {color}')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 600)
        # Bouton 1
        self.btnMessage1 = QPushButton(self)
        self.btnMessage1.setFixedSize(150, 40)
        self.btnMessage1.setText('Message 1')
        self.btnMessage1.move(20, 150)
        self.btnMessage1.clicked.connect(lambda: self.evt_btnMessage_clicked(self.btnMessage1.text()))

        # Bouton 2
        self.btnMessage2 = QPushButton(self)
        self.btnMessage2.setFixedSize(150, 40)
        self.btnMessage2.setText('Message 2')
        self.btnMessage2.move(20, 250)
        self.btnMessage2.clicked.connect(lambda: self.evt_btnMessage_clicked(self.btnMessage2.text()))

        self.lblBlue = LblColor('blue')
        self.lblBlue.setParent(self)
        self.lblBlue.move(10, 400)
        self.lblBlue.clicked.connect(lambda: self.label_clicked('blue'))

        self.lblRed = LblColor('red')
        self.lblRed.setParent(self)
        self.lblRed.move(100, 400)
        self.lblRed.clicked.connect(lambda: self.label_clicked('red'))

    def label_clicked(self, color):
        self.btnMessage1.setStyleSheet(f'background-color: {color}')
        self.btnMessage2.setStyleSheet(f'background-color: {color}')


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