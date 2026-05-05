import csv  # Comma Separated Values

# ------------------ csv.reader ------------------
with open('urunler3.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)  # başlık satırını atla

    for satir in reader:
        print(satir)
        print(f"Ürün Adı: {satir[0]}, Ürün Fiyatı: {satir[1]}")


# ------------------ csv.DictReader ------------------
with open('urunler3.csv', encoding='utf-8') as file:
    dict_reader = csv.DictReader(file)

    for satir in dict_reader:
        print(satir)
        print(f"Ürün Adı: {satir['Ürün']}, Ürün Fiyatı: {satir['Fiyat']}")