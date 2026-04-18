# Question 1: List Comprehension Kullanarak 1 ile 100 arasındaki 12'nin katlarını bulun.
number = [n for n in range(1, 101) if n % 12 == 0]
print("1 ile 100 arasındaki 12'nin katları:", number)


# Question 2: Verilen bir metindeki rakamları listeleyin.
text = "BTK 2026 egitim yılı 5. dönem"
rakamlar = [rkm for rkm in text if rkm.isdigit()]
print("Metindeki Rakamlar:", rakamlar)


# Question 3: Sıcaklık değerlerine göre buzlanma tehlikesi durumunu belirten bir liste oluşturun.
sicakliklar = [10, 2, -3, 5, 0]
Buzlanma = ["Buzlanma Tehlikesi" if sicaklik < 4 else "Normal" for sicaklik in sicakliklar]
print("Sıcaklıklar:", sicakliklar)
print("Buzlanma Durumu:", Buzlanma)


# Question 4: Öğrenci isimleri ve notlarına göre geçip kalma durumunu belirten bir sözlük oluşturun.
students = ["Ali", "Ayşe"]
grades = [40, 70]
results = ["Geçti" if grade >= 50 else "Kaldı" for grade in grades]
sözlük = {student: result for student, result in zip(students, results)}  # zip() Python’da listeyi paralel olarak eşleştirir.
print("Öğrenci Sonuçları Sözlüğü:", sözlük)


# Question 5: İki farklı listede bulunan sayıların çarpımlarını içeren bir liste oluşturun comprehension kullanarak.
# without list comprehension
list = [1, 2, 3]
list2 = [10, 20]
carpimlar = []

for x in list:
    for y in list2:
        carpimlar.append(x * y)
print("Çarpımlar (without list comprehension):", carpimlar)

# with list comprehension
carpimlar2 = [x * y for x in list for y in list2]
print("Çarpımlar (with list comprehension):", carpimlar2)


# Post lardan pasif olanları bulma
users= [
{"username": "ebru_aydogan", "posts": ["Python 101", "İleri Seviye Python", "Data Science"]},
{"username": "btk_akademi", "posts": ["Duyuru", "Yeni Kurs"]},
{"username": "yazilim_ogrencisi", "posts": ["Merhaba Dünya"]},
{"username": "python_coder", "posts": []}
]

pasifKullanicilar=[]

for user in users:
    if len(user["posts"])<2:
        pasifKullanicilar.append(user)

filtered=filter(lambda user: len(user["posts"])<2, users)

pasifler=list(map(lambda user: user["username"], filtered))

print(pasifler)


