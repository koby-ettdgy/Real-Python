import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	cars = [('Ford', 'Fiest', 50000),\
	('Ford', 'Focus', 60000),\
	('Ford', 'Fusion', 150000), \
	('Honda', 'Accord', 60000), \
	('Honda', 'Civic', 160000)  ]

	c.executemany("INSERT INTO invantory VALUES (?,?,?);", cars)


	



