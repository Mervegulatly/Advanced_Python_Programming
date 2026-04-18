sayilar = [1, 2, 3, 4, 5]
kareler=[]

for i in sayilar:
    kareler.append(i**2)

print(sayilar)
print(kareler)

def kareHesapla(i):
    return i**2

kareleri=list(map(lambda i : i**2, sayilar))  # KareHesapla fonk yerine lambda ile tek satıra düşürdük.
print(kareleri)


text = ["Ebru", "Ayşe", "Ceren"]
sonuc = list(map(lambda x : x.upper(), text)) #upper ile büyük harfe çevirdik.
print(sonuc)

liste = [1.3, 4.8, 8.5]
sonuc2 = list(map(int, liste)) #map in içinde kullanılırken inti parantez kullnaılmaz çünkü tüm listeye uygulammasını istedik.
print(sonuc2)


# Map de kaç eleman varsa o kadar çıkar.