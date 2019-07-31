import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE invantory SET Quantity = 60000 WHERE Model = 'Civic'")
	c.execute("UPDATE invantory SET Quantity = 70000 WHERE Model = 'Fiest'")

	print ("\nNEW DATA:\n")

	c.execute("SELECT * FROM invantory")

	rows = c.fetchall()

	for r in rows:
		print (r[0], r[1], r[2])








