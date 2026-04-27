#Büyük veriler kullanılacağı zamna kullanılıyor. 

def count(max):

    sayilar = []
    sayi = 0
    while sayi <= max:
        sayilar.append(sayi)
        sayi += 1
    return sayilar

sonuc = count(15)
print(sonuc)
    
def count_gen(max):
    for i in range(max):
        yield i   # Yield tıpkı Return gibi fakat çağırıldıkça KALDIĞI YERDEN devam eder.

sonuc2 = count_gen(15)
print(sonuc2) 

print(next(sonuc2))
print(next(sonuc2))
print(next(sonuc2))

for x in sonuc2:  
    print(x)

####################################################

my_list = [i**2 for i in range(5)]
print(my_list)

my_gen = (i**2 for i in range(5))  #Bu şekilde bize adresi getirir fazla yer kaplamaz çağırıldıkça gelir.
print(my_gen)
print(next(my_gen)) #Kullanmak istediğimizde çağırıldığı kadar gösterir
print(next(my_gen))