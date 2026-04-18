list = [1, 2, 3, 4, 5]
result = []

print("Orijinal Liste:", list)
result = list.append(6)
print("Güncellenmiş Liste:", list)



number = []
for i in range(6):
    number.append(i**2)

print("Kareler Listesi:", number)


list = [i for i in range(6)]
print("Liste Üretimi ile Oluşturulan Liste:", list)


list = [i**2 for i in range(6)]
print("Kareler Listesi (Liste Üretimi ile):", list)


names = ["Alice", "Bob", "Charlie", "David"]
print("Orijinal İsimler Listesi:", names)


for name in names:
    print(name.upper())

isimler = []


for name in names:
    isimler.append(name.upper())
print("Büyük Harf Listesi:", isimler)


#List Comprehension ile büyük harf listesi oluşturma
names = [name.upper() for name in names]
print("Büyük Harf Listesi:", names)


metin = "BTK Akademi"
print("Orijinal Metin:", metin)

Karakterler = [krk for krk in metin]
print("Karakterler Listesi:", Karakterler)

ters_metin = metin[::-1]
print("Ters Metin:", ters_metin)

