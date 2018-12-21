from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from login_screen import LoginScreen

app = QApplication([])
app.setStyle('Fusion')
login_screen = LoginScreen()
app.exec_()
