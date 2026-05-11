Bu repo; Python ile veritabanı (SQLite), dosya okuma/yazma (CSV), veri sorgulama ve API’den veri çekme gibi konuları içeren örnek çalışmaları barındırır.

## Genel içerik
- **Hafta1:** Python temelleri (fonksiyonlar, lambda, koleksiyonlar, filtreleme/sıralama vb.)
- **Hafta2:** Nesne yönelimli programlama (class/constructor, encapsulation, inheritance, polymorphism vb.)
- **Hafta3:** Dosya işlemleri (CSV/JSON) + SQLite ile CRUD ve sorgular (Hafta3/Day2 part2)
- **Final_Project:** API’den veri çekme (exchange rate) → SQLite’a kaydetme → sorgulama

---

# Final_Project - Döviz Kurları (API → SQLite)

Bu proje, **exchangerate-api.com** üzerinden döviz kurlarını çekip seçilen para birimlerini **SQLite** veritabanına kaydeder ve temel sorguları ekrana basar.

## İçerik
- `request.py`: API’den kurları çeker, sadece `USD`, `EUR`, `GBP` için `secilen_kurlar` dict’ini oluşturur.
- `insert.py`: `secilen_kurlar` içindeki değerleri `final_db.db` veritabanındaki `kayitlar` tablosuna yazar.
- `db_queries.py`: `kayitlar` tablosu üzerinde örnek SQL sorgularını çalıştırır.
- `DataPipeLine_App.py`: Projenin çalıştırma/akış dosyası (API çekme + tablo/insert + sorgu).

## Gereksinimler
- Python 3.x
- `requests` kütüphanesi

Kurulum:
```bash
pip install requests
```

## Çalıştırma
Proje akış dosyasını çalıştır:
```bash
python DataPipeLine_App.py
```

Ayrıca ayrı ayrı çalıştırmak istersen:
```bash
python request.py
python insert.py
python db_queries.py
```

## Veritabanı
- Dosya: `Final_Project/final_db.db` (proje klasöründe tutulur)
- Tablo: `kayitlar`
  - `id` (PRIMARY KEY)
  - `birim_adi` (TEXT)
  - `deger` (REAL)
  - `islem_tarihi` (TEXT)

## Kaydedilen Veri Nasıl Seçiliyor?
`request.py` içinde API response’un `rates` alanından sadece şu para birimleri alınır:
- `USD`
- `EUR`
- `GBP`

## Not / İpucu (Modül Import)
Dosyalar aynı klasörde olduğu için `Final_Project` klasöründen çalıştırmak import problemini azaltır. Örn:
```bash
cd Final_Project
python insert.py
```

