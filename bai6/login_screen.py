from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fake_data import *
from product_screen import ProductScreen
class LoginScreen:
    def __init__(self,):
        super().__init__()    
        self.initUI()
    
    def initUI(self):
        self.window = QWidget()    
        self.window.resize(300,200)
        self.window.setWindowTitle('Login Screen')
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)

        #anh
        self.label_logo = QLabel()        
        self.label_logo.resize(50, 50)
        self.pixmap = QPixmap('./logo.jpeg')
        self.pixmap = self.pixmap.scaledToWidth(64)
        self.label_logo.setPixmap(self.pixmap)
        #Tao ra HBox chua pixmap
        self.hbox = QHBoxLayout()
        self.hbox.setAlignment(Qt.AlignCenter)            
        self.hbox.addWidget(self.label_logo)
        
        self.layout.setAlignment(Qt.AlignCenter)            
        self.layout.addLayout(self.hbox)
        
        self.txtEmail = QLineEdit()            
        self.txtEmail.setPlaceholderText('Enter email')
        self.layout.addWidget(self.txtEmail)

        self.txtPassword = QLineEdit()
        self.txtPassword.setPlaceholderText('Enter password')
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.txtPassword)

        self.buttonLogin = QPushButton('Login')

        QShortcut(Qt.Key_Return, self.window).activated.connect(self.on_login_clicked)
        self.buttonLogin.clicked.connect(self.on_login_clicked)
        self.layout.addWidget(self.buttonLogin)

        self.window.setLayout(self.layout)

        self.txtEmail.setText('hoang123@gmail.com')
        self.txtPassword.setText('123456')

        self.window.show()
        
    def on_login_clicked(self):
        # alert = QMessageBox()
        # alert.setText('You clicked Login!')
        # alert.exec_()
        if(self.login_user()):
            # alert = QMessageBox()
            # alert.setText('Dang nhap thanh cong')
            # alert.exec_()
            self.window.close()
            self.product_screen = ProductScreen()
        else:
            alert = QMessageBox()
            alert.setText('Wrong email and password')
            alert.exec_()

    def login_user(self):
        email = self.txtEmail.text().strip()
        password = self.txtPassword.text().strip()
        for fake_user in fake_users:
            if(fake_user['email'] == email and fake_user['password'] == password):
                return True
        return False
