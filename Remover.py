# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/acucena/teste.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_RemoveWindow(object):
    def setupUi(self, RemoveWindow):
        RemoveWindow.setObjectName("RemoveWindow")
        RemoveWindow.resize(577, 414)
        self.centralwidget = QtWidgets.QWidget(RemoveWindow)
        self.centralwidget.setObjectName("centralwidget")

        RemoveWindow.setObjectName("Remover")
        RemoveWindow.resize(665, 411)
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
        self.lineEdit.setGeometry(QtCore.QRect(50, 350, 271, 41))
        self.scrollArea = QtWidgets.QScrollArea(RemoveWindow)
        self.scrollArea.setGeometry(QtCore.QRect(50, 130, 561, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_remover = QtWidgets.QPushButton(RemoveWindow)
        self.botao_remover.setGeometry(QtCore.QRect(340, 357, 140, 30))
        self.botao_remover.setObjectName("botao_remover")
        self.botao_remover.setIcon(QtGui.QIcon('icons/delete.png'))
        self.botao_remover.setIconSize(QtCore.QSize(24,24))


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.label2.setText("")
        pixmap = QtGui.QPixmap("icons/iconRemover.png")
        pixmap3 = pixmap.scaled(561, 120, QtCore.Qt.KeepAspectRatio)
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Other = QtWidgets.QMainWindow()
    ui = Ui_RemoveWindow()
    ui.setupUi(Other)
    Other.show()
    sys.exit(app.exec_())

