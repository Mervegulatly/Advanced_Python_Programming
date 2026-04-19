#Clouser kullanma mantığı fonksiyondan fonksiyon döndürmek için!!

def usAlma(taban):
    def inner(us):
        return taban ** us
    return inner #Parantez koymazsak fonksiyonun kendisini döndürür, parantez koyarsak fonksiyonun sonucunu döndürür.

#Her ikisi de aynı, iç içe fonksiyon gibi.
sonuc = usAlma(3)
print(sonuc(2)) 

sonuc2 = usAlma(5)(2)
print(sonuc2)

##########################################################

def yetki_sorgulama(rol):
    def mesaj_ver(isim):
        return f"{rol} yetkisiyle: merhaba {isim}."
    return mesaj_ver  #Burda fonksiyonun değeriyle değil de işiyle ilgileniyoruz.

admin_yetki = yetki_sorgulama("Admin")
user_yetki = yetki_sorgulama("User")

print(admin_yetki("Merve"))
print(user_yetki("Ali"))

###########################################################

def yetki_sorgulama(sayfa):
    def inner(rol):
        if rol == "Admin":
            return f"{rol} rolü {sayfa} sayfasına erişebilir."
        else:
            return f"{rol} rolü {sayfa} sayfasına erişemez!!"
    return inner

yetki = yetki_sorgulama("Ürün güncelleme")
print(yetki("Admin"))
print(yetki("User"))

########################################################
def hesap_makinesi(islemAdi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islemAdi == "toplama":
        return toplam
    elif islemAdi == "çarpma":
        return carpma
    else:
        return "Geçersiz işlem!"
    
islem = hesap_makinesi("toplama")
sonuc_toplam = islem(1, 2, 3, 4)
print(sonuc_toplam)

islem2 = hesap_makinesi("çarpma")
sonuc_carpma = islem2(1, 2, 3, 4)
print(sonuc_carpma)
