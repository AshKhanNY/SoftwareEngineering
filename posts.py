from functools import partial

import mysql.connector
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSizePolicy, QTextEdit


def get_posts(cursor):
    query = "SELECT * FROM post"
    cursor.execute(query)
    return cursor.fetchall()


def get_replies(cursor):
    query = "SELECT * FROM reply"
    cursor.execute(query)
    return cursor.fetchall()


def replace_id_with_username(cursor, posts):
    query = "SELECT id, name FROM customer"
    cursor.execute(query)
    usernames = cursor.fetchall()

    array = []
    for post in posts:
        id = post[1]
        for username in usernames:
            if username[0] == id:
                array.append((username[1], post[2]))
    return array


def format_replies(cursor, replies):
    query = "SELECT id, name FROM customer"
    cursor.execute(query)
    usernames = cursor.fetchall()

    array = []
    for reply in replies:
        id, reply_id = reply[1], reply[2]
        author, reply_to = "", ""
        for username in usernames:
            if username[0] == id:
                author = username[1]
            elif username[0] == reply_id:
                reply_to = username[1]
        array.append((author, reply_to, reply[3]))
    return array


def add_post(author_id, content):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    query = "INSERT INTO post(author, content) VALUES(%s, %s)"
    try:
        cursor.execute(query, (author_id, content))
        print("Succesfully added a post")
    except:
        print("Error adding a post")
    db.commit()


def add_reply(author_id, reply_to_id, content):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    query = "INSERT INTO reply(author, thread, content) VALUES(%s, %s, %s)"
    try:
        cursor.execute(query, (author_id, reply_to_id, content))
        print("Succesfully replied to a post")
    except:
        print("Error adding a reply")
    db.commit()


def remove_replies(thread_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    query = f"DELETE FROM reply WHERE thread = \'{thread_id}\';"
    cursor.execute(query, thread_id)
    db.commit()


def remove_posts_from_author(author_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    query = f"DELETE FROM post WHERE author = \'{author_id}\';"
    cursor.execute(query, author_id)
    db.commit()


def test():
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    print(replace_id_with_username(cursor, sorted(get_posts(cursor), key=lambda x: x[1])))
    print(format_replies(cursor, sorted(get_replies(cursor), key=lambda x: x[2])))


test()


class Posts(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
        self.cursor = self.db.cursor()

        self.vbox = QVBoxLayout()

        self.posts = replace_id_with_username(self.cursor, sorted(get_posts(self.cursor), key=lambda x: x[1]))
        self.replies = format_replies(self.cursor, sorted(get_replies(self.cursor), key=lambda x: x[2]))

        # Possibly Update this so that replies go under specific posts
        for post in self.posts:
            self.addPost(post)
            # Get all of the replies with the same post author
            replies_to_post = list(filter(lambda x: x[1] == post[0], self.replies))
            for reply in replies_to_post:
                self.addReply(reply)

        self.writePost()

        self.setLayout(self.vbox)

    def addPost(self, post):
        hbox = QHBoxLayout()

        username = QLabel(post[0])
        font = QFont()
        font.setBold(True)
        username.setFont(font)

        content = QLabel(post[1])
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(content.sizePolicy().hasHeightForWidth())
        content.setSizePolicy(size_policy)

        font.setPointSize(12)
        font.setBold(False)
        content.setFont(font)

        # Add Reply Functionality
        reply_button = QPushButton("Reply")
        reply_button.setFixedSize(50, 20)

        # Add Report Functionality
        report_button = QPushButton("Report")
        report_button.setFixedSize(50, 20)

        hbox.addWidget(username)
        hbox.addWidget(content)
        hbox.addWidget(reply_button)
        hbox.addWidget(report_button)

        self.vbox.addLayout(hbox)

    def addReply(self, reply):
        hbox = QHBoxLayout()

        username = QLabel(reply[0])
        font = QFont()
        font.setBold(True)
        username.setFont(font)

        reply_to = QLabel("replying to " + reply[1] + ":")

        content = QLabel(reply[2])
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(content.sizePolicy().hasHeightForWidth())
        content.setSizePolicy(size_policy)

        font.setPointSize(12)
        font.setBold(False)
        content.setFont(font)

        # Add Report Functionality
        report_button = QPushButton("Report")
        report_button.setFixedSize(50, 20)

        hbox.addWidget(username)
        hbox.addWidget(reply_to)
        hbox.addWidget(content)
        hbox.addWidget(report_button)

        self.vbox.addLayout(hbox)

    def writePost(self):
        hbox = QHBoxLayout()

        hbox = QHBoxLayout()

        username = QLabel("You")
        font = QFont()
        font.setBold(True)
        username.setFont(font)

        content = QTextEdit("Add a description!")
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(content.sizePolicy().hasHeightForWidth())
        content.setSizePolicy(size_policy)

        font.setPointSize(12)
        font.setBold(False)
        content.setFont(font)

        # Add Report Functionality
        submit_button = QPushButton("Submit")
        submit_button.setFixedSize(50, 20)

        hbox.addWidget(username)
        hbox.addWidget(content)

        hbox.addWidget(submit_button)
        submit_button.clicked.connect(partial(self.add_post_to_database, content.toPlainText()))

        self.vbox.addLayout(hbox)

    def add_post_to_database(self, text):
        taboo_list = ["beans", "fruit", "orange"]
        for word in taboo_list:
            if word in text:
                text = text.replace(word, "CENSORED")
        print(text)
