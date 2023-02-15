import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users(id, email, password) VALUES (?,?,?)", (1, 'test@example.com', 123 ))

connection.commit()
connection.close()