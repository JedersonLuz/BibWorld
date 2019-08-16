from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyrebaseConnector as PC
import BibWorld
import sys

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

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

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.main_ui.button_add.clicked.connect(self.OpenAddWindow)
        self.add_ui.button_voltar.clicked.connect(self.OpenMainWindow)

        self.main_ui.button_remover.clicked.connect(self.OpenRemoveWindow)
        self.remove_ui.botao_voltar.clicked.connect(self.OpenMainWindow)

        self.main_ui.button_editar.clicked.connect(self.OpenEditWindow)
        self.edit_ui.botao_voltar.clicked.connect(self.OpenMainWindow)
        self.edit_ui.botao_editar.clicked.connect(self.OpenEditFormWindows)
        self.edit_form_ui.button_cadastrar.clicked.connect(self.OpenEditWindow)
        self.edit_form_ui.button_voltar.clicked.connect(self.OpenEditWindow)

        self.main_ui.button_buscar.clicked.connect(self.OpenBuscarWindow)
        self.search_ui.botao_voltar.clicked.connect(self.OpenMainWindow)
        self.search_ui.botao_buscar.clicked.connect(self.OpenReadWindow)
        self.read_ui.button_back.clicked.connect(self.OpenBuscarWindow)
        self.read_ui.pushButton.clicked.connect(self.OpenEditFormWindows)

    def OpenMainWindow(self):
        self.QtStack.setCurrentIndex(0)

    def OpenAddWindow(self):
        self.QtStack.setCurrentIndex(1)

    def OpenRemoveWindow(self):
        self.remove_ui.updateTable()
        self.QtStack.setCurrentIndex(2)

    def OpenEditWindow(self):
        self.edit_ui.updateTable()
        self.QtStack.setCurrentIndex(3)

    def OpenEditFormWindows(self):
        if self.edit_ui.lineEdit.text() == '':
            self.edit_ui.messageBox("Campo obrigatório!", "Aviso")
        else:
            try:
                int(self.edit_ui.lineEdit.text())
                book = PC.pc.searchBook_ISBN(self.edit_ui.lineEdit.text())
                print(book)
                if book:
                    self.edit_form_ui.lineTitulo.setText(book['title'])
                    self.edit_form_ui.lineISBN.setText(str(book['ISBN']))
                    self.edit_form_ui.lineAutor.setText(book['leadAutor'])
                    self.edit_form_ui.lineNumPag.setText(str(book['numPages']))
                    self.edit_form_ui.dateEdit.setDate(QtCore.QDate(int(book['pubDate'].split('/')[2]), int(book['pubDate'].split('/')[1]), int(book['pubDate'].split('/')[0])))

                    self.QtStack.setCurrentIndex(4)

                    self.edit_ui.lineEdit.setText('')
                else:
                    self.edit_ui.messageBox("ISBN não encontrado!", "Erro")
            except:
                self.edit_ui.messageBox("O ISBN é um campo de números! Tente novamente!", "Erro")

    def OpenEditFormWindows(self):
        self.edit_form_ui.lineTitulo.setText(self.read_ui.book['title'])
        self.edit_form_ui.lineISBN.setText(str(self.read_ui.book['ISBN']))
        self.edit_form_ui.lineAutor.setText(self.read_ui.book['leadAutor'])
        self.edit_form_ui.lineNumPag.setText(str(self.read_ui.book['numPages']))
        print(self.read_ui.book['pubDate'])
        self.edit_form_ui.dateEdit.setDate(QtCore.QDate(int(self.read_ui.book['pubDate'].split('/')[2]), int(self.read_ui.book['pubDate'].split('/')[1]), int(self.read_ui.book['pubDate'].split('/')[0])))

        self.QtStack.setCurrentIndex(4)

    def OpenBuscarWindow(self):
        self.QtStack.setCurrentIndex(5)

    def OpenReadWindow(self):
        self.read_ui.book = PC.pc.searchBook_ISBN(self.search_ui.lineEdit.text())
        self.read_ui.UpdateTable()
        self.QtStack.setCurrentIndex(6)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())