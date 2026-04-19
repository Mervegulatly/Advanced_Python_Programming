def Hello(isim):
    print(f"Hello {isim} Function")

merhaba = Hello

Hello("Python")
merhaba("Java")

print(Hello)
print(merhaba)

del Hello  #Hello fonksiyonunu siler

print(merhaba)  #merhaba fonksiyonu hala Hello fonksiyonunu referans ettiği için çalışır. Ana fonksiyon silinse bile referanslar çalışmaya devam eder.
merhaba("C#")
#print(Hello) # Ama bu artık çalışmaz çünkü Hello fonksiyonu silindi.

####################################################

def outer(number):
    print("Hello")
    #print(x) #Bu kabul olmaz çünkü iç de tanımlı dıştan bunu bulamaz.
    def inner(number):  #inner a parametre yazmasan da outer da ki parametre de yeterli olacaktır.
        x = 10
        print(f"Girdiğiniz sayi :{number}")
    inner(number) #Encapsulation sağlar

#outer direkt çağırılmaz inner ı da çağırmamız gerek

outer(15)

###################################################

#Faktoriyel hesaplama Nested versionu

def factorial(number):
    def inner(number):
        if number <= 1:
            return 1
        return number*inner(number-1)  #Burda inner a parametre yazdığın için fonsiyonda da parametre almalı
    return inner(number)
    
sonuc = factorial(3)
print(sonuc)

#############################################
#İnner fonksiyonun parametre almak zorunda olmadığı versiyon  ???????????

def factorial2(number):
    def inner2(n):
        if n <= 1:
            return 1
        return n * inner2(n - 1)
    return inner2(number)

sonuc = factorial2(3)
print(sonuc)

########################################

def factorial_rec(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    
    if not number >= 0:
        raise ValueError("Number must be zero or positive")

    def inner(number):
        if number <= 1:
            return 1
        return number*inner(number-1)
    return inner(number)

sonuc = factorial_rec(5)
try:   
    sonuc = factorial_rec("4")  #Bu bir string olduğu için TypeError verecektir.
    print(sonuc)

except TypeError as ex:
    print(ex)