import csv

# csv.writer()

urunler = [
    ['Mouse', '4500'],
    ['Klavye', '7800'],
    ['Monitor', '10000']
]

with open('urunler_writer.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Başlık satırı
    writer.writerow(['Ürün', 'Fiyat'])

    # Veriler
    writer.writerows(urunler)

print("writer ile dosya oluşturuldu")

#csv.DictWriter()

fieldnames = ["Ürün", "Fiyat"]

urunler = [
    {'Ürün': 'Laptop', 'Fiyat': '25000'},
    {'Ürün': 'Mouse', 'Fiyat': '4500'},
    {'Ürün': 'Klavye', 'Fiyat': '7800'}
]

with open('urunler_dictwriter.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Başlık yaz
    writer.writeheader()

    # Verileri yaz
    writer.writerows(urunler)

    # Tek satır ekleme
    writer.writerow({'Ürün': 'Monitor', 'Fiyat': '20000'})

print("DictWriter ile dosya oluşturuldu")