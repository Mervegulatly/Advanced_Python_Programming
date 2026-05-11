import sqlite3

connection=sqlite3.connect("my_db.db")

cursor=connection.cursor()

print("Veritabanı oluşturuldu.")

connection.close()