import sqlite3

db = sqlite3.connect("my_db.db")
cursor = db.cursor()

sql = "SELECT * FROM urunler WHERE urun_adi LIKE ?"

search_target = "I%"

cursor.execute(sql, (search_target,))

sonuclar = cursor.fetchall()

print(sonuclar)