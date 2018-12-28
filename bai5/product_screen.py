from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fake_data import *

class ProductScreen:    
    def __init__(self,):
        super().__init__()    
        self.initUI()
    def initUI(self):
        self.window = QWidget()    
        self.window.resize(700,400)        
        self.window.setWindowTitle('List of products')
        vbox = QVBoxLayout()

        self.label_select_category = QLabel()
        self.label_select_category.setText('Select a category: ')

        self.comboBox = QComboBox()
        for fake_category in fake_categories:
            self.comboBox.addItem(fake_category)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label_select_category)
        self.hbox.addWidget(self.comboBox)
        
        vbox.addLayout(self.hbox)
        self.window.setLayout(vbox)
        
        self.window.show()