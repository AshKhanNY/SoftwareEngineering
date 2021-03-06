# Initialize database from SQL file
import random
import mysql.connector
from datetime import datetime

def initializeDBFromFile(cursor, filename):
    print("Initializing database...")
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()
    sql_commands = sql_file.split(';')
    try:
        for command in sql_commands:
            if command.strip() != '':
                cursor.execute(command)
        print("Successfully initialized database.")
    except Exception as e:
        print(f"Error in initializing: {e}")

# Fetching specific values from database
def fetchFromDatabase(cursor, table, item="*", condition=""):
    try:
        if condition != "":
            cursor.execute(f"SELECT {item} FROM {table} WHERE {condition};")
        else:
            cursor.execute(f"SELECT {item} FROM {table};")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error in \'fetchFromDatabase\': {e}")
        return False

# Checking what type of user is logged in
def getSignedInType(cursor):
    user_type = []
    try:
        temp = fetchFromDatabase(cursor, "user", condition="signed_in = 1")[0]
        user_type = temp[1]
    except Exception as e:
        print(f"Error in \'getSignedInType\': {e}")
    return user_type

# Check if someone is signed in
def getSignedIn(cursor):
    user = []
    try:
        user = fetchFromDatabase(cursor, "user", condition="signed_in = 1")[0]
    except Exception as e:
        print(f"Error in \'getSignedInType\': {e}")
    return user

# Signs user in
def signIn(cursor, user_type, user_id):  # User type must be "customer", "company", "admin", or "clerk"
    signOut(cursor)
    statement = f"UPDATE user SET signed_in = 1 WHERE id = {user_id} AND type = \'{user_type}\';"
    try:
        cursor.execute(statement)
        name = fetchFromDatabase(cursor, user_type, condition=f"id = {user_id}")[0][1]
        print(f"Signed in as {user_type} {name}")
    except Exception as e:
        print(f"Error in \'signIn\': {e}")

# Signs user out
def signOut(cursor):
    statement = f"UPDATE user SET signed_in = 0;"
    try:
        cursor.execute(statement)
        print(f"Signed everyone out.")
    except Exception as e:
        print(f"Error in \'signOut\': {e}")

# Check if something exists in a table
def existsInTable(cursor, table, atr, val):
    statement = f"SELECT * FROM {table} WHERE {atr} = {val};"
    cursor.execute(statement)
    return cursor.fetchall()

# Update table with new values (replace old w/ new)
def updateTable(cursor, table, atr, val, condition):
    statement = f"UPDATE {table} " \
                f"SET {atr} = {val} " \
                f"WHERE {condition};"
    cursor.execute(statement)

# Check if customer exists
def customerExists(cursor, user_details_arr):
    if len(user_details_arr) == 2:  # Contains email AND password (for signing in)
        statement = f"SELECT * FROM customer WHERE email = %s AND password = %s;"
        cursor.execute(statement, (user_details_arr[0], user_details_arr[1]))
    else:  # Contains just email (for signing up)
        statement = f"SELECT * FROM customer WHERE email = %s;"
        cursor.execute(statement, (user_details_arr[0],))
    try:
        return cursor.fetchall()
    except Exception as e:
        print(f"Error in customer sign in: {e}")

# Check if worker (admin or clerk) exists
def workerExists(cursor, user_details_arr, type):
    statement = f"SELECT * FROM {type} WHERE name = %s AND password = %s;"
    cursor.execute(statement, (user_details_arr[0], user_details_arr[1]))
    try:
        return cursor.fetchall()
    except Exception as e:
        print(f"Error in worker sign in: {e}")

