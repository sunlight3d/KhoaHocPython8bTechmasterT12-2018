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
        self.comboBox = QComboBox(self)
        for fake_category in fake_categories:
            self.comboBox.addItem(fake_category)
        vbox.addWidget(self.comboBox)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(fake_products))
        self.tableWidget.setColumnCount(4)
        for rowId in range(0, len(fake_products)):
            self.tableWidget.setItem(rowId,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.move(0,0)
        vbox.addWidget(self.tableWidget)
        # self.window.setLayout(self.layout)
        self.window.show()
    def on_login_clicked(self):
        alert = QMessageBox()
        alert.setText('You clicked Login!')
        alert.exec_()
    def to_string(self):
        pass
            