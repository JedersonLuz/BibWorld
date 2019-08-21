from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PyrebaseConnector as PC
import BibWorld
import sys

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 480)

        self.flagEdit = 4

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

        self.login_ui = BibWorld.loginWindows.Ui_Form()
        self.login_ui.setupUi(self.stack0)

        self.add_user_ui = BibWorld.telaAddUser.Ui_Form()
        self.add_user_ui.setupUi(self.stack8)

        self.main_ui = BibWorld.Ui_MainWindow()
        self.main_ui.setupUi(self.stack1)

        self.add_ui = BibWorld.telaAdd.Add_Form()
        self.add_ui.setupUi(self.stack2)

        self.remove_ui = BibWorld.Remover.Ui_RemoveWindow()
        self.remove_ui.setupUi(self.stack3)

        self.edit_ui = BibWorld.telaEditar.Ui_EditWindow()
        self.edit_ui.setupUi(self.stack4)

        self.edit_form_ui = BibWorld.telaEditForm.Edit_Form()
        self.edit_form_ui.setupUi(self.stack5)

        self.search_ui = BibWorld.telaBuscar.Ui_BuscarWindow()
        self.search_ui.setupUi(self.stack6)

        self.read_ui = BibWorld.telaVerLivro.Ui_MainWindow()
        self.read_ui.setupUi(self.stack7)

        self.editUser_ui = BibWorld.telaEditUser.Ui_Form()
        self.editUser_ui.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.login_ui.pushButton.clicked.connect(self.MakeLogin)
        self.login_ui.pushButton_2.clicked.connect(self.OpenSignUpWindow)

        self.add_user_ui.buttonSubmit.clicked.connect(self.MakeSignUp)
        self.add_user_ui.buttonBack.clicked.connect(self.OpenLoginWindow)

        self.main_ui.buttonAddBook.clicked.connect(self.OpenAddWindow)
        self.add_ui.button_voltar.clicked.connect(self.OpenMainWindow)

        self.main_ui.buttonRemoveBook.clicked.connect(self.OpenRemoveWindow)
        self.remove_ui.botao_voltar.clicked.connect(self.OpenMainWindow)

        self.main_ui.buttonEditBook.clicked.connect(self.OpenEditWindow)
        self.edit_ui.botao_voltar.clicked.connect(self.OpenMainWindow)
        self.edit_ui.botao_editar.clicked.connect(self.OpenEditFormWindows)
        self.edit_form_ui.button_cadastrar.clicked.connect(self.editBook)
        self.edit_form_ui.button_voltar.clicked.connect(self.OpenEditWindow)

        self.main_ui.buttonSearch.clicked.connect(self.OpenBuscarWindow)
        self.search_ui.botao_voltar.clicked.connect(self.OpenMainWindow)
        self.search_ui.botao_buscar.clicked.connect(self.OpenReadWindow)
        self.read_ui.button_back.clicked.connect(self.OpenBuscarWindow)
        self.read_ui.pushButton.clicked.connect(self.OpenEditFormWindows_telaVerLivro)

        self.main_ui.buttonEditUser.clicked.connect(self.OpenEditUser)
        self.main_ui.buttonExit.clicked.connect(self.messageBoxExit)
        self.editUser_ui.button_back.clicked.connect(self.OpenMainWindow)

    def MakeLogin(self):
        erroVazio = 0
        if (self.login_ui.lineEdit.text() == '') or (self.login_ui.lineEdit_2.text() == ''):
            self.edit_ui.messageBox('Campos obrigatórios!', 'Erro')
            erroVazio = 1
        if erroVazio == 0:
            email = self.login_ui.lineEdit.text()
            password = self.login_ui.lineEdit_2.text()
            response = PC.pc.login(email, password)
            if response == 'Ok':
                self.OpenMainWindow()
            else:
                self.edit_ui.messageBox(response, 'Erro')

    def messageBoxExit(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText('Tem certeza que deseja sair?')
        infoBox.setWindowTitle('Alerta')
        infoBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        infoBox.buttonClicked.connect(self.BackLogin)
        infoBox.exec_()

    def BackLogin(self, choosedButton):
        if choosedButton.text() == '&Yes':
            self.login_ui.lineEdit.setText('')
            self.login_ui.lineEdit_2.setText('')
            self.OpenLoginWindow()

    def MakeSignUp(self):
        email = self.add_user_ui.lineEditEmail.text()
        password = self.add_user_ui.lineEditPassword.text()
        password_2 = self.add_user_ui.lineEditPassword_2.text()
        displayName = self.add_user_ui.lineEditUserName.text()
        dateBirth = self.add_user_ui.dateBirth.text()
        gender = self.add_user_ui.selectGender.currentText()

        erroVazio = 0
        if (email == '') or (password == '') or (password_2 == '') or (displayName == ''):
            self.edit_ui.messageBox('Campos obrigatórios.', 'Erro')
            erroVazio = 1
        
        erroSenha = 0
        if (password != password_2) and (erroVazio == 0):
            self.edit_ui.messageBox('Os campos de senha não coincidem.', 'Erro')
            erroSenha = 1

        if (erroVazio == 0) and (erroSenha == 0):
            response = PC.pc.signUp(email, password, displayName, dateBirth, gender)
            if response == 'Ok':
                self.edit_ui.messageBox('Cadastro realizado com sucesso. Bem-vindo (a) ao BibWorld!', 'Confirmação')
                self.OpenLoginWindow()
            else:
                self.edit_ui.messageBox(response, 'Erro')
    
    def OpenSignUpWindow(self):
        self.QtStack.setCurrentIndex(8)

    def OpenLoginWindow(self):
        self.QtStack.setCurrentIndex(0)

    def OpenMainWindow(self):
        keyUser = PC.pc.auth.current_user['localId']
        currentUser = PC.pc.db.child('users').child(keyUser).get()
        self.main_ui.labelUser1.setText(currentUser.val()['displayName'])
        self.QtStack.setCurrentIndex(1)

    def OpenAddWindow(self):
        self.QtStack.setCurrentIndex(2)

    def OpenRemoveWindow(self):
        self.remove_ui.updateTable()
        self.QtStack.setCurrentIndex(3)

    def OpenEditWindow(self):
        self.edit_ui.updateTable()
        self.QtStack.setCurrentIndex(4)

    def OpenEditFormWindows(self):
        self.flagEdit = 4
        if self.edit_ui.lineEdit.text() == '':
            self.edit_ui.messageBox("Campo obrigatório!", "Aviso")
        else:
            try:
                int(self.edit_ui.lineEdit.text())
                book = PC.pc.searchBook_ISBN(self.edit_ui.lineEdit.text())
                if book:
                    self.edit_form_ui.lineTitulo.setText(book['title'])
                    self.edit_form_ui.lineISBN.setText(str(book['ISBN']))
                    self.edit_form_ui.lineAutor.setText(book['leadAutor'])
                    self.edit_form_ui.lineNumPag.setText(str(book['numPages']))
                    self.edit_form_ui.dateEdit.setDate(QtCore.QDate(int(book['pubDate'].split('/')[2]), int(book['pubDate'].split('/')[1]), int(book['pubDate'].split('/')[0])))

                    self.QtStack.setCurrentIndex(5)

                    self.edit_ui.lineEdit.setText('')
                else:
                    self.edit_ui.messageBox("ISBN não encontrado!", "Erro")
            except:
                self.edit_ui.messageBox("O ISBN é um campo de números! Tente novamente!", "Erro")

    def OpenEditFormWindows_telaVerLivro(self):
        self.flagEdit = 7
        self.edit_form_ui.lineTitulo.setText(self.read_ui.book['title'])
        self.edit_form_ui.lineISBN.setText(str(self.read_ui.book['ISBN']))
        self.edit_form_ui.lineAutor.setText(self.read_ui.book['leadAutor'])
        self.edit_form_ui.lineNumPag.setText(str(self.read_ui.book['numPages']))
        self.edit_form_ui.dateEdit.setDate(QtCore.QDate(int(self.read_ui.book['pubDate'].split('/')[2]), int(self.read_ui.book['pubDate'].split('/')[1]), int(self.read_ui.book['pubDate'].split('/')[0])))

        self.QtStack.setCurrentIndex(5)

    def OpenBuscarWindow(self):
        self.search_ui.updateTable()
        self.QtStack.setCurrentIndex(6)

    def OpenReadWindow(self):
        erroVazio = 0
        if(self.search_ui.lineEdit.text() == ''):
            self.edit_ui.messageBox('Campo obrigatório!', 'Erro')
            erroVazio = 1

        if(erroVazio == 0):
            self.read_ui.book = PC.pc.searchBook_ISBN(self.search_ui.lineEdit.text())
            if(self.read_ui.book != None):
                self.read_ui.UpdateTable()
                self.QtStack.setCurrentIndex(7)
            else:
                self.edit_ui.messageBox('ISBN não existe!', 'Erro')

    def OpenEditUser(self):
        keyUser = PC.pc.auth.current_user['localId']
        email = PC.pc.auth.current_user['email']
        currentUser = PC.pc.db.child('users').child(keyUser).get()
        self.editUser_ui.lineEdit_4.setText(email)
        self.editUser_ui.lineEdit_5.setText(currentUser.val()['displayName'])
        self.editUser_ui.dateEdit.setDate(QtCore.QDate(int(currentUser.val()['dateBirth'].split('/')[2]), int(currentUser.val()['dateBirth'].split('/')[1]), int(currentUser.val()['dateBirth'].split('/')[0])))
        if currentUser.val()['gender'] == 'Feminino': gender = 0
        else: gender = 1
        self.editUser_ui.comboBox.setCurrentIndex(gender)
        self.QtStack.setCurrentIndex(9)

    def editBook(self):
        # print(self.fname)
        erroNum = 0
        erroISBN = 0
        erroVazio = 0

        if((self.edit_form_ui.lineISBN.text() == '') or (self.edit_form_ui.lineTitulo.text() == '') or (self.edit_form_ui.lineAutor.text() == '') or (self.edit_form_ui.lineNumPag.text() == '') or (self.edit_form_ui.fname == '')):
            self.edit_form_ui.messageBox("Todas os campos devem ser preenchidos!", "Campos obrigatórios")
            erroVazio = 1

        if((erroISBN == 0) and (erroVazio == 0)):
            try:
                int(self.edit_form_ui.lineISBN.text())
            except:
                self.edit_form_ui.messageBox("O ISBN é um campo de números! Tente novamente!", "Erro")
                erroISBN = 1

        if(erroNum == 0 and (erroISBN == 0) and (erroVazio == 0)):
            try:
                int(self.edit_form_ui.lineNumPag.text())
            except:
                self.edit_form_ui.messageBox("Número de páginas inválido! Tente novamente!", "Erro")
                erroNum = 1

        if((erroISBN == 0) and (erroNum == 0) and (erroVazio == 0)):
            PC.pc.updateBook(self.edit_form_ui.lineISBN.text(), self.edit_form_ui.lineTitulo.text(), self.edit_form_ui.lineAutor.text(), self.edit_form_ui.lineNumPag.text(), self.edit_form_ui.dateEdit.text(), self.edit_form_ui.fname)
            self.edit_form_ui.messageBox("Alterações salvas com sucesso!", "Confirmação de alteração")
            self.edit_form_ui.lineISBN.setText('')
            self.edit_form_ui.lineTitulo.setText('')
            self.edit_form_ui.lineAutor.setText('')
            self.edit_form_ui.lineNumPag.setText('')
            self.QtStack.setCurrentIndex(self.flagEdit)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())