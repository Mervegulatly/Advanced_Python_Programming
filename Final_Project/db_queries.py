import sqlite3

db = sqlite3.connect("final_db.db")
cursor = db.cursor()

print("Değeri 50'den büyük olanlar:\n")

cursor.execute("""
SELECT id, birim_adi, deger, islem_tarihi
FROM kayitlar
WHERE deger > 0.5
""")
sonuclar = cursor.fetchall()

for row in sonuclar:
    print(row)


print("\n🔹 Her kur için en yüksek değer:\n")

cursor.execute("""
SELECT birim_adi, MAX(deger)
FROM kayitlar
GROUP BY birim_adi
""")

sonuclar = cursor.fetchall()

for row in sonuclar:
    print(f"Birim: {row[0]} | En yüksek değer: {row[1]}")


db.close()