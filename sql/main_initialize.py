import mysql.connector

# Initializes database with empty tables
def initializeDBFromFile(cur, filename):
    print("Initializing database...")
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()
    sql_commands = sql_file.split(';')
    try:
        for command in sql_commands:
            if command.strip() != '':
                cur.execute(command)
        print("Successfully initialized database.")
    except Exception as e:
        print(f"Error in initializing: {e}")

# Connecting to database...
try:
    db = mysql.connector.connect(user="root", passwd="root", host="localhost", db="pa_store")
    cursor = db.cursor()
except mysql.connector.errors.ProgrammingError as e:
    print(f"Looks like this is your first time running this: {e}.\n"
          f"Let's make a new database for you.")
    db = mysql.connector.connect(user="root", passwd="root", host="localhost")
    cursor = db.cursor()
    statement = "CREATE DATABASE IF NOT EXISTS pa_store;"
    cursor.execute(statement)
    db.commit()

initializeDBFromFile(cursor, "pa_store.sql")
