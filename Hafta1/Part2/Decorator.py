def hi(fn):
    def inner(isim):
        print("Hi there!")
        fn(isim)
        print("See you later")
    return inner

@hi
def morning(isim):
    print(f"Good morning, {isim}!")
    print("Have a nice day")
@hi
def evening(isim):
    print(f"Good evening, {isim}!")
    print("Have a nice night")


morning("Ahmet") #g = hi(morning) buna gerek kalmadı
evening("Ayşe") #Decorator sayesinde morning ve evening fonksiyonları hi fonksiyonunun içine gömülür ve hi fonksiyonunun içindeki kodlar çalışır.


###################################################

def susleyici(func):
    def inner(isim):
        print("---Paketi Açıyoruz---")
        func(isim)
        print("---Paketi Kapatıyoruz---")
    return inner

@susleyici
def selamlama(isim):
    print(f"Merhaba, {isim}! nasılsın?")

selamlama("Merve") #g = susleyici(selamlama) buna gerek kalmadı
