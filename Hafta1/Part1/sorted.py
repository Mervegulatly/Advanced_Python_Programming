liste = [25, 10, 5, 80, 33]
print(liste)
print(sorted(liste)) #sorted fonksiyonu listeyi sıralar ama orjinal listeyi değiştirmez.
print(liste)

print(sorted(liste, reverse=True)) #reverse parametresi ile büyükten küçüğe sıralama yapar.

################################################################

stok = [("Elma", 50), ("Cilek", 100), ("Muz", 20)]
sirali = sorted(stok, reverse = True)
print(sirali)

############################################################
#dict = {key : value}

urunler = [
    {"ad": "Laptop", "fiyat": 1000},
    {"ad": "Telefon", "fiyat": 900},
    {"ad": "Tablet", "fiyat": 700}
]

sirali_urunler = sorted(urunler, key=lambda x: x["fiyat"]) #key parametresi ile sıralama kriteri belirlenir.
print(sirali_urunler)

##########################################################

isimler = ["Ebru", "Ayşe", "Abdullah", "Zeynep"]
sirali_isimler = sorted(isimler) #sorted fonksiyonu stringleri alfabetik olarak sıralar. Büyük harfler küçük harflerden önce gelir.
print(sirali_isimler)


sirali_isimler2 = sorted(isimler, key=lambda x: len(x)) # isimlerin uzunluğuna göre
print(sirali_isimler2)  #Ebru ve Ayşe aynı olduğu için onlar aynı kalır yer değiştirmez!!


