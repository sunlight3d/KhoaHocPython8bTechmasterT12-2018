"""
DROP TABLE pythontutorial.users;
CREATE TABLE IF NOT EXISTS pythontutorial.users (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            email VARCHAR(50),
            password VARCHAR(50),
            created_date TIMESTAMP);
INSERT INTO pythontutorial.users(name,email,password) VALUES('Hoang', 'hoang123@gmail.com', '123456');
SELECT * FROM pythontutorial.users;
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from product_screen import ProductScreen
from fake_data import *
from database import Database
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
        self.hbox = QHBoxLayout()
        self.hbox.setAlignment(Qt.AlignCenter)
        self.label_logo = QLabel()
        self.label_logo.resize(50, 50)
        pixmap = QPixmap('logo.png')
        pixmap = pixmap.scaledToWidth(64)
        self.label_logo.setPixmap(pixmap)
        self.hbox.addWidget(self.label_logo)
        self.txtEmail = QLineEdit()
        self.txtEmail.setPlaceholderText('Enter email')
        self.txtPassword = QLineEdit()
        self.txtPassword.setPlaceholderText('Enter password')
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtEmail.setText('hoang123@gmail.com')
        self.txtPassword.setText('123456')
        self.buttonLogin = QPushButton('Login')
        self.buttonLogin.clicked.connect(self.on_login_clicked)
        # self.buttonLogin.setFixedSize(QSize(100, 30))
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addLayout(self.hbox)
        self.layout.addWidget(self.txtEmail)
        self.layout.addWidget(self.txtPassword)
        self.layout.addWidget(self.buttonLogin)
        self.layout.addStretch(1)
        self.window.setLayout(self.layout)
        self.window.show()
        self.database = Database.getInstance()
    def on_login_clicked(self):
        # alert = QMessageBox()
        # alert.setText('You clicked Login!')
        # alert.exec_()
        if(self.login_user()):
            self.window.close()
            self.product_screen = ProductScreen()
        else:
            alert = QMessageBox()
            alert.setText('Wrong email and password')
            alert.exec_()
    def login_user(self):
        email = self.txtEmail.text().strip()
        password = self.txtPassword.text().strip()        
        return self.database.check_login(email, password)        
    def to_string(self):
        pass