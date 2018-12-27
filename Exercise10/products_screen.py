from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class ProductScreen:	

	def __init__(self,):
		super().__init__()	
		self.initUI()

	def initUI(self):
		self.window = QWidget()	
		self.window.resize(550,300)		
		self.window.setWindowTitle('List of products')

		
		combo = QComboBox(self)

        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
		
		# self.window.setLayout(self.layout)
		self.window.show()
	
	def on_login_clicked(self):
		alert = QMessageBox()
		alert.setText('You clicked Login!')
		alert.exec_()
	
	def to_string(self):
		pass