# Tek kullanımlık anonim fonksiyonlar. Sadece birkaç kez kullanılacak fonksiyonlar için kullanılır.

def kareal(sayi):
    return sayi**2
print(kareal(5))

kareal2 = lambda x: x**2
print(kareal2)
print(kareal2(7))


def topla(a, b):
    return a+b
print(topla(5, 6))

topla2=lambda x, y: x+y
print(topla2(7, 8))

print((lambda x, y: x+y)(7, 8))

text="btk akademi"
sonuc= lambda x: x.upper()
print(sonuc(text))