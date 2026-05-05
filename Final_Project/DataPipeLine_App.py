import sqlite3

db=sqlite3.connect("btk_final.db")
cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kayitlar (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               birim_adi TEXT NOT NULL,
               deger REAL,
               islem_tarihi TEXT)"""

)

db.commit()
print("Tablo oluşturuldu.")

db.close()