# Insert to Shopping Cart
def insertToShoppingCart(self, item_id, customer_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = "INSERT INTO shoppingcart(user, item, amount) VALUES(%s, %s, %s);"
    try:
        data = (customer_id, item_id, 1)
        cursor.execute(statement, data)
        print("Item added to cart.")
    except Exception as e:
        print(f"Possible duplicate entry: {e}\n")
        statement = f"UPDATE shoppingcart SET amount = amount + 1 WHERE user = \'{customer_id}\' AND item = \'{item_id}\'"
        try:
            cursor.execute(statement)
            print("Item amount updated for user.")
        except Exception as e:
            print(f"Error in 'insertToShoppingCart': {e}\n")
    db.commit()

# Clear shopping cart
def clearShoppingCart(self, customer_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
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
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    try:
        balance = fetchFromDatabase(cursor, "wallet", condition=f"user = \'{customer_id}\'")[0]
        total_price = 0
        cart = fetchFromDatabase(cursor, "shoppingcart", condition=f"user = \'{customer_id}\'")
        for i in cart:  # Gathering items in shopping cart belonging to user
            item_price = fetchFromDatabase(cursor, "item", condition=f"id = \'{i[1]}\'")[0][2]  # Grabbing item price
            total_price += item_price
        if total_price == 0:
            print("You have no items in your shopping cart!")
        elif total_price > balance:
            print("You cannot afford all these items! Please clear shopping cart.")
        else:
            print(f"Purchased! New balance is: {balance - total_price}")
            # Upon purchasing, add to delivery table, update wallet, and delete from shopping cart
            statement = f"UPDATE wallet SET amount = \'{balance - total_price}\' WHERE user = \'{customer_id}\'"
            cursor.execute(statement)
            statement = "INSERT INTO delivery(tracking_num, item, amount, company, customer, claimed, status) " \
                        "VALUES(%s, %s, %s, %s, %s, %s, %s);"
            customer_cart = fetchFromDatabase(cursor, "shoppingcart", condition=f"user = \'{customer_id}\'")
            for order in customer_cart:
                cursor.execute(statement, (1,  # Auto-incremented shipping number
                                           order[1],  # Item ID
                                           order[2],  # Item Amount
                                           "",        # Company will be chosen via bidding
                                           customer_id,
                                           0,         # Unclaimed until clerk confirms
                                           "Processing"))
            clearShoppingCart(self, customer_id)
    except Exception as e:
        print(f"Error in 'purchaseEverything': {e}\n")
    db.commit()

# Display taboo list word for word
def getTabooList(self):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    taboo_list = fetchFromDatabase(cursor, "taboo")
    for word in taboo_list:
        print(word[0])  # TODO: Instead of printing, display list on separate window

# Insert word to taboo list
def insertTabooWord(self, word):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = "INSERT INTO taboo(word) " \
                "VALUES(%s);"
    try:
        cursor.execute(statement, word)
        print("Taboo word successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertTabooWord\': {e}\n")

def deleteTabooWord(self, word):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = f"DELETE FROM taboo WHERE word = {word};"
    try:
        cursor.execute(statement, word)
        print("Taboo word successfully deleted.")
    except Exception as e:
        print(f"Error in \'deleteTabooWord\': {e}\n")

# Insert into customer table (requires array of name, email, password)
def insertCustomer(cursor, arr):
    statement = "INSERT INTO customer(id, name, email, password, joined) " \
                "VALUES(%s, %s, %s, %s, %s);"
    try:
        cus_arr = fetchFromDatabase(cursor, "customer")
        id_num = len(cus_arr) + 1
        cursor.execute(statement, (id_num,   # ID
                                   arr[0],   # Name
                                   arr[1],   # Email
                                   arr[2],   # Password
                                   datetime.now()))

        insertUser(cursor, id_num, "customer")
        print("Customer successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertCustomer\': {e}\n")

# Insert into company table (requires array of name, type)
def insertCompany(cursor, arr):
    statement = "INSERT INTO company(id, name, type) " \
                "VALUES(%s, %s, %s);"
    try:
        com_arr = fetchFromDatabase(cursor, "company")
        id_num = len(com_arr) + 1
        cursor.execute(statement, (id_num,   # ID
                                   arr[0],   # Name
                                   arr[1]))  # Password
        insertUser(cursor, id_num, "company")
        print("Company successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertCompany\': {e}\n")

# Insert into clerk table (requires array of name, password)
def insertClerk(cursor, arr):
    statement = "INSERT INTO clerk(id, name, password) " \
                "VALUES(%s, %s, %s);"
    try:
        cl_arr = fetchFromDatabase(cursor, "clerk")
        id_num = len(cl_arr) + 1
        cursor.execute(statement, (id_num,   # ID
                                   arr[0],   # Name
                                   arr[1]))  # Password
        insertUser(cursor, id_num, "clerk")
        print("Clerk successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertClerk\': {e}\n")

# Insert into admin table (requires array of name, password)
def insertAdmin(cursor, arr):
    statement = "INSERT INTO admin(id, name, password) " \
                "VALUES(%s, %s, %s);"
    try:
        ad_arr = fetchFromDatabase(cursor, "admin")
        id_num = len(ad_arr) + 1
        cursor.execute(statement, (id_num,   # ID
                                   arr[0],   # Name
                                   arr[1]))  # Password
        insertUser(cursor, id_num, "admin")
        print("Admin successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertAdmin\': {e}\n")

# Insert to user table after inserting a customer/clerk/company/admin
def insertUser(cursor, user_id, user_type):
    signOut(cursor)
    statement = "INSERT INTO user(id, type, signed_in) " \
                "VALUES(%s, %s, %s);"
    try:
        cursor.execute(statement, (user_id, user_type, 1))
    except Exception as e:
        print(f"Error in \'insertUser\': {e}\n")

# ************** DELIVERIES ***************

# Preview current bids that are unclaimed
def viewBids(self):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    bid_list = fetchFromDatabase(cursor, "bid")
    for bid in bid_list:
        print(bid)

# View deliveries based on company ID
def viewCompanyDeliveries(self, user_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    deliveries = fetchFromDatabase(cursor, "delivery", condition=f"company = \'{user_id}\' AND claimed = \'1\'")
    for delivery in deliveries:
        print(delivery)

# View deliveries based on customer ID
def viewCustomerDeliveries(self, user_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    deliveries = fetchFromDatabase(cursor, "delivery", condition=f"customer = \'{user_id}\'")
    for delivery in deliveries:
        print(delivery)

# Cast a bid as a delivery company
def castBid(self, company_id, delivery_num, amount):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = "INSERT INTO bid(company, delivery, amount) VALUES(%s, %s, %s);"
    company_name = fetchFromDatabase(cursor, "company", condition=f"id = \'{company_id}\'")[1]
    try:
        data = (company_id, delivery_num, amount)
        cursor.execute(statement, data)
        print(f"New bid added for \'{company_name}\' for order number: {delivery_num} with amount of ${amount}.")
    except Exception as e:
        print(f"Possible that bid exists, must update: {e}\n")
        current_bid_amount = fetchFromDatabase(cursor, "bid", condition=f"delivery = \'{delivery_num}\' "
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
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = f"UPDATE delivery SET status = {new_status} WHERE tracking_num = \'{tracking_num}\'"
    try:
        cursor.execute(statement)
        print(f"Delivery with ID: {tracking_num} successfully updated.")
    except Exception as e:
        print(f"Error in \'editDeliveryStatus\': {e}\n")
    db.commit()

# Confirm bid
def confirmBid(cursor, delivery_num, company):
    deli_statement = f"UPDATE delivery SET status = Confirmed, company = {company} WHERE tracking_num = \'{delivery_num}\'"
    bid_statement = f"DELETE FROM bid WHERE delivery = {delivery_num}"
    try:
        cursor.execute(deli_statement)
        cursor.execute(bid_statement)
    except Exception as e:
        print(f"Error in \'confirmBid\': {e}\n")

# *************** SUPPLIES *****************
# View Supply Request
def viewSupplyRequests(self):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    requests = fetchFromDatabase(cursor, "supplyrequest")
    for request in requests:
        print(request)

# Cast supply request
def castSupplyRequest(self, text, company_id):
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
    statement = "INSERT INTO supplyrequest(supply_id, company, reason) " \
                "VALUES(%s, %s, %s);"
    try:
        sup_arr = fetchFromDatabase(cursor, "supplyrequest")
        id_num = len(sup_arr) + 1
        cursor.execute(statement, (id_num, company_id, text))
        print("Successfully casted reply!")
    except Exception as e:
        print(f"Error in \'castSupplyRequest\': {e}\n")

# Add supply to store
def insertItem(cursor, arr):
    statement = "INSERT INTO item(id, name, price, manufacturer, details, type, amount) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s);"
    try:
        item_arr = fetchFromDatabase(cursor, "item")
        id_num = len(item_arr) + 1
        cursor.execute(statement, (id_num,   # ID
                                   arr[0],   # Name
                                   arr[1],   # Price
                                   arr[2],   # Manufacturer
                                   arr[3],   # Details
                                   arr[4],   # Type
                                   arr[5]))  # Amount
        print("Item successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertItem\': {e}\n")

# ************ Reports / Banning ************
def banUser(cursor, user_id, user_type, reason):
    if user_type == "customer":
        statement = "INSERT INTO blacklistedcustomer(customer_id, reason) " \
                    "VALUES(%s, %s);"
    else:
        statement = "INSERT INTO blacklistedcompany(company_id, reason) " \
                    "VALUES(%s, %s);"
    try:
        cursor.execute(statement, (user_id, reason))
        print(f"Banned user {user_id} for: {reason}")
    except Exception as e:
        print(f"Error in \'banUser\': {e}\n")

def viewReportList(cursor, user_type):
    return fetchFromDatabase(cursor, f"{user_type}report")

def viewBannedList(cursor, user_type):
    return fetchFromDatabase(cursor, f"blacklisted{user_type}")

def reportUser(cursor, user_id, user_type, reason):
    statement = f"INSERT INTO {user_type}report({user_type}_id, num_reported, reason) " \
                "VALUES(%s, %s, %s);"
    try:
        report_count = 1
        if fetchFromDatabase(cursor, f"{user_type}report", condition=f"{user_type}_id = {user_id}"):
            report_count = fetchFromDatabase(cursor, f"{user_type}report", condition=f"{user_type}_id = {user_id}")[0][1]
        cursor.execute(statement, (user_id, report_count, reason))
        print(f"Reported user {user_id} for: {reason}")
    except Exception as e:
        print(f"Error in \'reportUser\': {e}\n")

# ********** CREDIT CARD / WALLET ***********
def addCreditCard(cursor, user_id, name, number, expiration):
    statement = f"INSERT INTO creditcard(user, name, number, expiration) " \
                "VALUES(%s, %s, %s, %s);"
    try:
        cursor.execute(statement, (user_id, name, number, expiration))
        print("Successfully added credit card.")
    except Exception as e:
        print(f"Error in \'addCreditCard\': {e}\n")

def addFundsToWallet(cursor, user_id, amount):
    statement = "INSERT INTO wallet(user, amount) VALUES(%s, %s);"
    try:
        cursor.execute(statement, (user_id, amount))
        print(f"New wallet created.")
    except Exception as e:
        print(f"Possible that wallet exists, must update: {e}\n")
        current_wallet_amount = fetchFromDatabase(cursor, "wallet", condition=f"user = {user_id}")[0][1]
        statement = f"UPDATE wallet SET amount = \'{amount + current_wallet_amount}\' WHERE user = \'{user_id}\'"
        try:
            cursor.execute(statement)
            print(f"Wallet updated to ${amount + current_wallet_amount}.")
        except Exception as e:
            print(f"Error in 'addFundsToWallet': {e}\n")
