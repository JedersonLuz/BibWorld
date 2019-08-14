import pyrebase
import getpass 
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
        # Initialize Application Services
        self.firebase = InitializeApp()
        
        # Get a reference to the auth service
        self.auth = self.firebase.auth()

        # Get a reference to the database service
        self.db = self.firebase.database()

        # Get a reference to the storage service
        self.storage = self.firebase.storage()


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
    def signUp(self, email, displayName, password):
        # email = input("Enter your email: ")
        # displayName = input('Enter your display name: ')
        # password = input("Enter your password: ")

        try:
            self.user = self.auth.create_user_with_email_and_password(email, password)
            data = {
                "displayName": displayName
            }
            self.db.child("users").child(self.user['localId']).set(data)
            return 'Ok'
        except Exception as e:
            _error_json = e.args[1]
            _error = json.loads(_error_json)['error']
            return _error['message']
    
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
        user = self.db.child('books').child(ISBN).get()
        print(user.val()['title'])
        print(user.val())
        return user.val()

    # Search for a book with Title
    def searchBook_title(self, title):
        user = self.db.child('books').child(title).get()
        print(user.val()['title'])
        return user.val()

    # Remove a book
    def removeBook(self, ISBN):
        self.db.child('books').child(ISBN).remove()

pc = PyrebaseConnector()
# pc.createBook(9788576051428, 'Sistemas Distribuidos', 'Tanenbaum', 416, 3/8/2007, 'images/sistemas_distribuidos.jpeg')
# pc.updateBook(ISBN=9788544103166, title='Ready Player One', leadAuthor='Ernet Cline', numPages=464, pubDate='8/9/2018', pathImg='images/jogador_n_1.jpg')
# pc.removeBook(9788544103166)
# pc.searchBook_ISBN(9788544103166)