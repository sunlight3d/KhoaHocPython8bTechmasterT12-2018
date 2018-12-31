from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from fake_data import *
from functools import partial
from detail_product_screen import DetailProductScreen
from database import Database
products = []
categories = ["All","Technology", "Foods", "Drinking", "Fashion"]
class ProductScreen:
    def __init__(self,):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.window = QWidget()
        self.window.resize(700,400)
        self.window.setWindowTitle('List of products')
        vbox = QVBoxLayout()
        self.comboBox = QComboBox()
        for category in categories:
            self.comboBox.addItem(category)        
        self.comboBox.currentIndexChanged.connect(self.comboBoxChange)
        self.hbox = QHBoxLayout()
        self.label_select_category = QLabel()
        self.label_select_category.setText('Select a category: ')
        self.hbox.addWidget(self.label_select_category)
        self.hbox.addWidget(self.comboBox)
        self.hbox.addStretch(1)
        self.btn_add_product = QPushButton('Add new Product')
        self.hbox.addWidget(self.btn_add_product)
        self.btn_add_product.clicked.connect(self.on_add_product)
        self.hbox.addStretch(9)
        vbox.addLayout(self.hbox)
        self.tableWidget = QTableWidget()
        self.tableWidget.setHorizontalHeaderLabels(["Tên", "Năm SX", "Công ty", "Thể loại"])
        self.tableWidget.horizontalHeader().setFixedHeight(40)
        self.reloadData()
        for i in range(0,6):
            self.tableWidget.setColumnWidth(i, self.tableWidget.width() / 6)
        self.tableWidget.move(0,0)
        vbox.addWidget(self.tableWidget)
        self.window.setLayout(vbox)
        self.window.show()
    def fetch_data_to_table(self, table_data):
        self.tableWidget.setRowCount(len(table_data))
        self.tableWidget.setColumnCount(4 + 2)
        for rowId in range(0, len(table_data)):
            product = table_data[rowId]
            self.tableWidget.setRowCount(len(table_data))
            self.tableWidget.setColumnCount(4 + 2)
            self.tableWidget.setItem(rowId,0, QTableWidgetItem(product["name"]))
            self.tableWidget.setItem(rowId,1, QTableWidgetItem(str(product["year"])))
            self.tableWidget.setItem(rowId,2, QTableWidgetItem(product["company"]))
            self.tableWidget.setItem(rowId,3, QTableWidgetItem(product["category"]))            
            
            btn_edit_product = QPushButton('Edit')
            btn_edit_product.setStyleSheet("background-color: aquamarine ")
            btn_edit_product.clicked.connect(partial(self.on_edit_product, product["id"]))
            self.tableWidget.setCellWidget(rowId,4, btn_edit_product)
            
            btn_delete_product = QPushButton('Delete')
            btn_delete_product.setStyleSheet("background-color: red")
            btn_delete_product.clicked.connect(partial(self.on_delete_product, product["id"]))

            self.tableWidget.setCellWidget(rowId,5, btn_delete_product)
    def reloadData(self):
        products = Database.getInstance().get_all_products()
        self.current_category = self.comboBox.currentText()
        if (self.current_category == 'All'):
            self.fetch_data_to_table(products)
        else:
            filtered_products = []
            for product in products:
                if(product["category"] == self.current_category):
                    filtered_products.append(product)
            self.fetch_data_to_table(filtered_products)
    def comboBoxChange(self):
        self.reloadData()
    def on_add_product(self):
        self.detail_product_screen = DetailProductScreen('insert',self)
    def on_edit_product(self, productId):        
        self.selectedId = productId
        self.detail_product_screen = DetailProductScreen('update',self)
    def on_delete_product(self, rowId):
        buttonReply = QMessageBox.question(self.window, 'Confirmation', "Do you want to delete this ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.delete_product(rowId)
            self.fetch_data_to_table(products)
    #insert, update, delete a product
    def insert_product(self, new_product):
        Database.getInstance().insert_new_product(new_product)        
        self.reloadData()
    def update_product(self, updated_product):
        Database.getInstance().update_product(productId, updated_product)                
        self.reloadData()
    def delete_product(self, productId):
        Database.getInstance().update_product(productId, updated_product)                
        self.reloadData()
    def get_selected_product(self):
        return Database.getInstance().get_product_from_id(self.selectedId)
    def to_string(self):
        pass