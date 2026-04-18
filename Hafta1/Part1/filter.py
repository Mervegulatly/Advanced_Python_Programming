numbers = [-3, 5, 8, -1, -4]

# Klasik yöntemle negatif sayıları bulma
# negatives = []

# for i in numbers:
#     if i < 0:
#         negatives.append(i)
# print(negatives)


########################################################
def negatives(i):
    return i < 0

# list kullanarak obje olarak döndürdük.
negatives2 = list(filter(negatives, numbers)) #filter ile tek satırda negatif sayıları bulduk.
print(negatives2)

########################################################


negatives3 = list(filter(lambda i : i < 0, numbers)) #lambda ile tek satırda negatif sayıları bulduk.
print(negatives3)


#########################################################

isimler = ["Ebru", "Ayşe", "Ceren", "Ali"]
A_ile_baslayanlar = []
for isim in isimler:
    if isim.startswith("A"):
        A_ile_baslayanlar.append(isim)
print(isimler)
print(A_ile_baslayanlar)


A_ile_baslayanlar = list(filter(lambda x : x.startswith("A"), isimler)) # A ile başlayanları bulduk.
print(A_ile_baslayanlar)


############################################################
isimler2 = ["ebru", "ayşe", "ceren", "ali", "Ahmet"]
a_ile_baslayanlar2 = list(filter(lambda x : x[0] == 'a', isimler2))

buyuk_harfe_cevirme = list(map(lambda x : x.upper(), a_ile_baslayanlar2)) # A ile başlayanları bulduk ve büyük harfe çevirdik.
print(a_ile_baslayanlar2)
print(buyuk_harfe_cevirme)


# Tek satırda filtreleme ve map işlemi yaparak a ile başlayanları bulup büyük harfe çevirdik.
sonuc = list(map(lambda x : x.upper(), filter(lambda x : x[0] == 'a', isimler2)))  # ne yaptığı, nerede yaptığı ve hangisini yaptığını sırasıyla yaazdık.
print(sonuc)
