# Insert Command

#import sqlite3 libary

import sqlite3

with sqlite3.connect ("new.db") as conn:
	cursor = conn.cursor()
	cursor.execute(""" INSERT INTO population VALUES ('New York City', 'NY', 8400000);""")
	cursor.execute(""" INSERT INTO population VALUES ('San Francisco', 'CA', 80000);""")


