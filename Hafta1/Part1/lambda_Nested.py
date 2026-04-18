katlayici = lambda n : lambda a : a * n

ikiKatiniAl = katlayici(2)
ucKatiniAl = katlayici(3)

sonuc = ucKatiniAl(10)

print(ikiKatiniAl(10))
print(ucKatiniAl(10))
print(sonuc(5)) #iç içe kabul etmedi sadece tek seferlik kullanılıyor.


