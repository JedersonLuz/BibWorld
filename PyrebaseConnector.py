import pyrebase
import getpass 
import socket
import json

def InitializeApp():
    config = {
        "apiKey": "AIzaSyAo71Hcm_Wlpgi1nEjd_WSi4-4YCv3-ZZo",
        "authDomain": "bibworld-84e32.firebaseapp.com",
        "databaseURL": "https://bibworld-84e32.firebaseio.com",
        "projectId": "bibworld-84e32",
        "storageBucket": "bibworld-84e32.appspot.com",
        "messagingSenderId": "923704057508",
        "appId": "1:923704057508:web:1ff8ee30f1bb971c"
    }
    
    return pyrebase.initialize_app(config)


class PyrebaseConnector(object):
    def __init__(self):
        # Check if an internet connection is present
        self.is_connected()

        # Initialize Application Services
        self.firebase = InitializeApp()
        
        # Get a reference to the auth service
        self.auth = self.firebase.auth()

        # Get a reference to the database service
        self.db = self.firebase.database()

        # Get a reference to the storage service
        self.storage = self.firebase.storage()


    def is_connected(self, hostname="github.com"):
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(hostname)
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except Exception as e:
            print('NO_INTERNET_CONECTION')
            print('Try:')
            print('  Checking the network cables, modem, and router')
            print('  Reconnecting to Wi-Fi')
            exit(0)
        return False

    # Log the user in application
    def login(self, email, password):
        # email = input("Enter email: ")
        # password = getpass.getpass()

        try:
            self.user = self.auth.sign_in_with_email_and_password(email, password)
            return 'Ok'
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']

    # Create a user
    def signUp(self, email, password, displayName, dateBirth, gender):
        try:
            self.user = self.auth.create_user_with_email_and_password(email, password)
            data = {
                "displayName": displayName,
                'dateBirth': dateBirth,
                'gender': gender,
            }
            self.db.child("users").child(self.user['localId']).set(data)
            return 'Ok'
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']
    
    def updateUser(self, displayName, dateBirth, gender):
        data = {
            "displayName": displayName,
            'dateBirth': dateBirth,
            'gender': gender,
        }
        # print(self.auth.current_user['localId'])
        self.db.child('users').child(self.auth.current_user['localId']).update(data)

    def changePassword(self, email):
        try:
            self.auth.send_password_reset_email(email)
        except Exception as e:
            print(e)

    # Register a book in database
    def createBook(self, ISBN, title, leadAuthor, numPages, pubDate, pathImg):
        self.storage.child('images/books/'+str(ISBN)).put(pathImg)

        data = {
            'ISBN': ISBN,
            'title': title,
            'leadAutor': leadAuthor,
            'numPages': numPages,
            'pubDate': pubDate,
            'pathImg': 'images/books/'+str(ISBN),
        }
        self.db.child('books').child(ISBN).set(data)

        print('Livro cadastrado!')

    # Update data from a book
    def updateBook(self, ISBN, title, leadAuthor, numPages, pubDate, pathImg):
        self.storage.child('images/books/'+str(ISBN)).put(pathImg)

        data = {
            'ISBN': ISBN,
            'title': title,
            'leadAutor': leadAuthor,
            'numPages': numPages,
            'pubDate': pubDate,
            'pathImg': 'images/books/'+str(ISBN),
        }
        self.db.child('books').child(ISBN).update(data)

    # Search for a book with ISBN
    def searchBook_ISBN(self, ISBN):
        book = self.db.child('books').child(ISBN).get()
        # print(book.val()['title'])
        # print(book.val())
        # print(type(book))
        return book.val()

    # Search for a book with Title
    def searchBook_title(self, title):
        book = self.db.child('books').child(title).get()
        print(book.val()['title'])
        return book.val()

    # Remove a book
    def removeBook(self, ISBN):
        if self.searchBook_ISBN(ISBN):
            self.db.child('books').child(ISBN).remove()
            return 1
        else:
            return 0
        

pc = PyrebaseConnector()

# pc.changePassword('jedersonalpha@gmail.com')

# pc.login('jedersonalpha@gmail.com', getpass.getpass())
# pc.updateUser('Jederson Sousa Luz', '18/02/1997', 'masculino')

# print(pc.signUp('vitoria@gmail.com', '123456', 'Vitória', '29/11/1999', 'feminino'))
# pc.createBook(9788576051428, 'Sistemas Distribuidos', 'Tanenbaum', 416, 3/8/2007, 'images/sistemas_distribuidos.jpeg')
# pc.updateBook(ISBN=9788544103166, title='Ready Player One', leadAuthor='Ernet Cline', numPages=464, pubDate='8/9/2018', pathImg='images/jogador_n_1.jpg')
# pc.removeBook(9788544103166)
# pc.searchBook_ISBN(9788544103166)