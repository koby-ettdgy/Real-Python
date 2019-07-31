import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("SELECT * FROM invantory;")

	rows = c.fetchall()

	for r in rows:
		print (f"{r[0]}, {r[1]} \n {r[2]}") 

		c.execute("SELECT COUNT(order_date) FROM orders WHERE make = ? AND model = ? ", (r[0], r[1]))

		order_count = c.fetchone()[0]

		print(order_count)



