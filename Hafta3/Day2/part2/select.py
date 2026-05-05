import sqlite3

db = sqlite3.connect("btk_akademi.db")
cursor = db.cursor()

sql = "SELECT * FROM urunler"

cursor.execute(sql)

urun = cursor.fetchone()
urun2 = cursor.fetchmany(3) #İlk 3 ürünü getirir
urun3 = cursor.fetchall()

print(urun)

for u in urun3:
    print(f"ID: {u[0]}, Ürün Adı: {u[1]}, Stok Adedi: {u[3]}")

toplam = 0
for urun in urun3:
    toplam += urun[3]
print(toplam)

db.close()

