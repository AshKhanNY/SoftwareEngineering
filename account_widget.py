from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import Sql
from functools import partial
import random

Logged_In = False
user = []
account_pages = {}
sql_password = "root"
db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
cursor = db.cursor()

class Page(QWidget):
    def __init__(self, stack):
        QWidget.__init__(self)
        self.stack = stack
        self.stack.addWidget(self)

class StartPage(Page):
    def __init__(self, stack):
        global user
        Page.__init__(self, stack)
        account_pages.update({"StartPage": self})
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Parts Authority")
        if Logged_In:
            self.L1.setText("Logged in as: " + user[0][1])
            self.Logout = QPushButton("Logout")
            self.Logout.clicked.connect(self.logout)
            self.grid.addWidget(self.Logout, 0, 0)
            # View Account Information
            if user[1] == "Customer":
                # Customer
                self.grid.addWidget(QLabel("Email Address: "), 1, 0)
                self.grid.addWidget(QLabel(user[0][2]), 1, 1)
                self.grid.addWidget(QLabel("View Your Shopping Cart"), 2, 0)
                self.grid.addWidget(QLabel("Track Your Deliveries"), 3, 0)
                self.shoppingCartBtn = QPushButton("My Shopping Cart")
                self.shoppingCartBtn.clicked.connect(self.gotoShoppingCart)
                self.trackerBtn = QPushButton("Track Deliveries")
                self.trackerBtn.clicked.connect(self.gotoDeliveries)
                self.grid.addWidget(self.shoppingCartBtn, 2, 1)
                self.grid.addWidget(self.trackerBtn, 3, 1)
                # self.grid.addWidget(QLabel("File a Complaint"), 4, 0)
                # self.ComplainBtn = QPushButton("Complain")
                # self.grid.addWidget(self.ComplainBtn, 4, 1)
            elif user[1] == "Store Manager":
                # Admin
                self.grid.addWidget(QLabel("View Taboo List"), 1, 0)
                self.ViewTabooBtn = QPushButton("Taboo List")
                self.ViewTabooBtn.clicked.connect(partial(self.View, "taboo"))
                self.grid.addWidget(self.ViewTabooBtn, 1, 1)
                self.grid.addWidget(QLabel("Edit Taboo List"), 2, 0)
                self.AddTabooBtn = QPushButton("Add")
                self.DeleteTabooBtn = QPushButton("Delete")
                self.grid.addWidget(self.AddTabooBtn, 2, 2)
                self.grid.addWidget(self.DeleteTabooBtn, 2, 3)
                self.TabooLine = QLineEdit()
                self.grid.addWidget(self.TabooLine, 2, 1)
                self.AddTabooBtn.clicked.connect(self.insertTabooWord)
                self.DeleteTabooBtn.clicked.connect(self.deleteTabooWord)
                self.grid.addWidget(QLabel("View Ban List"), 3, 0)
                self.ViewBanBtn = QPushButton("Ban List")
                self.ViewBanBtn.clicked.connect(partial(self.View, "blacklist"))
                self.grid.addWidget(self.ViewBanBtn, 3, 1)
                self.grid.addWidget(QLabel("Edit Blacklist"), 4, 0)
                self.BlackListLine = QLineEdit()
                self.grid.addWidget(self.BlackListLine, 4, 1)
                self.BanBtn = QPushButton("Ban User")
                self.grid.addWidget(self.BanBtn, 4, 2)
                self.unBanBtn = QPushButton("Unban User")
                self.grid.addWidget(self.unBanBtn, 4, 3)
                self.viewRequestsBtn = QPushButton("Requests")
                self.grid.addWidget(self.viewRequestsBtn, 5, 1)
                self.grid.addWidget(QLabel("View Requests"), 5, 0)
                # self.grid.addWidget(QLabel("View Complaints"), 5, 0)
                # self.ComplaintBtn = QPushButton("Complaints")
                # self.grid.addWidget(self.ComplaintBtn, 5, 1)
            elif user[1] == "Store Clerk":
                # Clerk
                self.grid.addWidget(QLabel("Choose Delivery Companies"), 1, 0)
                self.bidBtn = QPushButton("View Bids")
                self.bidBtn.clicked.connect(partial(self.View, "bid"))
                self.grid.addWidget(self.bidBtn, 1, 1)
            elif user[1] == "Delivery Company":
                # Delivery Company
                self.grid.addWidget(QLabel("Bid on Deliveries"), 1, 0)
                self.bidBtn = QPushButton("Cast Bids")
                self.bidBtn.clicked.connect(self.gotoBidding)
                self.grid.addWidget(self.bidBtn, 1, 1)
                self.grid.addWidget(QLabel("View Company Deliveries"), 2, 0)
                self.viewDeliveryBtn = QPushButton("Deliveries")
                self.viewDeliveryBtn.clicked.connect(partial(self.View, "delivery"))
                self.grid.addWidget(self.viewDeliveryBtn, 2, 1)
            else:
                # Computer Parts Company
                self.grid.addWidget(QLabel("Make Supply Request"), 1, 0)
                self.sellBtn = QPushButton("Request")
                self.grid.addWidget(self.sellBtn, 1, 1)
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

    def gotoShoppingCart(self):
        sc = ShoppingCart(self.stack)
        self.stack.setCurrentWidget(sc)

    def gotoDeliveries(self):
        dv = DeliveryPage(self.stack)
        self.stack.setCurrentWidget(dv)
        
    def gotoBidding(self):
        bidding = BiddingPage(self.stack)
        self.stack.setCurrentWidget(bidding)

    # Display taboo list word for word
    def getTabooList(self):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        taboo_list = Sql.fetchFromDatabase(cursor, "taboo")
        text = ""
        for word in taboo_list:
            text = text + word[0] + '\n'
        db.close()
        return text

    # Insert word to taboo list
    def insertTabooWord(self):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        word = self.TabooLine.text()
        if word == "":
            print("No Word Entered")
            return 0
        print(word)
        statement = "INSERT INTO taboo(word) " \
                    "VALUES(\"" + word + "\");"
        try:
            cursor.execute(statement)
            db.commit()
            print("Taboo word successfully inserted!")
        except Exception as e:
            print(f"Error in \'insertTabooWord\': {e}\n")
        db.close()

    def deleteTabooWord(self):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        word = self.TabooLine.text()
        if word == "":
            print("No Word Entered")
            return 0
        print(word)
        statement = f"DELETE FROM taboo WHERE word = \"" + word + "\";"
        try:
            cursor.execute(statement)
            db.commit()
            print("Taboo word successfully deleted.")
        except Exception as e:
            print(f"Error in \'deleteTabooWord\': {e}\n")
        db.close()

    # Preview current bids that are unclaimed
    def viewBids(self):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        bid_list = Sql.fetchFromDatabase(cursor, "bid")
        text = ""
        for bid in bid_list:
            text = text + "Company: " + Sql.fetchFromDatabase(cursor, "company", condition="id = " + str(bid[0]))[0][1] + ", "
            text = text + "Delivery ID: " + str(bid[1]) + ", "
            text = text + "Amount: " + str(bid[2]) + "\n"
        db.close()
        return text

    # View deliveries based on company ID
    def viewCompanyDeliveries(self, user_id):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        deliveries = Sql.fetchFromDatabase(cursor, "delivery", condition=f"company = \'{user_id}\' AND claimed = \'1\'")
        text = ""
        for delivery in deliveries:
            text = text + str(delivery) + "\n"
        db.close()
        return text

    # Cast a bid as a delivery company
    def castBid(self, company_id, delivery_num, amount):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        statement = "INSERT INTO bid(company, delivery, amount) VALUES(%s, %s, %s);"
        company_name = Sql.fetchFromDatabase(cursor, "company", condition=f"id = \'{company_id}\'")[1]
        try:
            data = (company_id, delivery_num, amount)
            cursor.execute(statement, data)
            print(f"New bid added for \'{company_name}\' for order number: {delivery_num} with amount of ${amount}.")
        except Exception as e:
            print(f"Possible that bid exists, must update: {e}\n")
            current_bid_amount = Sql.fetchFromDatabase(cursor, "bid", condition=f"delivery = \'{delivery_num}\' "
                                                                            f"AND company = \'{company_id}\'")[2]
            if amount <= current_bid_amount:
                print("Error: You must cast a higher bid than your current one!")
                return
            statement = f"UPDATE bid SET amount = \'{amount}\' " \
                        f"WHERE delivery = \'{delivery_num}\' AND company = \'{company_id}\'"
            try:
                cursor.execute(statement)
                print(f"Bid for \'{company_name}\' for order number: {delivery_num} updated to ${amount}.")
            except Exception as e:
                print(f"Error in 'castBid': {e}\n")

    # Delivery company can edit delivery status of their own shipments
    def editDeliveryStatus(self, tracking_num, new_status):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        statement = f"UPDATE delivery SET status = {new_status} WHERE tracking_num = \'{tracking_num}\'"
        try:
            cursor.execute(statement)
            print(f"Delivery with ID: {tracking_num} successfully updated.")
        except Exception as e:
            print(f"Error in \'editDeliveryStatus\': {e}\n")
        db.commit()

    def View(self, table):
        msg = QMessageBox()
        msg.setText("")
        msg.setWindowTitle("View " + table)
        msg.setStandardButtons(QMessageBox.Close)
        if table == "taboo":
            msg.setText(self.getTabooList())
        elif table == "bid":
            msg.setText(self.viewBids())
        elif table == "delivery":
            msg.setText(self.viewCompanyDeliveries(user[0][0]))
        msg.exec()

    def logout(self):
        Sql.signOut(cursor)
        db.commit()
        global Logged_In, user
        Logged_In = False
        user.clear()
        new_start = StartPage(self.stack)
        self.stack.setCurrentWidget(new_start)


