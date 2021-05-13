from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import mysql.connector
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import Sql

def Connect(item_type):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    select_item = "SELECT * FROM item"
    cursor.execute(select_item)
    result = cursor.fetchall()
    items = []
    for row in result:
        if row[5] == item_type:
            items.append(row)
    db.close()
    return items
    
    

class Store(QWidget):
    def __init__(self, item_type):
        QWidget.__init__(self)
        self.type = item_type
        self.items = Connect(item_type)
        self.vbox = QVBoxLayout()
        for item in self.items:
            self.addItem(item)
        self.setLayout(self.vbox)

    def addItem(self, item):
        hbox = QHBoxLayout()
        product_vbox = QVBoxLayout()
        product_name = QLabel(item[1])
        product_description = QLabel(item[4])
        product_image = QLabel()

        product_image.setMaximumSize(QtCore.QSize(200, 200))
        product_image.setStyleSheet("")
        product_image.setText("")
        product_image.setPixmap(QtGui.QPixmap(str(item[0]) + ".jpg"))
        product_image.setScaledContents(True)
        product_image.setObjectName(str(item[0]))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(product_image.sizePolicy().hasHeightForWidth())
        product_image.setSizePolicy(sizePolicy)
        
        product_manufacturer = QLabel(item[3])
        hbox.addWidget(product_image)
        product_vbox.addWidget(product_name)
        product_vbox.addWidget(product_description)
        product_vbox.addWidget(product_manufacturer)
        product_vbox.addWidget(QLabel("$" + str(item[2])))
        hbox.addLayout(product_vbox)

        #Button to add to the Shopping Cart
        Purchase_Btn = QPushButton("Purchase")
        Purchase_Btn.clicked.connect(partial(self.insertToShoppingCart, item[0]))
        
        hbox.addWidget(Purchase_Btn)
        self.vbox.addLayout(hbox)

    def setStack(self, stack):
        self.stack = stack

    def insertToShoppingCart(self, item_id):
        if self.stack.pages['pbMenu'].getLoggedIn() == True:
            if self.stack.pages['pbMenu'].getUser()[1] == 'Customer':
                customer_id = self.stack.pages['pbMenu'].getUser()[0][0]
                db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
                cursor = db.cursor()
                try:
                    Sql.insertToShoppingCart(cursor, item_id, customer_id)
                    db.commit()
                    db.close()
                    msg = QMessageBox()
                    msg.setText("Item Added to Cart")
                    msg.setWindowTitle("Shopping Cart")
                    msg.setStandardButtons(QMessageBox.Close)
                    msg.exec()
                except Exception as e:
                    print(f"Error in 'insertToShoppingCart': {e}\n")
            else:
                print("This user has no shopping cart")
        else:
            print("Only Registered Users can add items to shopping cart")

