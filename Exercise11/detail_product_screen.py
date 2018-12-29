from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fake_data import *
class DetailProductScreen:
    def __init__(self, screen_type, product_screen):
        super().__init__()
        self.screen_type = screen_type
        self.product_screen = product_screen
        self.initUI()
        self.fetch_data_to_ui()
    def initUI(self):
        self.window = QWidget()
        self.window.resize(300,200)
        if self.screen_type == 'insert':
            self.title = 'Add new product'
        elif self.screen_type == 'update':
            self.title = 'Edit a product'
        self.window.setWindowTitle(self.title)
        grid = QGridLayout()
        grid.setSpacing(10)
        lblTitle = QLabel('Name')
        self.nameEdit = QLineEdit()
        grid.addWidget(lblTitle, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        lblYear = QLabel('Year')
        self.yearEdit = QLineEdit()
        grid.addWidget(lblYear, 2, 0)
        grid.addWidget(self.yearEdit, 2, 1)
        lblCompany = QLabel('Company')
        self.companyEdit = QLineEdit()
        grid.addWidget(lblCompany, 3, 0)
        grid.addWidget(self.companyEdit, 3, 1)
        lblCategory = QLabel('Category')
        self.categoryEdit = QLineEdit()
        grid.addWidget(lblCategory, 4, 0)
        grid.addWidget(self.categoryEdit, 4, 1)
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.on_save)
        grid.addWidget(saveButton, 5, 0)
        self.window.setLayout(grid)
        self.window.show()
    def fetch_data_to_ui(self):
        if(self.screen_type == 'insert'):
            self.detail_product = {'name': '', 'year': '', 'company':'', 'category': ''}
        elif (self.screen_type == 'update'):
            self.detail_product = self.product_screen.get_selected_product()
        self.nameEdit.setText(self.detail_product['name'])
        if isinstance(self.detail_product['year'], str):
            self.yearEdit.setText(self.detail_product['year'])
        else:
            self.yearEdit.setText(str(self.detail_product['year']))
        self.companyEdit.setText(self.detail_product['company'])
        self.categoryEdit.setText(self.detail_product['category'])
    def on_save(self):
        # alert = QMessageBox()
        # alert.setText('You clicked Add')
        # alert.exec_()
        self.detail_product['name'] = self.nameEdit.text()
        self.detail_product['year'] = self.yearEdit.text()
        self.detail_product['company'] = self.companyEdit.text()
        self.detail_product['category'] = self.categoryEdit.text()
        if(self.screen_type == 'insert'):
            self.product_screen.insert_product(self.detail_product)
        elif(self.screen_type == 'update'):
            self.product_screen.update_product(self.detail_product)
        self.window.close()
    def to_string(self):
        pass