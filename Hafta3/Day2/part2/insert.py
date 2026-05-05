import sqlite3

db = sqlite3.connect("btk_akademi.db")
cursor = db.cursor()

sql = "INSERT INTO urunler(urun_adi, fiyat, stok_adedi) VALUES (?, ?, ?, ?)"  #id ye gerek yok eklersek çakışma olabilir.

#values = ("IPHONE 15, 50000, 52")

#cursor.execute(sql, values)

liste = [
    ("Mouse", 1500, 10),
    ("Monitor", 10000, 5)
    ("Klavye", 2000, 9)
]

cursor.execute(sql, liste)

db.commit()  #Değişiklik kaydediliyor
print(f"{cursor.rowcount} #adet kayıt eklendi. Son eklenen ID:{cursor.lastrowid}")

db.close()