# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/acucena/teste.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyrebaseConnector as PC
import sys

class Ui_RemoveWindow(object):
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
            # print(bookList[book])
            # print(bookList[book]['ISBN'], bookList[book]['title'])
            self.table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(bookList[book]['ISBN'])))
            self.table.setItem(count, 1, QtWidgets.QTableWidgetItem(bookList[book]['title']))
            count+=1

    def setupUi(self, RemoveWindow):
        RemoveWindow.setObjectName("RemoveWindow")
        RemoveWindow.resize(427, 502)
        self.centralwidget = QtWidgets.QWidget(RemoveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(RemoveWindow)
        self.label.setGeometry(QtCore.QRect(50, 310, 61, 51))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(RemoveWindow)
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit.setPlaceholderText('Informe o ISBN do livro')
        self.lineEdit.setGeometry(QtCore.QRect(50, 350, 200, 41))
       
        """ 
        self.scrollArea = QtWidgets.QScrollArea(RemoveWindow)
        self.scrollArea.setGeometry(QtCore.QRect(50, 130, 561, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        """

        bookList = PC.pc.db.child('books').get().val()
       
        self.table = QtWidgets.QTableWidget(RemoveWindow)
        self.table.setGeometry(QtCore.QRect(50, 130, 350, 181))
        self.table.setRowCount(len(bookList)+1)
        self.table.setColumnCount(2)
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("ISBN"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Título"))
        self.table.setColumnWidth(1, 250)
        
        # print(bookList['9788534525640'])
        count = 1
        for book in bookList:
            # print(bookList[book])
            # print(bookList[book]['ISBN'], bookList[book]['title'])
            self.table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(bookList[book]['ISBN'])))
            self.table.setItem(count, 1, QtWidgets.QTableWidgetItem(bookList[book]['title']))
            count+=1


        self.botao_remover = QtWidgets.QPushButton(RemoveWindow)
        self.botao_remover.setGeometry(QtCore.QRect(260, 357, 140, 30))
        self.botao_remover.setObjectName("botao_remover")
        self.botao_remover.setIcon(QtGui.QIcon('icons/delete.png'))
        self.botao_remover.setIconSize(QtCore.QSize(24,24))
        self.botao_remover.clicked.connect(self.removeBook)

        self.botao_voltar = QtWidgets.QPushButton(RemoveWindow)
        self.botao_voltar.setGeometry(QtCore.QRect(260, 400, 140, 30))
        self.botao_voltar.setObjectName("botao_voltar")
        self.botao_voltar.setText('Voltar')

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 10, 400, 80))
        self.label2.setText("")
        pixmap = QtGui.QPixmap("icons/iconRemover.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label2.setPixmap(pixmap3)
        self.label2.setObjectName("label")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        RemoveWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RemoveWindow)
        self.statusbar.setObjectName("statusbar")
        RemoveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RemoveWindow)
        QtCore.QMetaObject.connectSlotsByName(RemoveWindow)

    def retranslateUi(self, RemoveWindow):
        _translate = QtCore.QCoreApplication.translate
        RemoveWindow.setWindowTitle(_translate("RemoveWindow", "Remover - BibWorld"))
        self.label.setText(_translate("RemoveWindow", "ISBN: "))
        self.botao_remover.setText(_translate("RemoveWindow", "Remover"))

    def removeBook(self):
        removido = PC.pc.removeBook(self.lineEdit.text())
        if removido == 1:
            self.updateTable()
            self.messageBox('O livro com o ISBN de número {} foi removido.'.format(self.lineEdit.text()), 'Confimação')
            print('O livro com o ISBN de número {} foi removido.'.format(self.lineEdit.text()))
        else:
            self.messageBox('ISBN não encontrado.'.format(self.lineEdit.text()), 'Erro ao remover')

'''if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Other = QtWidgets.QMainWindow()
    ui = Ui_RemoveWindow()
    ui.setupUi(Other)
    Other.show()
    sys.exit(app.exec_())'''

