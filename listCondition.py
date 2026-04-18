#for i in list:
#    if (kosul):
#       expression


#[Expression for item in iterable if condition]

numbers = [2, 5, 8, 13, 24, 45]
ciftler = []

for i in numbers:
    if i % 2 == 0:
        ciftler.append(i)

print("Orijinal Sayılar Listesi:", numbers)
print("Çift Sayılar Listesi:", ciftler)

#Comprehension ile çift sayılar listesi
ciftler = [i for i in numbers if i % 2 == 0]  # i**2 for i in numbers if i % 2 == 0 olarak da çiftlerin karesini alabiliriz
print("Çift numbers Listesi (List Comprehension ile):", ciftler)

###########################################################

sehirler = ["Ankara", "Afyon", "Eskişehir", "Bursa"]
a_olanlar = [sehir for sehir in sehirler if "a" in sehir.lower()]  # "a" harfi büyük küçük farketmez şekilde kontrol edilir
print("Orijinal Şehirler Listesi:", sehirler)
print("İsminin içinde 'a' harfi bulunan şehirler:", a_olanlar)

###########################################################

notlar = [55, 70, 85, 90, 45]
sonuc = []

for n in notlar:
    if n >= 50:
        sonuc.append("Geçti")
    else:
        sonuc.append("Kaldı")

print("Orijinal Notlar Listesi:", notlar)
print("Sınav Sonuçları:", sonuc)

#List Comprehension ile sınav sonuçları
#Filtreleme işlemi yapılırken if koşulu sonda kullanılır, expression kısmında ise koşula göre farklı sonuçlar üretilebilir ve başta kullanılır!!!
# Neyi asıl if de iddia edildiyse o kısmı if in başında else kısmı diğer tarafında olmalıdır.
sonuc = ["Geçti" if n>=50 else "Kaldı" for n in notlar]
print("Sınav Sonuçları (List Comprehension ile):", sonuc)

