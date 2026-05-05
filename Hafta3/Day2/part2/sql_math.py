import sqlite3

db = sqlite3.connect("btk_akademi.db")
cursor = db.cursor()

#sql = "SELECT SUM(stok_adedi), AVG(fiyat) FROM urunler"  # "WHERE urun_adi LIKE 'I%'""  eklenebilir. 

#toplam_stok, ortalama_fiyat = cursor.fetchone()  #sql deki gibi sırasıyla atama yapılmalı

# print(f"Toplam stok: {toplam_stok}")
# print(f"Ortalama fiyat: {ortalama_fiyat}")

sql = "SELECT MIN(fiyat), MAX(fiayt) FROM urunler"

cursor.execute(sql)


min_fiyat, max_fiyat = cursor.fetchone

print(f"En düşük fiyat: {min_fiyat}")
print(f"En yüksek fiyat: {max_fiyat}")


##################################################

cursor.execute("SELECT kategori, COUNT(*) FROM urunler GROUP BY kategori")