class ShoppingCart(Page):
    def __init__(self, stack):
        global user
        Page.__init__(self, stack)
        account_pages.update({"ShoppingCart" : self})
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(QLabel("Shopping Cart"))
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        self.items = []
        result = Sql.fetchFromDatabase(cursor, "shoppingcart", condition = "user = " + str(user[0][0]))
        for r in result:
            i = Sql.fetchFromDatabase(cursor, "item", condition = "id = " + str(r[1]))
            self.items.append(i[0])
        for item in self.items:
            self.addItem(item)
        self.PurchaseEverythingBtn = QPushButton("Purchase Everything in Shopping Cart")
        self.PurchaseEverythingBtn.clicked.connect(partial(self.purchaseEverything, user[0][0]))
        self.vbox.addWidget(self.PurchaseEverythingBtn)
        self.ClearCartBtn = QPushButton("Clear Shopping Cart")
        self.ClearCartBtn.clicked.connect(partial(self.clearShoppingCart, user[0][0]))
        self.vbox.addWidget(self.ClearCartBtn)
        self.BackBtn = QPushButton("Exit Shopping Cart")
        self.BackBtn.clicked.connect(self.gotoStartPage)
        self.vbox.addWidget(self.BackBtn)
        self.setLayout(self.vbox)
        db.close()

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
        # Purchase_Btn = QPushButton("Purchase")
        # hbox.addWidget(Purchase_Btn)
        # Remove_Btn = QPushButton("Remove From Shopping Cart")
        # hbox.addWidget(Remove_Btn)
        self.vbox.addLayout(hbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])

    # Clear shopping cart
    def clearShoppingCart(self, customer_id):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        statement = f"DELETE FROM shoppingcart WHERE user = \'{customer_id}\';"
        try:
            cursor.execute(statement)
            print("Shopping cart cleared!")
        except Exception as e:
            print(f"Error in 'clearShoppingCart': {e}\n")
        db.commit()

    # Purchase all items in shopping cart
    def purchaseEverything(self, customer_id):
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        try:
            bal = Sql.fetchFromDatabase(cursor, "wallet", condition=f"user = \'{customer_id}\'")
            if bal == []:
                balance = 0
            else:
                balance = bal[0][1]
            total_price = 0
            cart = Sql.fetchFromDatabase(cursor, "shoppingcart", condition=f"user = \'{customer_id}\'")
            for i in cart:  # Gathering items in shopping cart belonging to user
                item_price = Sql.fetchFromDatabase(cursor, "item", condition=f"id = \'{i[1]}\'")[0][2]  # Grabbing item price
                total_price += item_price
            if total_price == 0:
                print("You have no items in your shopping cart!")
            elif total_price > balance:
                print("You cannot afford all these items! Please clear shopping cart.")
            else:
                print(f"Purchased! New balance is: {balance - total_price}")
                # Upon purchasing, add to delivery table and delete from shopping cart
                statement = "INSERT INTO delivery(tracking_num, item, amount, company, customer, claimed, status) " \
                            "VALUES(%s, %s, %s, %s, %s, %s, %s);"
                customer_cart = Sql.fetchFromDatabase(cursor, "shoppingcart", condition=f"user = \'{customer_id}\'")
                for order in customer_cart:
                    cursor.execute(statement, (random.randint(500, 999999),  # Auto-incremented shipping number
                                               order[1],  # Item ID
                                               order[2],  # Item Amount
                                               3,        # Company will be chosen via bidding
                                               customer_id,
                                               0,         # Unclaimed until clerk confirms
                                               "Processing"))
                self.clearShoppingCart(customer_id)
        except Exception as e:
            print(f"Error in 'purchaseEverything': {e}\n")
        db.commit()
        db.close()


class DeliveryPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"DeliveryPage" : self})
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("My Deliveries")
        self.vbox.addWidget(self.L1)
        # Deliveries go Here
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        self.items = []
        result = Sql.fetchFromDatabase(cursor, "delivery", condition = "customer = " + str(user[0][0]))
        for r in result:
            i = Sql.fetchFromDatabase(cursor, "item", condition = "id = " + str(r[1]))
            self.items.append(i[0])
        for item in range(len(self.items)):
            self.addItem(self.items[item], result[item], cursor)
        self.BackBtn = QPushButton("Exit My Deliveries")
        self.BackBtn.clicked.connect(self.gotoStartPage)
        self.vbox.addWidget(self.BackBtn)
        self.setLayout(self.vbox)
        db.close()

    def addItem(self, item, row, cursor):
        hbox = QHBoxLayout()
        tracking_num = QLabel("Tracking num: " + str(row[0]))
        amount = QLabel("Amount: " + str(row[2]))
        status = QLabel("Status: " + str(row[6]))
        dcompany = QLabel("Delivery Company: " + Sql.fetchFromDatabase(cursor, "company", condition = "id = " + str(row[3]))[0][1])
        product_vbox = QVBoxLayout()
        product_name = QLabel(item[1])
        product_description = QLabel(item[4])
        product_image = QLabel()
        # product_image.setPixmap(QPixmap(item['image']))
        product_manufacturer = QLabel(item[3])
        hbox.addWidget(tracking_num)
        hbox.addWidget(product_image)
        product_vbox.addWidget(product_name)
        product_vbox.addWidget(product_description)
        product_vbox.addWidget(product_manufacturer)
        product_vbox.addWidget(QLabel("$" + str(item[2])))
        hbox.addLayout(product_vbox)
        hbox.addWidget(amount)
        hbox.addWidget(dcompany)
        hbox.addWidget(status)
        self.vbox.addLayout(hbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])

        
class BiddingPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"BiddingPage": self})
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Bidding")
        self.vbox.addWidget(self.L1)
        self.BackBtn = QPushButton("Exit Bidding")
        self.BackBtn.clicked.connect(self.gotoStartPage)
        self.vbox.addWidget(self.BackBtn)
        self.setLayout(self.vbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])



class RegisterPage(Page):
    def __init__(self, stack):
        Page.__init__(self, stack)
        account_pages.update({"RegisterPage" : self})
        self.vbox = QVBoxLayout()
        self.L1 = QLabel("Register")
        self.vbox.addWidget(self.L1)
        # Widgets for Registration Form
        self.UseCaseLabel = QLabel()
        self.UseCaseField = QComboBox()
        self.UseCaseField.addItems(["Customer", "Store Manager", "Store Clerk", "Computer Parts Company", "Delivery Company"])
        self.EmailLabel = QLabel("Email Address: ")
        self.EmailField = QLineEdit()
        self.PasswordLabel = QLabel("Password: ")
        self.PasswordField = QLineEdit()
        self.NameLabel = QLabel("User Name: ")
        self.NameField = QLineEdit()
        self.form = QFormLayout()
        # Add Widgets to Form
        self.form.setWidget(0, QFormLayout.LabelRole, self.UseCaseLabel)
        self.form.setWidget(0, QFormLayout.FieldRole, self.UseCaseField)
        self.form.setWidget(2, QFormLayout.LabelRole, self.EmailLabel)
        self.form.setWidget(2, QFormLayout.FieldRole, self.EmailField)
        self.form.setWidget(3, QFormLayout.LabelRole, self.PasswordLabel)
        self.form.setWidget(3, QFormLayout.FieldRole, self.PasswordField)
        self.form.setWidget(1, QFormLayout.LabelRole, self.NameLabel)
        self.form.setWidget(1, QFormLayout.FieldRole, self.NameField)
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
        global Logged_In, user
        if response.text() == "OK":
            db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
            cursor = db.cursor()
            if self.UseCaseField.currentText() == "Customer":
                # Register Customer
                customer = [self.NameField.text(), self.EmailField.text(), self.PasswordField.text()]
                Sql.insertCustomer(cursor, customer)
                db.commit()
                user.append(Sql.fetchFromDatabase(cursor, "customer", condition = "email = '" + self.EmailField.text() + "'")[0])
                user.append(self.UseCaseField.currentText())
            elif self.UseCaseField.currentText() == "Store Manager":
                # Register Admin
                admin = [self.NameField.text(), self.PasswordField.text()]
                Sql.insertAdmin(cursor, admin)
                db.commit()
                user.append(Sql.fetchFromDatabase(cursor, "admin", condition = "name = '" + self.NameField.text() + "'")[0])
                user.append(self.UseCaseField.currentText())
            elif self.UseCaseField.currentText() == "Store Clerk":
                # Register Clerk
                clerk = [self.NameField.text(), self.PasswordField.text()]
                Sql.insertClerk(cursor, clerk)
                db.commit()
                user.append(Sql.fetchFromDatabase(cursor, "clerk", condition = "name = '" + self.NameField.text() + "'")[0])
                user.append(self.UseCaseField.currentText())
            else:
                # Register Company
                company = [self.NameField.text(), self.PasswordField.text()]
                Sql.insertCompany(cursor, company)
                db.commit()
                user.append(Sql.fetchFromDatabase(cursor, "company", condition = "name = '" + self.NameField.text() + "'")[0])
                user.append(self.UseCaseField.currentText())
            # update user
            Logged_In = True
            StartPage(self.stack)
            self.gotoStartPage()
            db.close()

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
        self.loginButton.clicked.connect(self.login)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.gotoStartPage)
        self.buttonLayout.addWidget(self.loginButton)
        self.buttonLayout.addWidget(self.cancelButton)
        self.vbox.addLayout(self.buttonLayout)
        self.setLayout(self.vbox)

    def gotoStartPage(self):
        self.stack.setCurrentWidget(account_pages["StartPage"])

    def login(self):
        global Logged_In, user
        db = mysql.connector.connect(user="root", passwd=sql_password, host="localhost", db="pa_store")
        cursor = db.cursor()
        if self.UseCaseField.currentText() == "Customer":
            select_user = "SELECT * FROM customer"
            cursor.execute(select_user)
            result = cursor.fetchall()
            for row in result:
                if row[2] == self.EmailField.text():
                    if row[3] == self.PasswordField.text():
                        user.append(row)
                        user.append(self.UseCaseField.currentText())
                        Logged_In = True
                        user_id = Sql.fetchFromDatabase(cursor, "customer",
                                                        condition=f"email = \'{row[2]}\' AND password = \'{row[3]}\'")[0][0]
                        Sql.signIn(cursor, "customer", user_id)
                        db.commit()
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Complete")
                        msg.setText("Successfully Logged in as " + row[1])
                        msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Failed")
                        msg.setText('Incorrect password')
                        msg.exec()
            if not Logged_In:
                print("Login Failed: Incorrect Username or Password")
        elif self.UseCaseField.currentText() == "Store Manager":
            select_user = "SELECT * FROM admin"
            cursor.execute(select_user)
            result = cursor.fetchall()
            for row in result:
                if row[1] == self.EmailField.text():
                    if row[2] == self.PasswordField.text():
                        user.append(row)
                        user.append(self.UseCaseField.currentText())
                        Logged_In = True
                        user_id = Sql.fetchFromDatabase(cursor, "admin",
                                                        condition=f"name = \'{row[1]}\' AND password = \'{row[2]}\'")[0][0]
                        Sql.signIn(cursor, "admin", user_id)
                        db.commit()
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Complete")
                        msg.setText("Successfully Logged in as " + row[1])
                        msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Failed")
                        msg.setText('Incorrect password')
                        msg.exec()
            if Logged_In == False:
                print("Login Failed: Incorrect Username or Password")
        elif self.UseCaseField.currentText() == "Store Clerk":
            select_user = "SELECT * FROM clerk"
            cursor.execute(select_user)
            result = cursor.fetchall()
            for row in result:
                if row[1] == self.EmailField.text():
                    if row[2] == self.PasswordField.text():
                        user.append(row)
                        user.append(self.UseCaseField.currentText())
                        Logged_In = True
                        user_id = Sql.fetchFromDatabase(cursor, "clerk",
                                                        condition=f"name = \'{row[1]}\' AND password = \'{row[2]}\'")[0][0]
                        Sql.signIn(cursor, "clerk", user_id)
                        db.commit()
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Complete")
                        msg.setText("Successfully Logged in as " + row[1])
                        msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Failed")
                        msg.setText('Incorrect password')
                        msg.exec()
            if not Logged_In:
                print("Login Failed: Incorrect Username or Password")
        else:
            select_user = "SELECT * FROM company"
            cursor.execute(select_user)
            result = cursor.fetchall()
            for row in result:
                if row[1] == self.EmailField.text():
                    if row[2] == self.PasswordField.text():
                        user.append(row)
                        user.append(self.UseCaseField.currentText())
                        Logged_In = True
                        user_id = Sql.fetchFromDatabase(cursor, "company",
                                                        condition=f"name = \'{row[1]}\' AND password = \'{row[2]}\'")[0][0]
                        Sql.signIn(cursor, "company", user_id)
                        db.commit()
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Complete")
                        msg.setText("Successfully Logged in as " + row[1])
                        msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Login Failed")
                        msg.setText('Incorrect password')
                        msg.exec()
            if Logged_In == False:
                print("Login Failed: Incorrect Username or Password")
        StartPage(self.stack)
        self.gotoStartPage()
        db.close()


class Account(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.account_stack = QStackedLayout()
        self.Start_Page = StartPage(self.account_stack)
        self.Register_Page = RegisterPage(self.account_stack)
        self.Login_Page = LoginPage(self.account_stack)
        self.setLayout(self.account_stack)

    def getUser(self):
        global user
        return user

    def getLoggedIn(self):
        global Logged_In
        return Logged_In
