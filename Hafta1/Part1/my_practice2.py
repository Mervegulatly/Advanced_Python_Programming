# Question 6: Veri temizleme sorusu
ham_veriler = ["Ahmet  "," ", "  Meryem",None, "Ali"," ", " Selin"]

#1 None ve sadece boşluktan oluşan verileri filter ile ayıklama.
temiz_veriler = list(filter(lambda veri : veri is not None and veri.strip() != "", ham_veriler)) 
print("Temiz Veriler:", temiz_veriler)

#2 Kalan isimlerin sağındaki veya solundaki bpşukları map ve strip() ile temizleme.
temizlenmis_veriler = list(map(lambda veri : veri.strip(), temiz_veriler))
print("Temizlenmiş Veriler:", temizlenmis_veriler)


################################################################################

ogrenciler = [
{"ad": "Lale", "notlar": [70, 80, 90]},
{"ad": "Deniz", "notlar": [40, 50, 30]},
{"ad": "Arda", "notlar": [90, 95, 100]},
{"ad": "Zeynep", "notlar": [60, 60, 70]} ]

#1 map ve lambda kullanarak her öğrencinin ortalama isminde yeni bir anahtar ve hesapladığınız ortamayı ekleyin.
ortalama = list(map(lambda student : {**student, "ortalama": sum(student["notlar"])/len(student["notlar"])}, ogrenciler))
print("Öğrenciler ve Ortalamaları:", ortalama)

#2 ortalaması 70 ve üzeri olan öğrencileri filter ve lambda başarılıları bulma.
basarili = list(filter(lambda student : student["ortalama"] >=70, ortalama))
print("Başarılı Öğrenciler:", basarili)

#3 sorted ve lambda kullanarak öğrencileri ortalamalarına göre büyükten küçüğe sıralama.
sirali_ortalama = sorted(ortalama, key=lambda student: student["ortalama"], reverse=True)
print("Sıralı Ortalamalar:", sirali_ortalama)