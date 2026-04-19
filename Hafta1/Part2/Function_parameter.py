def topla(a, b):
    return a + b

def carpma(a, b):
    return a * b    

def islem(fnc, a, b):
    return fnc(a, b)

print(islem(topla, 30, 40))
print(islem(carpma, 3, 4))

################################################


def kare_alma(x):
    return x ** 2

def kup_alma(x):
    return x ** 3

def islem(fnc, liste):
    sonuc = []
    for i in liste:
        sonuc.append(fnc(i))    
    return sonuc

sayilar = [1, 2, 3, 4, 5]
print(islem(kare_alma, sayilar))
print(islem(kup_alma, sayilar))

##################################################