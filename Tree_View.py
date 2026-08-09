import sqlite3
conn=sqlite3.connect('phones')
cursor = conn.cursor()
cursor.execute("SELECT * FROM customers")
list = cursor.fetchall()
print(list)