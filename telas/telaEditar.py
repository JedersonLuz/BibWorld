from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PyrebaseConnector as PC
import sys

class Ui_EditWindow(object):
    def messageBox(self, textMessage, nameWin):
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Information)
        infoBox.setText(textMessage)
        infoBox.setWindowTitle(nameWin)
        infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        infoBox.exec_()

    def updateTable(self):
        bookList = PC.pc.db.child('books').get().val()
        self.table.setRowCount(len(bookList)+1)

        count = 1
        for book in bookList:
            self.table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(bookList[book]['ISBN'])))
            self.table.setItem(count, 1, QtWidgets.QTableWidgetItem(bookList[book]['title']))
            count+=1

    def setupUi(self, EditWindow):
        EditWindow.setObjectName("EditWindow")
        EditWindow.resize(577, 502)
        EditWindow.setFixedSize(577, 502)
        self.centralwidget = QtWidgets.QWidget(EditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(EditWindow)
        self.label.setGeometry(QtCore.QRect(110, 310, 61, 51))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(EditWindow)
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit.setPlaceholderText('Informe o ISBN do livro')
        self.lineEdit.setGeometry(QtCore.QRect(110, 350, 150, 30))

        bookList = PC.pc.db.child('books').get().val()
       
        self.table = QtWidgets.QTableWidget(EditWindow)
        self.table.setGeometry(QtCore.QRect(110, 130, 350, 181))
        self.table.setRowCount(len(bookList)+1)
        self.table.setColumnCount(2)
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("ISBN"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Título"))
        self.table.setColumnWidth(1, 250)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.table.setFont(font)
        
        count = 1
        for book in bookList:
            self.table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(bookList[book]['ISBN'])))
            self.table.setItem(count, 1, QtWidgets.QTableWidgetItem(bookList[book]['title']))
            count+=1


        self.botao_editar = QtWidgets.QPushButton(EditWindow)
        self.botao_editar.setGeometry(QtCore.QRect(270, 350, 90, 30))
        self.botao_editar.setObjectName("botao_editar")
        self.botao_editar.setIcon(QtGui.QIcon('icons/edit.png'))
        self.botao_editar.setIconSize(QtCore.QSize(24,24))
        self.botao_editar.setStyleSheet('background-color:#1f4c73')
        self.botao_editar.setFont(font)

        self.botao_voltar = QtWidgets.QPushButton(EditWindow)
        self.botao_voltar.setGeometry(QtCore.QRect(370, 350, 90, 30))
        self.botao_voltar.setObjectName("botao_voltar")
        self.botao_voltar.setText('Voltar')
        self.botao_voltar.setStyleSheet('background-color:#1f4c73')
        self.botao_voltar.setFont(font)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(80, 10, 400, 80))
        self.label2.setText("")
        pixmap = QtGui.QPixmap("icons/iconEditar.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label2.setPixmap(pixmap3)
        self.label2.setObjectName("label")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        EditWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditWindow)
        self.statusbar.setObjectName("statusbar")
        EditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditWindow)
        QtCore.QMetaObject.connectSlotsByName(EditWindow)

    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        EditWindow.setWindowTitle(_translate("EditWindow", "Editar - BibWorld"))
        self.label.setText(_translate("EditWindow", "ISBN: "))
        self.botao_editar.setText(_translate("EditWindow", "Editar"))