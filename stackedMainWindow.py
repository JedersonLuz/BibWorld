from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import BibWorld
import sys

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.main_ui = BibWorld.Ui_MainWindow()
        self.main_ui.setupUi(self.stack1)

        self.add_ui = BibWorld.telaAdd.Add_Form()
        self.add_ui.setupUi(self.stack2)

        self.remove_ui = BibWorld.Remover.Ui_RemoveWindow()
        self.remove_ui.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.main_ui.button_add.clicked.connect(self.OpenAddWindow)
        self.add_ui.button_voltar.clicked.connect(self.OpenMainWindow)

        self.main_ui.button_remover.clicked.connect(self.OpenRemoveWindow)
        self.remove_ui.botao_voltar.clicked.connect(self.OpenMainWindow)

    def OpenMainWindow(self):
        self.QtStack.setCurrentIndex(0)

    def OpenAddWindow(self):
        self.QtStack.setCurrentIndex(1)

    def OpenRemoveWindow(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())