import sqlite3

values = (
    ("Ron", "Obvious", 42),
    ("Ron", "Obvious", 42),
    ("Ron", "Obvious", 42),
)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS People")
    cursor.execute(
        """CREATE TABLE People(
        first_name TEXT,
        last_name TEXT,
        age INT
        );"""
    )
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", values)

    cursor.execute(
        "SELECT first_name, last_name FROM People WHERE Age > 30"
    )
    for row in cursor.fetchall():
        print(row)

