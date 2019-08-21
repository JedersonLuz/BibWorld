# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telas/telaEditUser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PyrebaseConnector as PC
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 502)
        Form.setFixedSize(577, 502)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 25, 401, 61))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 120, 231, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setDisabled(True)
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Feminino')
        self.comboBox.addItem('Masculino')
        self.verticalLayout.addWidget(self.comboBox)

        self.buttonResetPass = QtWidgets.QPushButton(Form)
        self.buttonResetPass.setObjectName('buttonResetPass')
        self.buttonResetPass.setGeometry(QtCore.QRect(250, 410, 71, 31))
        self.buttonResetPass.setStyleSheet('background-color:#1f4c73')
        self.buttonResetPass.setFont(font)

        self.button_cadastrar = QtWidgets.QPushButton(Form)
        self.button_cadastrar.setGeometry(QtCore.QRect(330, 410, 71, 31))
        self.button_cadastrar.setStyleSheet('background-color:#1f4c73')
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_cadastrar.setFont(font)
        self.button_cadastrar.setObjectName("button_cadastrar")
        self.button_back = QtWidgets.QPushButton(Form)
        self.button_back.setGeometry(QtCore.QRect(170, 410, 71, 31))
        self.button_back.setStyleSheet('background-color:#1f4c73')
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setObjectName("button_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        pixmap = QtGui.QPixmap("icons/iconEditUser.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setText(_translate("Form", "Email:"))
        self.label_7.setText(_translate("Form", "Nome de usuário:"))
        self.label_5.setText(_translate("Form", "Data de nascimento:"))
        self.label_4.setText(_translate("Form", "Sexo:"))
        self.button_cadastrar.setText(_translate("Form", "Salvar"))
        self.button_cadastrar.clicked.connect(self.UpdateUser)
        self.buttonResetPass.setText(_translate('Form', 'Mudar\nsenha'))
        self.buttonResetPass.clicked.connect(self.changePass)
        self.button_back.setText(_translate("Form", "Voltar"))

    def changePass(self):
        PC.pc.changePassword(PC.pc.auth.current_user['email'])
        self.messageBox('Enviamos um email para você com as instruções para cadastrar uma nova senha!', 'Alerta')

    def messageBox(self, textMessage, nameWin):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(textMessage)
        infoBox.setWindowTitle(nameWin)
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()

    def UpdateUser(self):
        erroVazio = 0
        if self.lineEdit_5.text() == '':
            erroVazio = 1
            self.messageBox('Campos obrigatórios!', 'Erro')
        
        if erroVazio == 0:
            PC.pc.updateUser(self.lineEdit_5.text(), self.dateEdit.text(), self.comboBox.currentText())
            self.messageBox('Dados atualizados!', 'Mensagem')

""" if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Other = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Other)
    Other.show()
    sys.exit(app.exec_()) """