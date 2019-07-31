import sqlite3

cars = [('Frod','Fiest', '1988-01-20'), 
        ('Frod','Fiest', '1990-11-2'), 
        ('Frod','Fiest', '1986-05-25'),
        ('Frod','Focus', '1986-05-25'),
        ('Frod','Focus', '1982-07-21'),
        ('Frod','Focus', '1988-06-25'),
        ('Frod','Fusion', '1999-05-25'),
        ('Frod','Fusion', '1996-07-21'),
        ('Frod','Fusion', '1998-06-25'),
        ('Honda', 'Accord', '2000-01-16'),
        ('Honda', 'Accord', '2000-05-1'),
        ('Honda', 'Accord', '2000-06-6'),
        ('Honda', 'Civic', '2001-01-11'),
        ('Honda', 'Civic', '2002-02-13'),
        ('Honda', 'Civic', '2003-05-15')
         ]
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT);")
    c.executemany("INSERT INTO orders VALUES(?,?,?);", cars)









