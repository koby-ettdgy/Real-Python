import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT invantory.make, invantory.model,
            invantory.quantity, orders.order_date FROM invantory INNER JOIN orders
            ON invantory.model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
        print(r[2])
        print(r[3])
        print()