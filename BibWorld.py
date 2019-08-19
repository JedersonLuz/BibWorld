# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vitoria/BibWorld.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from telas import telaAdd, Remover, telaEditar, telaEditForm, telaBuscar, telaVerLivro, loginWindows, telaAddUser
import sys


class Ui_MainWindow(object):
    def openAdd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = telaAdd.Add_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openEditar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = telaEditar.Editar_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRemove(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Remover.Ui_RemoveWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 502)
        MainWindow.setFixedSize(577, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar.setGeometry(QtCore.QRect(130, 290, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_buscar.setFont(font)
        self.button_buscar.setObjectName("button_buscar")
        self.button_buscar.setIcon(QtGui.QIcon('icons/search.png'))
        self.button_buscar.setIconSize(QtCore.QSize(24,24))
        self.button_buscar.setStyleSheet('background-color:#1f4c73')

        self.button_editar = QtWidgets.QPushButton(self.centralwidget)
        self.button_editar.setGeometry(QtCore.QRect(320, 290, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_editar.setFont(font)
        self.button_editar.setObjectName("button_editar")
        self.button_editar.setIcon(QtGui.QIcon('icons/edit.png'))
        self.button_editar.setIconSize(QtCore.QSize(24,24))
        self.button_editar.setStyleSheet('background-color:#1f4c73')
        # self.button_editar.clicked.connect(self.openEditar)

        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(130, 210, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.button_add.setIcon(QtGui.QIcon('icons/plus.png'))
        self.button_add.setIconSize(QtCore.QSize(24,24))
        # self.button_add.clicked.connect(self.openAdd)
        self.button_add.setStyleSheet('background-color:#1f4c73')

        self.button_remover = QtWidgets.QPushButton(self.centralwidget)
        self.button_remover.setGeometry(QtCore.QRect(320, 210, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_remover.setFont(font)
        self.button_remover.setObjectName("button_remover")
        self.button_remover.setIcon(QtGui.QIcon('icons/delete.png'))
        self.button_remover.setIconSize(QtCore.QSize(24,24))
        self.button_remover.setStyleSheet('background-color:#1f4c73')
        # self.button_remover.clicked.connect(self.openRemove)
        """ self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_remover.setIconSize(QtCore.QSize(24,24))
        self.verticalLayout.addWidget(self.button_remover) """

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.label.setText("")
        pixmap = QtGui.QPixmap("icons/bibworld.png")
        pixmap3 = pixmap.scaled(561, 120, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap3)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_buscar.setText(_translate("MainWindow", " Buscar livro"))
        self.button_editar.setText(_translate("MainWindow", " Editar livro"))
        self.button_add.setText(_translate("MainWindow", " Cadastrar livro"))
        self.button_remover.setText(_translate("MainWindow", " Remover livro"))


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     Other = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(Other)
#     Other.show()
#     sys.exit(app.exec_())
