import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	sql = {'Focus Count':"SELECT COUNT(make) FROM orders WHERE model='Focus';",
	       'Fiest Coute':"SELECT COUNT(make) FROM orders WHERE model='Fiest';",
	       'Fusion Coute':"SELECT COUNT(make) FROM orders WHERE model='Fusion';",
	       'Civic Coute':"SELECT COUNT(make) FROM orders WHERE model='Civic';",
	       'Accord Coute':"SELECT COUNT(make) FROM orders WHERE model='Accord';"}

	for keys, values in sql.items():
		c.execute(values)

		results = c.fetchone()

		print (f"{keys}: {results[0]}")

