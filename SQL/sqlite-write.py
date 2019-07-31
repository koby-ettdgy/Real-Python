import sqlite3


# Working with DataBase Tables

with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.execute(""" CREATE TABLE Peoples(FirstName TEXT,Last_Name TEXT,Age INT);""")
	cursor.execute("""INSERT INTO Peoples VALUES('Ron','Obvious',25);""")

# Create a new table and insert values

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute(""" CREATE TABLE People(FirstName TEXT,Last_Name TEXT,Age INT);""")
cursor.execute("""INSERT INTO People VALUES('Ron','Obvious',25);""")
connection.commit()
connection.close()

# get data from a table

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM People")
cursor.fetchone()


# Executing Multiple SQL Statements using executescript()

with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.executescript("""DROP TABLE IF EXISTS People;
	DROP TABLE IF EXISTS Peoples; 
	CREATE TABLE People(
	FirstName TEXT, 
	LastName TEXT, 
	Age INT); 
	INSERT INTO People VALUES(
	'Ron', 
	'Obvious', '66'
	);""")


# Execute many similar statements using .executemany()

people_values = (
	("Ron", "Obvious", 42),
	("Luri", "Victor", 15),
	("Arthor", "Bill", 66)
)
with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)


# Take a user input and insert into a table

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age"))
data = (first_name, last_name, age)

with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.execute("INSERT INTO People VALUES(?, ?, ?)", data)


# update the content of a row

cursor.execute(
	"UPDATE People SET Age=? WHERE First_Name = ? AND Last_Name = ?",
	(45, "BOB", "BOBI"))





