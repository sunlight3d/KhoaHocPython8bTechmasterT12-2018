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
        try:
            currentComboIndex = fake_categories[1:].index(self.detail_product['category'])
            self.comboBox.setCurrentIndex(currentComboIndex)
        except ValueError:
            self.comboBox.setCurrentIndex(0)
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
        grid.addWidget(lblTitle, 1, 0) #Hang 1, cot 0
        grid.addWidget(self.nameEdit, 1, 1) #Hang 1, cot 1

        lblYear = QLabel('Year')
        self.yearEdit = QLineEdit()
        grid.addWidget(lblYear, 2, 0) #Hang 2, cot 0
        grid.addWidget(self.yearEdit, 2, 1)#Hang 2, cot 1

        lblCompany = QLabel('Company')
        self.companyEdit = QLineEdit()
        grid.addWidget(lblCompany, 3, 0)
        grid.addWidget(self.companyEdit, 3, 1)
        lblCategory = QLabel('Category')
        self.comboBox = QComboBox()
        for fake_category in fake_categories[1:]:
            self.comboBox.addItem(fake_category)
        grid.addWidget(lblCategory, 4, 0)
        grid.addWidget(self.comboBox, 4, 1)

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.on_save)
        grid.addWidget(saveButton, 5, 0)

        self.window.setLayout(grid)
        self.window.show()

    def on_save(self):
        self.detail_product = {'name':'', 'year': 0, 'company':'', 'category':''}
        self.detail_product['name'] = self.nameEdit.text().strip()
        self.detail_product['year'] = self.yearEdit.text().strip()
        self.detail_product['company'] = self.companyEdit.text().strip()
        self.detail_product['category'] = self.comboBox.currentText()
        if(self.screen_type == 'insert'):
            self.product_screen.insert_product(self.detail_product)
        elif(self.screen_type == 'update'):
            self.product_screen.update_product(self.detail_product)
        self.window.close()