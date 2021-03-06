from PyQt5.QtWidgets import QWidget, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

import mysql.connector

from Sql import fetchFromDatabase
from bids import message_box

username_to_id = {}

def get_all_users(cursor):
    users = []
    for database_name in ["Customer", "Company", "Clerk"]:
        query = "SELECT id, name FROM " + database_name.lower()
        cursor.execute(query)
        for id, username in cursor.fetchall():
            users.append(username)
            username_to_id[username] = id
    return users

def test():
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()

    print(get_all_users(cursor))
    #print(username_to_id)

    text = "I do not like you"
    user_type_selected = "Customer".lower()
    username = "Echo"
    count = fetchFromDatabase(cursor, user_type_selected + "report", "num_reported",
                              user_type_selected + f"_id={username_to_id[username]}")
    if not count:
        query = f"INSERT INTO {user_type_selected}report VALUES(%s, %s, %s)"
        cursor.execute(query, (username_to_id[username], "1", text))
    else:
        query = f"UPDATE {user_type_selected}report SET num_reported={count[0][0] + 1} WHERE {user_type_selected}_id={username_to_id[username]}"
        cursor.execute(query)
    db.commit()

# test()

class Complain(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
        self.cursor = self.db.cursor()

        self.vertical_layout = QVBoxLayout()
        self.horizontal_selectors = QHBoxLayout()

        self.prompt = QLabel("Please enter a detailed report about the user you want to report")
        self.user_types = ["Customer", "Company", "Clerk"]
        self.select_user_type = QComboBox()
        self.select_user_type.addItems(self.user_types)

        self.select_user = QComboBox()
        self.select_user.addItems(get_all_users(self.cursor))

        self.horizontal_selectors.addWidget(self.select_user_type)
        self.horizontal_selectors.addWidget(self.select_user)

        self.input_field = QTextEdit("Add a description here!")
        self.submit_complaint = QPushButton("Submit")
        self.submit_complaint.clicked.connect(self.post_in_database)


        self.vertical_layout.addLayout(self.horizontal_selectors)
        self.vertical_layout.addWidget(self.prompt)
        self.vertical_layout.addWidget(self.input_field)
        self.vertical_layout.addWidget(self.submit_complaint)

        self.setLayout(self.vertical_layout)

    def post_in_database(self):
        text = self.input_field.toPlainText()
        user_type_selected = self.select_user_type.currentText().lower()
        username = self.select_user.currentText()
        count = fetchFromDatabase(self.cursor, user_type_selected + "report", "num_reported",
                                  user_type_selected + f"_id={username_to_id[username]}")
        if not count:
            query = f"INSERT INTO {user_type_selected}report VALUES(%s, %s, %s)"
            self.cursor.execute(query, (username_to_id[username], "1", text))
        else:
            query = f"UPDATE {user_type_selected}report SET num_reported={count[0][0] + 1} WHERE {user_type_selected}_id={username_to_id[username]}"
            self.cursor.execute(query)
        self.db.commit()
        message_box("Your complaint has been successfully sent!")
