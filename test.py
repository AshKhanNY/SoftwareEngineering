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
        print(f"Error in 'insertToShoppingCart' (Possible duplicate entry): {e}\n")
        statement = f"UPDATE shoppingcart SET amount = amount + 1 WHERE user = \'{customer_id}\' AND item = \'{item_id}\'"
        cursor.execute(statement)
        print("Item amount updated for user.")
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
            # Upon purchasing, add to delivery table
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
    except Exception as e:
        print(f"Error in 'purchaseEverything': {e}\n")
    db.commit()


# Insert into customer table (requires array of name, email, password)
def insertCustomer(cursor, arr):
    statement = "INSERT INTO customer(id, name, email, password, joined, signed_in) " \
                "VALUES(%s, %s, %s, %s, %s, %s);"
    try:
        cus_arr = fetchFromDatabase(cursor, "customer")
        cursor.execute(statement, (len(cus_arr) + random.randint(500, 999999),   # ID
                                   arr[0],   # Name
                                   arr[1],   # Email
                                   arr[2],   # Password
                                   datetime.now(),        # Time Joined
                                   False))   # Signed In?
        print("Customer successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertCustomer\': {e}\n")

# Insert into company table (requires array of name, type)
def insertCompany(cursor, arr):
    statement = "INSERT INTO company(id, name, type, signed_in) " \
                "VALUES(%s, %s, %s, %s);"
    try:
        com_arr = fetchFromDatabase(cursor, "company")
        cursor.execute(statement, (len(com_arr) + random.randint(1200, 999999),   # ID
                                   arr[0],   # Name
                                   arr[1],   # Type
                                   False))   # Signed In?
        print("Company successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertCompany\': {e}\n")

# Insert into clerk table (requires array of name, password)
def insertClerk(cursor, arr):
    statement = "INSERT INTO clerk(id, name, password, signed_in) " \
                "VALUES(%s, %s, %s, %s);"
    try:
        cl_arr = fetchFromDatabase(cursor, "clerk")
        cursor.execute(statement, (len(cl_arr) + random.randint(700, 999999),   # ID
                                   arr[0],   # Name
                                   arr[1],   # Password
                                   False))   # Signed In?
        print("Clerk successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertClerk\': {e}\n")

# Insert into admin table (requires array of name, password)
def insertAdmin(cursor, arr):
    statement = "INSERT INTO admin(id, name, password, signed_in) " \
                "VALUES(%s, %s, %s, %s);"
    try:
        ad_arr = fetchFromDatabase(cursor, "admin")
        cursor.execute(statement, (len(ad_arr) + random.randint(1500, 999999),   # ID
                                   arr[0],   # Name
                                   arr[1],   # Password
                                   False))   # Signed In?
        print("Admin successfully inserted!")
    except Exception as e:
        print(f"Error in \'insertAdmin\': {e}\n")
