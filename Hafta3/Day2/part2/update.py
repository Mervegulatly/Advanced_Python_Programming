import sqlite3

db = sqlite3.connect("btk_akademi.db")
cursor = db.cursor()

yeni_fiyat = 40000
urun_id = 1

sql = "UPDATE urunler SET fiyat = ? WHERE  id = ?" # "?" = place holder kullanmamızdaki neden genel bir kod yazmak daha spesifik de yazılabilir direkt ürünün fiyatı gibi.

cursor.execute(sql, (yeni_fiyat, urun_id))  # Öncelik sırası önemli hangisi önecyse onu yazmalısın

db.commit()


# Select ile tüm ürün fiyatları çekilir ve ürünlerin %10 indirimli halini hesaplayıp yazdırabiliriz