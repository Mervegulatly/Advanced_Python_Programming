def sayi_uret():
    sayi = 0
    while True:
        yield sayi ** 2
        sayi += 1

# print(sayi_uret())

generator = sayi_uret()

# for i in generator:
#     print(i)  # Sonsuza kadar yazdırır


######################################

#Fibonacci seridini hem normal hem de generator ile yazınız

def fibonacci(max):
    fib_list = []
    sayi1, sayi2 = 0, 1
    count = 0

    while count <= max:
        fib_list.append(sayi1)
        sayi1, sayi2 = sayi2, sayi1 + sayi2
        count += 1
    return fib_list

# print(fibonacci(5))

# Fibonacci generator versiyonu ile bulma
def fib_gen(max):
    sayi1, sayi2 = 0, 1
    count = 0

    while count <= max:
        yield sayi2
        sayi1, sayi2 = sayi2, sayi1 + sayi2
        count += 1

for i in fib_gen(20):
    print(i)