import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()
	c.execute("DROP TABLE IF EXISTS numbers")
	c.execute("CREATE TABLE numbers (random_num INT);")
	for i in range(100):
		c.execute("INSERT INTO numbers VALUES(?);", (random.randint(0, 101),))
