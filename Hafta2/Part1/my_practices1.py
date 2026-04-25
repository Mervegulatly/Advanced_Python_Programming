class Ogrenci():

    def __init__(self, ad, soyad, ders_notu):
        self.ad = ad
        self.soyad = soyad
        self.ders_notu = ders_notu

    def durum_sorgula(self):
        return "Basarili" if self.ders_notu >= 50 else "Basarisiz"
            
ogrenci1 = Ogrenci("Merve", "Atalay", 90)
ogrenci2 = Ogrenci("Ali", "Demir", 23)

print(Ogrenci.durum_sorgula(ogrenci1))
print(Ogrenci.durum_sorgula(ogrenci2))


####################################################

class Urun():

    urun_adet = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Urun.urun_adet += 1

    @classmethod
    def toplam_urun_sayisini_getir(cls):
        return cls.urun_adet

urun1 = Urun("Telefon", 2000, 3)
urun2 = Urun("Bilgisayar", 80000, 2)
urun3 = Urun("Tablet", 30000, 2)

print(Urun.toplam_urun_sayisini_getir())

####################################################


class Robot():

    toplam_robot_sayisi = 0

    def __init__(self, name):
        self.name = name
        Robot.toplam_robot_sayisi += 1

    def selamla(self):
        print(f"Merhaba, ben {self.name}")

    @classmethod
    def robot_sayisini_sorgula(cls):
        return cls.toplam_robot_sayisi
    
robot1 = Robot("Robo1")
robot2 = Robot("Robo2")  #Nesne oluşturmayı unutmaa!!!

print(f"Şu an dünyada {Robot.robot_sayisini_sorgula()} tane robot var")
