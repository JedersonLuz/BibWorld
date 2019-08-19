# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vitoria/telaAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyrebaseConnector as PC
import datetime
from PyQt5.QtWidgets import QMessageBox


class Add_Form(object):
    def setupUi(self, Form):
        self.fname = ''
        Form.setObjectName("Form")
        Form.resize(577, 502)
        Form.setFixedSize(577, 502)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 401, 61))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.button_voltar = QtWidgets.QPushButton(Form)
        self.button_voltar.setGeometry(QtCore.QRect(170, 450, 90, 29))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_voltar.setFont(font)
        self.button_voltar.setObjectName("button_voltar")
        # self.button_voltar.clicked.connect(self.registerBook)
        self.button_voltar.setStyleSheet('background-color:#1f4c73')
        self.button_voltar.setText('Voltar')
        
        self.button_cadastrar = QtWidgets.QPushButton(Form)
        self.button_cadastrar.setGeometry(QtCore.QRect(270, 450, 131, 29))
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_cadastrar.setFont(font)
        self.button_cadastrar.setObjectName("button_cadastrar")
        self.button_cadastrar.clicked.connect(self.registerBook)
        self.button_cadastrar.setStyleSheet('background-color:#1f4c73')
        #self.button_cadastrar.setStyleSheet('font-color:white;')
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(170, 108, 231, 321))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineTitulo = QtWidgets.QLineEdit(self.widget)
        self.lineTitulo.setObjectName("lineTitulo")
        self.lineTitulo.setPlaceholderText('Informe o título do livro')
        self.verticalLayout.addWidget(self.lineTitulo)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineISBN = QtWidgets.QLineEdit(self.widget)
        self.lineISBN.setObjectName("lineISBN")
        self.lineISBN.setPlaceholderText('Informe o ISBN do livro')
        self.verticalLayout.addWidget(self.lineISBN)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineAutor = QtWidgets.QLineEdit(self.widget)
        self.lineAutor.setObjectName("lineAutor")
        self.lineAutor.setPlaceholderText('Informe o autor principal do livro')
        self.verticalLayout.addWidget(self.lineAutor)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        #self.dateEdit.setDateTime(QDate(2019, 8, 13))
        self.verticalLayout.addWidget(self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineNumPag = QtWidgets.QLineEdit(self.widget)
        self.lineNumPag.setObjectName("lineNumPag")
        self.lineNumPag.setPlaceholderText('Informe o nº de páginas do livro')
        self.verticalLayout.addWidget(self.lineNumPag)
        self.button_escolher = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("KacstOne")
        font.setBold(True)
        font.setWeight(75)
        self.button_escolher.setFont(font)
        self.button_escolher.setObjectName("button_escolher")
        self.button_escolher.setIcon(QtGui.QIcon('icons/upload.png'))
        self.button_escolher.setIconSize(QtCore.QSize(24,24))
        self.button_escolher.clicked.connect(self.openFileNameDialog)
        self.verticalLayout.addWidget(self.button_escolher)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Cadastro")
        self.label.setText(_translate("Form", "TextLabel"))
        pixmap = QtGui.QPixmap("icons/iconCadastrar.png")
        pixmap3 = pixmap.scaled(400, 80, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button_cadastrar.setText(_translate("Form", "Concluir cadastro"))
        self.button_voltar.setText(_translate("Form", "Voltar"))
        self.label_6.setText(_translate("Form", "Título"))
        self.label_2.setText(_translate("Form", " ISBN"))
        self.label_3.setText(_translate("Form", "Autor principal"))
        self.label_5.setText(_translate("Form", "Data de publicação"))
        self.label_4.setText(_translate("Form", "Nºde páginas"))
        self.button_escolher.setText(_translate("Form", " Escolher imagem de capa"))

    def openFileNameDialog(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '',"Image files (*.jpg *.gif *.png *.jpeg)")
        # print(fname)

    def messageBox(self, textMessage, nameWin):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(textMessage)
        infoBox.setWindowTitle(nameWin)
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.exec_()

    def registerBook(self):
        # print(self.fname)
        erroNum = 0
        erroISBN = 0
        erroVazio = 0
        erroISBNExiste = 0

        if PC.pc.searchBook_ISBN(self.lineISBN.text()):
            self.messageBox('ISBN já existe!', 'Erro')
            erroISBNExiste = 1

        if((self.lineISBN.text() == '') or (self.lineTitulo.text() == '') or (self.lineAutor.text() == '') or (self.lineNumPag.text() == '') or (self.fname == '')):
            self.messageBox("Todas os campos devem ser preenchidos!", "Campos obrigatórios")
            erroVazio = 1

        if((erroISBN == 0) and (erroVazio == 0)):
            try:
                int(self.lineISBN.text())
            except:
                self.messageBox("O ISBN é um campo de números! Tente novamente!", "Erro")
                erroNum = 1

        if(erroNum == 0 and (erroISBN == 0) and (erroVazio == 0)):
            try:
                int(self.lineNumPag.text())
            except:
                self.messageBox("Número de páginas inválido! Tente novamente!", "Erro")
                erroNum = 1

        if((erroISBN == 0) and (erroNum == 0) and (erroVazio == 0) and (erroISBNExiste == 0)):
            PC.pc.createBook(self.lineISBN.text(), self.lineTitulo.text(), self.lineAutor.text(), self.lineNumPag.text(), self.dateEdit.text(), self.fname)
            self.messageBox("Livro cadastrado com sucesso!", "Confirmação de cadastro")
            self.lineISBN.setText('')
            self.lineTitulo.setText('')
            self.lineAutor.setText('')
            self.lineNumPag.setText('')