# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 502)
        Form.setFixedSize(577, 502)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 401, 61))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 108, 231, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEmail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelEmail.setFont(font)
        self.labelEmail.setObjectName("labelEmail")
        self.verticalLayout.addWidget(self.labelEmail)
        self.lineEditEmail = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditEmail.setPlaceholderText('Informe o seu email')
        self.verticalLayout.addWidget(self.lineEditEmail)
        self.labelUserName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelUserName.setFont(font)
        self.labelUserName.setObjectName("labelUserName")
        self.verticalLayout.addWidget(self.labelUserName)
        self.lineEditUserName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditUserName.setPlaceholderText('Informe o seu nome de usuário')
        self.verticalLayout.addWidget(self.lineEditUserName)
        self.labelPassword = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setPlaceholderText('Informe a sua senha')
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.labelPassword2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword2.setFont(font)
        self.labelPassword2.setObjectName("labelPassword2")
        self.verticalLayout.addWidget(self.labelPassword2)
        self.lineEditPassword_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword_2.setObjectName("lineEditPassword_2")
        self.lineEditPassword_2.setPlaceholderText('Confirme a sua senha')
        self.verticalLayout.addWidget(self.lineEditPassword_2)
        self.labelDateBirth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelDateBirth.setFont(font)
        self.labelDateBirth.setObjectName("labelDateBirth")
        self.verticalLayout.addWidget(self.labelDateBirth)
        self.dateBirth = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateBirth.setObjectName("dateBirth")
        self.verticalLayout.addWidget(self.dateBirth)
        self.labelGender = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.labelGender.setFont(font)
        self.labelGender.setObjectName("labelGender")
        self.verticalLayout.addWidget(self.labelGender)
        self.selectGender = QtWidgets.QComboBox(self.layoutWidget)
        self.selectGender.setObjectName("selectGender")
        self.selectGender.addItem('Feminino')
        self.selectGender.addItem('Masculino')
        self.verticalLayout.addWidget(self.selectGender)
        self.buttonSubmit = QtWidgets.QPushButton(Form)
        self.buttonSubmit.setGeometry(QtCore.QRect(260, 450, 141, 29))
        self.buttonSubmit.setStyleSheet('background-color:#1f4c73')
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.buttonSubmit.setFont(font)
        self.buttonSubmit.setObjectName("buttonSubmit")
        self.buttonBack = QtWidgets.QPushButton(Form)
        self.buttonBack.setGeometry(QtCore.QRect(170, 450, 71, 29))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.buttonBack.setFont(font)
        self.buttonBack.setObjectName("buttonBack")
        self.buttonBack.setStyleSheet('background-color:#1f4c73')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Cadastro de Usuário")
        self.label.setText(_translate("Form", "TextLabel"))
        pixmap = QtGui.QPixmap("icons/iconCadUser.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEmail.setText(_translate("Form", "Email:"))
        self.labelUserName.setText(_translate("Form", "Nome de usuário:"))
        self.labelPassword.setText(_translate("Form", "Senha:"))
        self.labelPassword2.setText(_translate("Form", "Confirme a senha:"))
        self.labelDateBirth.setText(_translate("Form", "Data de nascimento:"))
        self.labelGender.setText(_translate("Form", "Sexo:"))
        self.buttonSubmit.setText(_translate("Form", "Concluir cadastro"))
        self.buttonBack.setText(_translate("Form", "Voltar"))