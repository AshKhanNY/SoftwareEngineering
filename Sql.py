# Initialize database from SQL file
import random
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

def insertToShoppingCart(cursor, item_id, customer_id):
    statement = "INSERT INTO shoppingcart(user, item, amount) " \
                "VALUES(%s, %s, %s);"
    try:
        cursor.execute(statement, (customer_id, item_id, 1))
        print("Item added to cart.")
    except Exception as e:
        print(f"Error in 'insertToShoppingCart': {e}\n")
