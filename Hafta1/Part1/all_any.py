liste = [True, True, False, True]
sonuc = all(liste)  # all() fonksiyonu, tüm elemanlar aynı ise True döner, değilse False döner.
print("Tüm elemanlar True mu?", sonuc) 


notlar = [50, 85, 45, 90, 95]

sonuc = False

for n in notlar:
    if n < 50:
        sonuc = False
        break

print(sonuc)

#######################################

sonuc = all(n >= 50 for n in notlar) # all() fonksiyonu, tüm elemanlar aynı ise True döner, değilse False döner.
print("Tüm notlar 50 ve üzeri mi?", sonuc)

######################################

liste = [True, False, True, False]
sonuc = any(liste)  # any() fonksiyonu, herhangi bir eleman True ise True döner, tüm elemanlar False ise False döner.
print("En az bir eleman True mu?", sonuc)


######################################

notlar = [30, 85, 45, 90, 100]
sonuc = False

for n in notlar:
    if n == 100:
        sonuc = True
        break
print("En az bir öğrenci 100 puan aldı mı?", sonuc)

notlar2 = [30, 85, 45, 90, 95]
sonuc = any(n == 100 for n in notlar2) 
print("En az bir öğrenci 100 puan aldı mı?", sonuc)