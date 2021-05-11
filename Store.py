from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import mysql.connector

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
        #product_image.setPixmap(QPixmap(item['image']))
        product_manufacturer = QLabel(item[3])
        hbox.addWidget(product_image)
        product_vbox.addWidget(product_name)
        product_vbox.addWidget(product_description)
        product_vbox.addWidget(product_manufacturer)
        product_vbox.addWidget(QLabel("$" + str(item[2])))
        hbox.addLayout(product_vbox)
        Purchase_Btn = QPushButton("Purchase")
        hbox.addWidget(Purchase_Btn)
        self.vbox.addLayout(hbox)

