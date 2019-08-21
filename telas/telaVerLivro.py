# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaVerLivro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyrebaseConnector as PC
import imghdr
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 502)
        MainWindow.setFixedSize(577, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.table = QtWidgets.QTableWidget(MainWindow)
        self.table.setGeometry(QtCore.QRect(190, 170, 360, 191))
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Título"))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("ISBN"))
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem("Autor Principal"))
        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem("Data de Publicação"))
        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem("Número de Páginas"))
        self.table.setColumnWidth(0, 130)
        self.table.setColumnWidth(1, 250)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.table.setFont(font)

        self.book = {}

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 170, 131, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap('images/9788544103166.jpg'))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 541, 111))
        self.label_13.setText("")
        pixmap = QtGui.QPixmap("icons/iconBuscar.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label_13.setPixmap(pixmap3)
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 400, 87, 29))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(310, 400, 87, 29))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setObjectName("button_back")
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

        self.button_back.setFont(font)
        self.button_back.setStyleSheet('background-color:#1f4c73')
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('background-color:#1f4c73')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Editar livro"))
        self.button_back.setText(_translate("MainWindow", "Voltar"))

    def UpdateTable(self):
        PC.pc.storage.child('images/books/'+str(self.book['ISBN'])).download('images/'+str(self.book['ISBN']))
        typeFile = imghdr.what('images/'+str(self.book['ISBN']))
        os.rename('images/'+str(self.book['ISBN']), 'images/'+str(self.book['ISBN'])+'.'+typeFile)
        fileName = 'images/'+str(self.book['ISBN'])+'.'+typeFile
        self.label.setPixmap(QtGui.QPixmap(fileName))

        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(self.book['title'])))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem(str(self.book['ISBN'])))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.book['leadAutor'])))
        self.table.setItem(3, 1, QtWidgets.QTableWidgetItem(str(self.book['pubDate'])))
        self.table.setItem(4, 1, QtWidgets.QTableWidgetItem(str(self.book['numPages'])))

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     Other = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(Other)
#     Other.show()
#     sys.exit(app.exec_())
