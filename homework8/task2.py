import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents where name=:name', {name: 'Yeltsin'})
data = cursor.fetchall()  # will get all records with this name. You can also use .fetchone() to get one record.