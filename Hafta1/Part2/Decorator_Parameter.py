def double(fn):
    def inner(isim):
        fn(isim)
        fn(isim)
    return inner

@double
def merhaba(isim):
    print(f"Merhaba {isim}")

@double
def selam(isim):
    print(f"Selam {isim}")

merhaba("Ahmet")
selam("Mehmet")

#############################################

def double(fn):
    def inner(*args, **kwargs):  #Bu şekilde yazrasak fonksiyonun aldığı tüm argümanları alırız. farklı parametre sayıları kullanılabilir artık.
        fn(*args, **kwargs)
        return fn(*args, **kwargs) #Buraya return eklemeliyiz.
    return inner

@double
def merhaba():
    print("Merhaba")

@double
def selam(isim):
    print(f"Selam {isim}")

@double
def iyi_gunler():
    return "İyi günler"  #Bu fonksiyon bir değer döndürüyor ama bizim ana double da return yok bu yüzden None döner.

merhaba()
selam("Mehmet")
iyi_gunler()

##############################################333

def rapor_dec(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} fonksiyonu çağrıldı.")
        result = func(*args, **kwargs)
        print("--> İşlem başarıyla bitti.")
        return result
    return wrapper

@rapor_dec
def topla(a, b):  #Burda artık istediğin kadar parametre alabilirsin.
    return a + b

print(topla(5, 3))
