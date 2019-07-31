import sqlite3

values = (
    ("Jean-Baptiste", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5),
)
with sqlite3.connect("new_test_databased.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute(
        """CREATE TABLE Roster(
               Name TEXT,
               Species TEXT,
               IQ INT);""")
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)", values)
    cursor.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")

    cursor.execute("SELECT IQ FROM Roster WHERE Species = 'Human'")

    for row in cursor.fetchall():
        print(row)
