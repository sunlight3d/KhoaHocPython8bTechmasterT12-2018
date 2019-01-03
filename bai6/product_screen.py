from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from fake_data import *
from detail_product_screen import DetailProductScreen
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
        self.comboBox.currentIndexChanged.connect(self.comboBoxChange)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label_select_category)
        self.hbox.addWidget(self.comboBox)

        self.btn_add_product = QPushButton('Add new Product')
        self.hbox.addWidget(self.btn_add_product)
        self.btn_add_product.clicked.connect(self.on_add_product)
        self.hbox.addStretch(9)
        
        vbox.addLayout(self.hbox)
        self.tableWidget = QTableWidget()
        self.tableWidget.setHorizontalHeaderLabels(["Tên", "Năm SX", "Công ty", "Thể loại"])
        self.tableWidget.horizontalHeader().setFixedHeight(40)
        self.tableWidget.move(0,0)
        vbox.addWidget(self.tableWidget)
        self.window.setLayout(vbox)
        self.fetch_data_to_table(fake_products)
        self.window.show()
    def on_add_product(self):
        self.detail_product_screen = DetailProductScreen('insert',self)
    def fetch_data_to_table(self, table_data):
        self.tableWidget.setRowCount(len(table_data))
        self.tableWidget.setColumnCount(4 + 2)
        for rowId in range(0, len(table_data)):
            fake_product = table_data[rowId]
            self.tableWidget.setItem(rowId,0, QTableWidgetItem(fake_product["name"]))
            self.tableWidget.setItem(rowId,1, QTableWidgetItem(str(fake_product["year"])))
            self.tableWidget.setItem(rowId,2, QTableWidgetItem(fake_product["company"]))
            self.tableWidget.setItem(rowId,3, QTableWidgetItem(fake_product["category"]))

            btn_edit_product = QPushButton('Edit')
            btn_edit_product.setStyleSheet("background-color: aquamarine ")
            self.tableWidget.setCellWidget(rowId,4, btn_edit_product)
            btn_edit_product.clicked.connect(partial(self.on_edit_product, rowId))

            btn_delete_product = QPushButton('Delete')
            btn_delete_product.setStyleSheet("background-color: red")
            self.tableWidget.setCellWidget(rowId,5, btn_delete_product)

        for i in range(0,6):
            self.tableWidget.setColumnWidth(i, self.tableWidget.width() / 6)
    def insert_product(self, new_product):
        fake_products.append(new_product)
        self.reloadData()
    def on_edit_product(self, rowId):        
        self.selectedId = rowId
        self.detail_product_screen = DetailProductScreen('update',self)

    def update_product(self, updated_product):
        product = fake_products[self.selectedId]
        if(product is not None):
           product = updated_product
           self.reloadData()
    
    def comboBoxChange(self):
        self.reloadData()
    def reloadData(self):
        self.current_category = self.comboBox.currentText()
        if (self.current_category == 'All'):
            self.fetch_data_to_table(fake_products)
        else:
            filtered_products = []
            for fake_product in fake_products:
                if(fake_product["category"] == self.current_category):
                    filtered_products.append(fake_product)
            self.fetch_data_to_table(filtered_products)