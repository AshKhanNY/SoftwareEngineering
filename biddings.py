from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

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


#test()

class Biddings(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        self.cursor = self.db.cursor()

        self.bids = sorted(viewBids(self.cursor), key=lambda x: x[2], reverse=True)

        # Helpers
        self.id_to_name = company_id_to_name(self.cursor)
        self.current_user = getSignedIn(self.cursor)

        self.vbox = QVBoxLayout()
        for bid in self.bids:
            self.addBid(bid)

        self.setLayout(self.vbox)

    def addBid(self, bid):
        hbox = QHBoxLayout()

        company_name = QLabel(self.id_to_name(bid[0]))
        delivery_id = QLabel(bid[1])
        bid_amount = QLabel(bid[2])

        hbox.addWidget(company_name)
        hbox.addWidget(delivery_id)
        hbox.addWidget(bid_amount)

        self.vbox.addLayout(hbox)