# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BibWorld.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 551, 91))
        self.label.setText("")
        pixmap = QtGui.QPixmap("../icons/bibworld.png")
        pixmap3 = pixmap.scaled(561, 120, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap3)
        self.label.setObjectName("label")
        self.labelUser = QtWidgets.QLabel(self.centralwidget)
        self.labelUser.setGeometry(QtCore.QRect(280, 130, 54, 17))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.labelUser.setFont(font)
        self.labelUser.setObjectName("labelUser")
        self.labelUser1 = QtWidgets.QLabel(self.centralwidget)
        self.labelUser1.setGeometry(QtCore.QRect(340, 130, 141, 17))
        self.labelUser1.setObjectName("labelUser1")
        self.buttonAddBook = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddBook.setGeometry(QtCore.QRect(130, 260, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonAddBook.setFont(font)
        self.buttonAddBook.setObjectName("buttonAddBook")
        self.buttonEditUser = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEditUser.setGeometry(QtCore.QRect(480, 120, 30, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonEditUser.setFont(font)
        self.buttonEditUser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEditUser.setIcon(icon)
        self.buttonEditUser.setObjectName("buttonEditUser")
        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setGeometry(QtCore.QRect(520, 120, 30, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonExit.setFont(font)
        self.buttonExit.setText("")
        self.buttonExit.setIcon(icon)
        self.buttonExit.setObjectName("buttonExit")
        self.buttonRemoveBook = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRemoveBook.setGeometry(QtCore.QRect(310, 260, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonRemoveBook.setFont(font)
        self.buttonRemoveBook.setObjectName("buttonRemoveBook")
        self.buttonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSearch.setGeometry(QtCore.QRect(130, 330, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonSearch.setFont(font)
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonEditBook = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEditBook.setGeometry(QtCore.QRect(310, 330, 140, 30))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.buttonEditBook.setFont(font)
        self.buttonEditBook.setObjectName("buttonEditBook")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(150, 200, 301, 17))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)

        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelUser.setText(_translate("MainWindow", "Usuário:"))
        self.labelUser1.setText(_translate("MainWindow", "TextLabel"))
        self.buttonAddBook.setText(_translate("MainWindow", "Cadastrar livro"))
        self.buttonRemoveBook.setText(_translate("MainWindow", "Remover livro"))
        self.buttonSearch.setText(_translate("MainWindow", "Buscar livro"))
        self.buttonEditBook.setText(_translate("MainWindow", "Editar livro"))
        self.labelTitulo.setText(_translate("MainWindow", "SISTEMA DE GERENCIAMENTO DE LIVROS"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Other = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Other)
    Other.show()
    sys.exit(app.exec_())
