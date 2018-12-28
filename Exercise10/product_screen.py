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
        self.comboBox = QComboBox()
        for fake_category in fake_categories:
            self.comboBox.addItem(fake_category)        
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
        self.fetch_data_to_table(fake_products)
        for i in range(0,4):
            self.tableWidget.setColumnWidth(i, self.tableWidget.width() / 4)
        self.tableWidget.move(0,0)
        vbox.addWidget(self.tableWidget)
        self.window.setLayout(vbox)
        self.window.show()
    
    def fetch_data_to_table(self, table_data):
        self.tableWidget.setRowCount(len(table_data))
        self.tableWidget.setColumnCount(4)
        for rowId in range(0, len(table_data)):
            fake_product = table_data[rowId]
            self.tableWidget.setRowCount(len(table_data))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setItem(rowId,0, QTableWidgetItem(fake_product["name"]))
            self.tableWidget.setItem(rowId,1, QTableWidgetItem(str(fake_product["year"])))
            self.tableWidget.setItem(rowId,2, QTableWidgetItem(fake_product["company"]))            
            self.tableWidget.setItem(rowId,3, QTableWidgetItem(fake_product["category"]))

    def comboBoxChange(self, i):
        self.current_category = self.comboBox.currentText()
        if (self.current_category == 'All'):
            self.fetch_data_to_table(fake_products)
        else:
            filtered_products = []
            for fake_product in fake_products:
                if(fake_product["category"] == self.current_category):
                    filtered_products.append(fake_product)
            self.fetch_data_to_table(filtered_products)
    def on_add_product(self):
        alert = QMessageBox()
        alert.setText('You clicked Add')
        alert.exec_()    
    def to_string(self):
        pass
            