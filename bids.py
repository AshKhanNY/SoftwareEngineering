from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit, QPushButton, QMessageBox

from Sql import getSignedIn, fetchFromDatabase
import mysql.connector

sql_password = "root"


def viewBids(cursor):
    return fetchFromDatabase(cursor, "bid")


def company_id_to_name(cursor):
    query = 'SELECT id, name FROM company WHERE type="D"'
    cursor.execute(query)
    return {id: username for id, username in cursor.fetchall()}


def test():
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    print(sorted(viewBids(cursor), key=lambda x: x[2], reverse=True))
    print(company_id_to_name(cursor))


test()

def message_box(message):
    msg = QMessageBox()
    msg.setText(message)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Close)
    msg.exec()

class Bids(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        self.cursor = self.db.cursor()

        self.vbox = QVBoxLayout()

        self.bids = sorted(viewBids(self.cursor), key=lambda x: x[2], reverse=True)

        # Helpers
        self.id_to_name = company_id_to_name(self.cursor)
        self.current_user = getSignedIn(self.cursor)


        for bid in self.bids:
            self.addBid(bid)

        self.makeBid()
        self.setLayout(self.vbox)

    def addBid(self, bid):
        hbox = QHBoxLayout()

        company_name = QLabel(self.id_to_name[bid[0]])
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        company_name.setFont(font)

        delivery = QLabel(str(bid[1]))
        font.setBold(False)
        delivery.setAlignment(Qt.AlignCenter)

        font.setPointSize(24)
        font.setBold(True)
        amount = QLabel("$" + str(bid[2]))
        amount.setFont(font)
        amount.setAlignment(Qt.AlignRight)

        hbox.addWidget(company_name)
        hbox.addWidget(delivery)
        hbox.addWidget(amount)

        self.vbox.addLayout(hbox)

    def makeBid(self):
        hbox = QHBoxLayout()

        company_name = QLabel(self.id_to_name[self.current_user[0]])

        choose_delivery_id = QTextEdit("Choose a delivery ID")
        choose_amount = QTextEdit("Choose a bidding amount!")

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(partial(self.add_bid_to_database, choose_delivery_id, choose_amount))

        hbox.addWidget(company_name)
        hbox.addWidget(choose_delivery_id)
        hbox.addWidget(choose_amount)
        hbox.addWidget(submit_button)

        self.vbox.addLayout(hbox)

    def add_bid_to_database(self, delivery, amount):
        try:
            delivery = int(delivery.toPlainText())
            amount = int(amount.toPlainText())
        except:
            message_box("Please only input valid numbers!")
            return
        self.castBid(delivery, amount)
        message_box("You have cast a bid! Hooray!")

    def castBid(self, delivery, amount):
        try:
            query = "INSERT INTO bid(company, delivery, amount) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (self.current_user[0], delivery, amount))
            self.db.commit()
            print("Added bid to database :)")
        except:
            print("Error adding bid to database")
