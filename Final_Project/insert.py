import sqlite3
from datetime import datetime
from request import secilen_kurlar

db = sqlite3.connect("btk_final.db")
cursor = db.cursor()

# secilen_kurlar = {
#     "USD": 1,
#     "EUR": 0.92,
#     "GBP": 0.78
# }

tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Data insert
for birim, deger in secilen_kurlar.items():
    cursor.execute("""
    INSERT INTO kayitlar (birim_adi, deger, islem_tarihi)
    VALUES (?, ?, ?)
    """, (birim, deger, tarih))

db.commit()

db.close()

print("Veriler veritabanına kaydedildi")