from PyQt5.QtWidgets import *
import mysql.connector

Logged_In = False
user = {}
account_pages = {}

class Page(QWidget):
    def __init__(self, stack):
        QWidget.__init__(self)
        self.stack = stack
        self.stack.addWidget(self)

class StartPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"StartPage" : self})
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Parts Authority")
        if Logged_In:
            self.Logout = QPushButton("Logout")
            self.grid.addWidget(self.Logout, 0, 0)
        else:
            self.Login = QPushButton("Login")
            self.Login.clicked.connect(self.gotoLoginPage)
            self.Register = QPushButton("Register")
            self.Register.clicked.connect(self.gotoRegisterPage)
            self.grid.addWidget(self.Login, 0, 0)
            self.grid.addWidget(self.Register, 0, 1)
        self.vbox.addWidget(self.L1)
        self.vbox.addLayout(self.grid)
        self.setLayout(self.vbox)

    def gotoRegisterPage(self):
        self.stack.setCurrentWidget(account_pages["RegisterPage"])

    def gotoLoginPage(self):
        self.stack.setCurrentWidget(account_pages["LoginPage"])

class RegisterPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"RegisterPage" : self})
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Register")
        self.vbox.addWidget(self.L1)
        #Widgets for Registration Form
        self.UseCaseLabel = QLabel()
        self.UseCaseField = QComboBox()
        self.UseCaseField.addItems(["Customer", "Store Manager", "Store Clerk", "Computer Parts Company", "Delivery Company"])
        self.EmailLabel = QLabel("Email Address: ")
        self.EmailField = QLineEdit()
        self.PasswordLabel = QLabel("Password: ")
        self.PasswordField = QLineEdit()
        self.AddressLabel = QLabel("Delivery Address: ")
        self.AddressField = QLineEdit()
        self.form = QFormLayout()
        #Add Widgets to Form
        self.form.setWidget(0, QFormLayout.LabelRole, self.UseCaseLabel)
        self.form.setWidget(0, QFormLayout.FieldRole, self.UseCaseField)
        self.form.setWidget(1, QFormLayout.LabelRole, self.EmailLabel)
        self.form.setWidget(1, QFormLayout.FieldRole, self.EmailField)
        self.form.setWidget(2, QFormLayout.LabelRole, self.PasswordLabel)
        self.form.setWidget(2, QFormLayout.FieldRole, self.PasswordField)
        self.form.setWidget(3, QFormLayout.LabelRole, self.AddressLabel)
        self.form.setWidget(3, QFormLayout.FieldRole, self.AddressField)
        self.formWidget = QWidget()
        self.formWidget.setLayout(self.form)
        self.vbox.addWidget(self.formWidget)
        self.buttonLayout = QHBoxLayout()
        self.registerButton = QPushButton("Register")
        self.registerButton.clicked.connect(self.register_msg)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.gotoStartPage)
        self.buttonLayout.addWidget(self.registerButton)
        self.buttonLayout.addWidget(self.cancelButton)
        self.vbox.addLayout(self.buttonLayout)
        self.setLayout(self.vbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])

    def register(self, response):
        global Logged_In
        if response.text() == "OK":
            user.update({"email" : self.EmailField.text(),
                     "password": self.PasswordField.text(),
                     "address" : self.AddressField.text(),
                     "user_type" : self.UseCaseField.currentText()})
            Logged_In = True
            StartPage(self.stack)
            self.gotoStartPage()

    def register_msg(self):
        msg = QMessageBox()
        msg.setText("Are you sure you want to register with the following information?")
        msg.setWindowTitle("Register New User")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.register)
        msg.exec()

class LoginPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"LoginPage" : self})
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Login")
        self.vbox.addWidget(self.L1)
        self.form = QFormLayout()
        self.UseCaseLabel = QLabel()
        self.UseCaseField = QComboBox()
        self.UseCaseField.addItems(["Customer", "Store Manager", "Store Clerk", "Computer Parts Company", "Delivery Company"])
        self.EmailLabel = QLabel("Email Address: ")
        self.EmailField = QLineEdit()
        self.PasswordLabel = QLabel("Password: ")
        self.PasswordField = QLineEdit()
        self.form.setWidget(0, QFormLayout.LabelRole, self.UseCaseLabel)
        self.form.setWidget(0, QFormLayout.FieldRole, self.UseCaseField)
        self.form.setWidget(1, QFormLayout.LabelRole, self.EmailLabel)
        self.form.setWidget(1, QFormLayout.FieldRole, self.EmailField)
        self.form.setWidget(2, QFormLayout.LabelRole, self.PasswordLabel)
        self.form.setWidget(2, QFormLayout.FieldRole, self.PasswordField)
        self.vbox.addLayout(self.form)
        self.buttonLayout = QHBoxLayout()
        self.loginButton = QPushButton("Login")
        #self.loginButton.clicked.connect(self.login)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.gotoStartPage)
        self.buttonLayout.addWidget(self.loginButton)
        self.buttonLayout.addWidget(self.cancelButton)
        self.vbox.addLayout(self.buttonLayout)
        self.setLayout(self.vbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])

    def login(self):
        db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
        cursor = db.cursor()
        if self.UseCaseField.currentText() == "Customer":
            select_user = "SELECT * FROM customer"
            cursor.execute(select_user)
            result = cursor.fetchall()
        elif self.UseCaseField.currentText() == "Store Manager":
            select_user = "SELECT * FROM admin"
            cursor.execute(select_user)
            result = cursor.fetchall()
        elif self.UseCaseField.currentText() == "Store Clerk":
            select_user = "SELECT * FROM clerk"
            cursor.execute(select_user)
            result = cursor.fetchall()
        else:
            select_user = "SELECT * FROM company"
            cursor.execute(select_user)
            result = cursor.fetchall()
        db.close()

class Account(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.account_stack = QStackedLayout()
        self.Start_Page = StartPage(self.account_stack)
        self.Register_Page = RegisterPage(self.account_stack)
        self.Login_Page = LoginPage(self.account_stack)
        self.setLayout(self.account_stack)
        

