# Create a SQLite3 database and table

# Import SQLite3 library

import sqlite3

conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands 

cursor = conn.cursor()

# create a table

cursor.execute("DROP TABLE IF EXISTS population")
cursor.execute("""CREATE TABLE population ( city TEXT, state TEXT, population INT );""")

# close database connection 

conn.close()