import sqlite3

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()
	while True:
		user_input = input("WHAT Would YOU LIKE TO DO ?\n \
		FOR AVG PRESS 1\n \
		FOR MAX PRESS 2\n\
		FOR MIN PRESS 3\n\
		FOR SUM PRESS 4\n\
		TO QUIT PRESS q\n The System Is Waiting For Your Choice:")
		if user_input == '1':
			c.execute("SELECT AVG(random_num) FROM numbers")
			avg_num = c.fetchone()
			print(f"\n\nTHE AVG Number is: {avg_num[0]}\n\n")
		elif user_input == '2':
			c.execute("SELECT MAX(random_num) FROM numbers")
			max_num = c.fetchone()
			print(f"\n\nTHE MAX Number is: {max_num[0]}\n\n")
		elif user_input == '3':
			c.execute("SELECT MIN(random_num) FROM numbers")
			min_num = c.fetchone()
			print(f"\n\nTHE MIN Number is: {min_num[0]}\n\n")
		elif user_input == '4':
			c.execute("SELECT SUM(random_num) FROM numbers")
			sum_num = c.fetchone()
			print(f"\n\nTHE SUM Number is: {sum_num[0]}\n\n")
		elif user_input == 'q':
			print(f"\n\nBye Bye !!!!\n\n")
			break
		else:
			print("Invalid Option!")




