from PyQt5.QtWidgets import *
from login_screen import LoginScreen
app = QApplication([])
app.setStyle('Fusion')
login_screen = LoginScreen()
app.exec_()