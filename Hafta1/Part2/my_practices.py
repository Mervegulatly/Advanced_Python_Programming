def islem_merkezi(sayi1, sayi2):
    def toplama():
        return sayi1 + sayi2
    
    def cikarma():
        return sayi1 - sayi2
    
    def bolme():
        return sayi1 / sayi2

    return {
        "toplama": toplama(),
        "cikarma": cikarma(),  
        "bolme": bolme()
    }
print(islem_merkezi(10, 5))

##############################################

# Question 2: Logger function create

def logger(seviye):

    def mesaj_yaz(metin):
        print(f"{seviye.upper()}: {metin}")
    return mesaj_yaz

bilgi_log = logger("INFO")
hata_log = logger("ERROR")

bilgi_log("Sistem Çalışıyor.")
hata_log("Bağlantı kesildi.")

###############################################3

import math

def kare_al(n):
    return n ** 2

def kok_al(n):
    return math.sqrt(n) # yada n ** 0.5

def Hesap_makinesi(liste, islem_fonksiyonu):
    sonuc = []
    for i in liste:
        sonuc.append(islem_fonksiyonu(i))
    return sonuc

sayilar = [1, 4, 9, 16]
print(Hesap_makinesi(sayilar, kare_al))
print(Hesap_makinesi(sayilar, kok_al))