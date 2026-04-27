liste = [1, 2, 3, 4, 5, 6]

iterator = iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break


for i in liste:
    print(i)

print(dir(liste))

print(dir(iterator))