def selamlama_dec(count):  #Bu şekilde decorator kullanılan fonksiyonlar kendi içinde özelleşebilir.
    def selamlama(fn):
        def inner(isim):
            for i in range(count):
                fn(isim)
        return inner
    return selamlama

@selamlama_dec(count = 5)  #sadece 5 olarak da yazabiliriz.
def merhaba(isim):
    print(f"Merhaba {isim}")

@selamlama_dec(3)
def selam(isim):
    print(f"Selam {isim}")

merhaba("Ahmet")
selam("Mehmet")

############################################

def dec_yetki_kontrol(rol):
    def yetki_kontrol(func):
        def inner(*args, **kwargs):
            kullanici_rol = "admin"  #Kulanıcı rolü yetki kontroldeki rolünden farklı olursa hata mesajı alırsın.

            if kullanici_rol == rol:
                return func (*args, **kwargs)
            else: 
                return (f"Hata: Bunu çalıştırmak için {rol} olmalısınız.")
        return inner
    return yetki_kontrol

@dec_yetki_kontrol("admin")
def admin_sayfa():
    return "Admin paneline Hoş Geldiniz!"

print(admin_sayfa())

############################################

